import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("captcha_dir","data_source/tfrecords/captcha.tfrecords", "验证码数据的路径")
tf.app.flags.DEFINE_integer("batch_size",100,"每批次训练的样本数")
tf.app.flags.DEFINE_integer("label_num",4,"每个样本的目标值数量")
tf.app.flags.DEFINE_integer("letter_num",26,"每个目标值的取值可能性")


def init_weight_var(shape):
    '''
    按照传入的形状，生成随机数组成的初始权重值
    :param shape:
    :return:
    '''
    w = tf.Variable(
        tf.random_normal(
            shape=shape,
            mean=0.0,
            stddev=1.0,
        )
    )
    return w


def init_bias_var(shape):
    '''
    按照传入的形状，生成初始偏置值
    :param shape:
    :return:
    '''
    b = tf.Variable(
        tf.constant(
            0.0,
            shape=shape
        )
    )
    return b


def read_tf_file():
    '''
    读取存储了图片特征值和标签值的tfrecords文件，
    并进行解码
    :return:
    '''
    # 读取指定文件夹中的所有tfrecords文件,放入文件队列
    file_queue = tf.train.string_input_producer([FLAGS.captcha_dir])

    # 构建tf文件的阅读器
    reader = tf.TFRecordReader()

    # 读取第一个样本，并解码
    key,value = reader.read(file_queue)

    # 解析一个样本的内容
    features = tf.parse_single_example(
        value,
        features={
            "image":tf.FixedLenFeature([],tf.string),
            "label":tf.FixedLenFeature([],tf.string),
        }
    )
    image = tf.decode_raw(features["image"], tf.uint8)
    label = tf.decode_raw(features["label"], tf.uint8)

    # 改变形状
    img_reshaped = tf.reshape(image,[20,80,3])
    lab_reshaped = tf.reshape(label,[4])

    # 使用子线程，批量读取样本数据
    img_batch,lab_batch = tf.train.batch(
        [img_reshaped,lab_reshaped],
        batch_size=FLAGS.batch_size,
        num_threads=1,
        capacity=FLAGS.batch_size
    )

    return img_batch,lab_batch


def deep_model(img):
    '''
    本次采用即卷积模型
    :param img: 100图片特征值[100, 20, 80, 3]
    :return: y_predict预测值[100, 4 * 26]
    '''
    with tf.variable_scope("conv1"):
        # 随机初始化权重, 偏置[32]
        w_conv1 = init_weight_var([3, 3, 3, 32])
        b_conv1 = init_bias_var([32])

        # 对x进行形状的改变[100, 20, 80, 3]
        x_shaped = tf.reshape(img,[-1,20,80,3])
        x_shaped = tf.cast(x_shaped,tf.float32)

        # 进行过滤和激活：[None, 20,80,3]-----> [None, 20,80,32]
        x_relu1 = tf.nn.relu(
            tf.nn.conv2d(
                x_shaped,
                w_conv1,
                strides=[1,1,1,1],
                padding="SAME"
            ) + b_conv1
        )

        # 池化 2*2 ,strides2 [None, 20, 80, 32]---->[None, 10, 40, 32]
        x_pool1 = tf.nn.max_pool(
            x_relu1,
            ksize=[1,2,2,1],
            strides=[1,2,2,1],
            padding="SAME"
        )

    with tf.variable_scope("conv2"):
        # 随机初始化权重, 偏置[64]
        w_conv2 = init_weight_var([3, 3, 32, 64])
        b_conv2 = init_bias_var([64])

        # 卷积，激活计算 [None, 10, 40, 32]-----> [None,10, 40, 64]
        x_relu2 = tf.nn.relu(
            tf.nn.conv2d(
                x_pool1,
                w_conv2,
                strides=[1, 1, 1, 1],
                padding="SAME"
            ) + b_conv2
        )

        # 池化 2*2, strides 2, [None, 10, 40, 64]---->[None, 5, 20, 64]
        x_pool2 = tf.nn.max_pool(
            x_relu2,
            ksize=[1, 2, 2, 1],
            strides=[1, 2, 2, 1],
            padding="SAME"
        )

    # 全连接层
    with tf.variable_scope("fc"):
        # 随机初始化权重和偏置
        w_fc = init_weight_var([5 * 20 * 64, 4 * 26])
        b_fc = init_bias_var([4 * 26])

        # 修改形状 [None, 5, 20, 64] --->None, 5 * 20 * 64]
        x_fc_reshaped = tf.reshape(x_pool2, [-1, 5 * 20 * 64])
        # 进行矩阵运算得出每个样本的104个结果
        # y_predict = tf.matmul(tf.cast(x_fc_reshaped,tf.float32),w_fc) + b_fc
        y_predict = tf.matmul(x_fc_reshaped,w_fc) + b_fc

    return y_predict


