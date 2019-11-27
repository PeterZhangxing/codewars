import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# 复杂大数据使用google的这个卷积网络预测和测试
from tensorflow.contrib.slim.python.slim.nets.inception_v3 import inception_v3_base
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


def weight_variables(shape):
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


def bias_variables(shape):
    '''
    按照传入的形状，生成偏置值
    :param shape:
    :return:
    '''
    b = tf.Variable(
        tf.constant(0.0,shape=shape)
    )
    return b


def model():
    '''
    自定义一个卷积模型
    :return:
    '''
    # 1、准备数据的占位符，x:[None, 784],y_true:[None, 10]
    with tf.variable_scope("data"):
        x = tf.placeholder(tf.float32,[None,784])
        y_true = tf.placeholder(tf.int32,[None,10])

    # 2、定义第一层卷积层，卷积: 5*5*1，32个观察者，移动步幅strides=1，激活函数tf.nn.relu，池化
    with tf.variable_scope("conv1"):
        # 随机初始化权重, 偏置[32]
        w_conv1 = weight_variables([5, 5, 1, 32])
        b_conv1 = bias_variables([32])

        # 对x进行形状的改变[None, 784]  [None, 28, 28, 1]
        x_shaped = tf.reshape(x,[-1,28,28,1])

        # 进行过滤和激活：[None, 28, 28, 1]-----> [None, 28, 28, 32]
        x_relu1 = tf.nn.relu(
            tf.nn.conv2d(
                x_shaped,
                w_conv1,
                strides=[1,1,1,1],
                padding="SAME"
            ) + b_conv1
        )

        # 池化 2*2 ,strides2 [None, 28, 28, 32]---->[None, 14, 14, 32]
        x_pool1 = tf.nn.max_pool(
            x_relu1,
            ksize=[1,2,2,1],
            strides=[1,2,2,1],
            padding="SAME"
        )

    # 3、定义第二层卷积层，5*5*32，64个filter，strides=1 激活: tf.nn.relu 池化：
    with tf.variable_scope("conv2"):
        # 随机初始化权重, 偏置[32]
        w_conv2 = weight_variables([5, 5, 32, 64])
        b_conv2 = bias_variables([64])

        # 卷积，激活，池化计算 [None, 14, 14, 32]-----> [None, 14, 14, 64]
        x_relu2 = tf.nn.relu(
            tf.nn.conv2d(
                x_pool1,
                w_conv2,
                strides=[1,1,1,1],
                padding="SAME"
            ) + b_conv2
        )

        # 池化 2*2, strides 2, [None, 14, 14, 64]---->[None, 7, 7, 64]
        x_pool2 = tf.nn.max_pool(
            x_relu2,
            ksize=[1,2,2,1],
            strides=[1,2,2,1],
            padding="SAME"
        )

    # 4、全连接层 [None, 7, 7, 64]--->[None, 7*7*64]*[7*7*64, 10]+ [10] =[None, 10]
    with tf.variable_scope("full_connect"):
        # 随机初始化权重和偏置
        w_fc = weight_variables([7 * 7 * 64, 10])
        b_fc = bias_variables([10])

        # 修改形状 [None, 7, 7, 64] --->None, 7*7*64]
        x_fc_reshaped = tf.reshape(x_pool2, [-1, 7 * 7 * 64])
        # 进行矩阵运算得出每个样本的10个结果
        y_predict = tf.matmul(x_fc_reshaped,w_fc) + b_fc

    return x,y_true,y_predict


def conv_fc():
    '''
    使用真实数据训练模型
    :return:
    '''
    # 从文件中获取数据
    mnist = input_data.read_data_sets("data_source/mnist/input_data/",one_hot=True)

    # 从模型得到输出结果
    x, y_true, y_predict = model()

    # 求出所有样本的损失，然后求平均值
    with tf.variable_scope("soft_cross"):
        # 求平均交叉熵损失,越小越好
        loss = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict)
        )

    # 梯度下降求出损失最小的weight和bias
    with tf.variable_scope("optimizer"):
        train_op = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

    # 5、计算准确率
    with tf.variable_scope("accuracy"):
        equal_list = tf.equal(tf.argmax(y_true,1),tf.argmax(y_predict,1))
        # equal_list: 两个矩阵比较，每一行最大值的下标相等，就是1，否则是0，最后求平均值就是准确率
        # equal_list形状：[1, 0, 1, 0, 1, 1,..........]
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 定义初始化变量的op
    init_op = tf.global_variables_initializer()

    # 创建存储训练结果的对象
    saver = tf.train.Saver()

    # 开启会话运行代码
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 循环训练模型
        for i in range(2000):
            # 每次取50个样本，进行训练
            mnist_x,mnist_y = mnist.train.next_batch(50)
            sess.run(train_op,feed_dict={x: mnist_x, y_true: mnist_y})
            print("训练第%d步,准确率为:%f" % (
                i,
                sess.run(accuracy, feed_dict={x: mnist_x, y_true: mnist_y})
                )
            )
        # 保存训练好的模型
        saver.save(sess, "tmp/ckpt/fc_model")
    return saver


def predict_from_model(filepath="tmp/ckpt/fc_model"):
    '''
    从文件中读取训练好的模型，进行预测
    :param filepath:
    :return:
    '''
    mnist = input_data.read_data_sets("data_source/mnist/input_data/", one_hot=True)
    x, y_true, y_predict = model()
    saver = tf.train.Saver()

    with tf.Session() as sess:
        saver.restore(sess, filepath)

        for i in range(100):
            # 每次测试一张图片 [0,0,0,0,0,1,0,0,0,0]
            x_test, y_test = mnist.test.next_batch(1)
            ytrue_argmax_index = tf.argmax(y_test, 1).eval()
            # ypre_argmax_index = tf.argmax(sess.run(y_predict,feed_dict={x: x_test, y_true: y_test}),1).eval()
            ypre_argmax_index = tf.argmax(sess.run(y_predict, feed_dict={x: x_test, }), 1).eval()
            print("第%d张图片，手写数字图片目标是:%d, 预测结果是:%d" % (i, ytrue_argmax_index, ypre_argmax_index))


if __name__ == '__main__':
    # 训练模型
    # conv_fc()

    # 使用存储的模型预测结果
    predict_from_model()