def predict_to_onehot(label):
    """
    将读取文件当中的目标值转换成one-hot编码
    :param label: [100, 4] [[13, 25, 15, 15], [19, 23, 20, 16]...]
    :return: one-hot
    """
    # 进行one_hot编码转换，提供给交叉熵损失计算，准确率计算[100, 4, 26]
    label_onehot = tf.one_hot(label, depth=FLAGS.letter_num, on_value=1.0, axis=2)
    # print(label_onehot)
    '''
    Tensor("one_hot:0", shape=(100, 4, 26), dtype=float32)
    '''
    return label_onehot


def rec_captcha():
    '''
    计算误差，使用梯度下降减小熵差，训练模型，存储模型
    :return:
    '''
    # 1、读取验证码的数据文件 label_btch [100 ,4]
    image_batch, label_batch = read_tf_file()
    # image_batch = tf.cast(image_batch,tf.float32)

    # 2、通过输入图片特征数据，建立模型，得出预测结果
    # 通过两层卷积网络，一层全连接神经网络进行预测
    y_predict = deep_model(image_batch)

    # 3、把目标值转换成one-hot编码 [100, 4, 26]
    y_true = predict_to_onehot(label_batch)

    # 4、softmax计算, 交叉熵损失计算
    with tf.variable_scope("soft_cross"):
        # 求平均交叉熵损失 ,y_true [100, 4, 26]--->[100, 4*26]
        loss = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits_v2(
                labels=tf.reshape(y_true, [FLAGS.batch_size, FLAGS.label_num * FLAGS.letter_num]),
                logits=y_predict)
        )

    # 5、梯度下降优化损失
    with tf.variable_scope("optimizer"):
        train_op = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

    # 6、求出样本的每批次预测的准确率是多少，要进行三维比较
    with tf.variable_scope("acc"):
        # 比较每个预测值和目标值,最大那个值的位置是否一样,
        # 3位比较时，需要第三个维度上的4个目标值都相同，才算这一个样本预测准确。
        # y_predict [100, 4 * 26]---->[100, 4, 26]
        equal_list = tf.equal(
            tf.argmax(y_true, 2),
            tf.argmax(tf.reshape(y_predict, [FLAGS.batch_size, FLAGS.label_num, FLAGS.letter_num]), 2)
        )
        # equal_list  100个样本   [1, 0, 1, 0, 1, 1,..........]
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 定义一个初始化变量的op
    init_op = tf.global_variables_initializer()

    # 创建存储训练结果的对象
    saver = tf.train.Saver()

    # 开启会话训练
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 定义线程协调器和开启线程（有数据在文件当中读取提供给模型）
        coord = tf.train.Coordinator()
        # 开启线程去运行读取文件操作
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 训练识别程序
        for i in range(5000):
            sess.run(train_op)
            print("第%d批次的准确率为：%f" % (i, accuracy.eval()))

        # 保存训练好的模型
        saver.save(sess, "tmp/ckpt/fc_model")

        # 回收读取样本数据的线程
        coord.request_stop()
        coord.join(threads)

    return None


if __name__ == '__main__':
    rec_captcha()