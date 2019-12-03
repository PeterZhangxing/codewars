import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_integer("is_train", 0, "指定程序是预测还是训练")


def full_connected():
    '''
    使用简单全连接神经网络，识别手写数字[0-9]
    :return:
    '''
    # 从文件中获取数据
    mnist = input_data.read_data_sets("data_source/mnist/input_data/",one_hot=True)

    # 1、建立数据的占位符，图片特征值：x[None, 784]，图片标签：y_true[None, 10]
    with tf.variable_scope("raw_data"):
        x = tf.placeholder(tf.float32,[None,784])
        y_true = tf.placeholder(tf.int32,[None,10])

    # 2、建立一个全连接层的神经网络,计算预测值，每一个神经元的权重:w[784, 10],每个神经元的偏移量:b[10]
    with tf.variable_scope("fc_model"):
        # 随机初始化权重和偏移量
        weight = tf.Variable(tf.random_normal([784,10],mean=0.0,stddev=1.0),name="weight")
        bias = tf.Variable(tf.constant(0.0,shape=[10]),name="bias")
        # 预测None个样本的输出结果matrix [None, 784]* [784, 10] + [10] = [None, 10]
        y_predict = tf.matmul(x,weight) + bias

    # 3、求出所有样本的损失，然后求平均值
    with tf.variable_scope("soft_cross"):
        # 求平均交叉熵损失
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))

    # 4、梯度下降求出损失最小的weight和bias
    with tf.variable_scope("optimizer"):
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # 5、计算准确率
    with tf.variable_scope("accuracy"):
        equal_list = tf.equal(tf.argmax(y_true,1),tf.argmax(y_predict,1))
        # equal_list: 两个矩阵比较，每一行最大值的下标相等，就是1，否则是0，最后求平均值就是准确率
        # equal_list形状：[1, 0, 1, 0, 1, 1,..........]
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 收集变量 单个数字值收集
    tf.summary.scalar("losses", loss)
    tf.summary.scalar("acc", accuracy)

    # 高纬度变量收集
    tf.summary.histogram("weightes", weight)
    tf.summary.histogram("biases", bias)

    # 定义一个合并变量de op
    merged = tf.summary.merge_all()

    # 定义初始化变量的op
    init_op = tf.global_variables_initializer()

    # 创建存储训练结果的对象
    saver = tf.train.Saver()

    # 开启会话，训练模型
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 建立events文件，存储训练过程中保存的变量和图等值
        filewriter = tf.summary.FileWriter("tmp/summary/test/", graph=sess.graph)

        if FLAGS.is_train == 1:
            # 迭代步数去训练，更新权重和偏置值
            for i in range(5000):
                # 取出真实存在的特征值和目标值,每次取50个样本
                mnist_x,mnist_y = mnist.train.next_batch(50)
                # 使用样本训练模型
                sess.run(train_op,feed_dict={x:mnist_x,y_true:mnist_y})
                # 将每次训练的结果保存到events文件
                summary = sess.run(merged,feed_dict={x:mnist_x,y_true:mnist_y})
                filewriter.add_summary(summary, i)
                print("训练第%d步,准确率为:%f" % (
                    i,
                    sess.run(accuracy, feed_dict={x: mnist_x, y_true: mnist_y})))
            # 保存训练好的模型
            saver.save(sess,"tmp/ckpt/fc_model")
        else:
            # 使用模型进行预测
            saver.restore(sess,"tmp/ckpt/fc_model")
            for i in range(100):
                # 每次测试一张图片 [0,0,0,0,0,1,0,0,0,0]
                x_test, y_test = mnist.test.next_batch(1)
                ytrue_argmax_index = tf.argmax(y_test,1).eval()
                # ypre_argmax_index = tf.argmax(sess.run(y_predict,feed_dict={x: x_test, y_true: y_test}),1).eval()
                ypre_argmax_index = tf.argmax(sess.run(y_predict,feed_dict={x: x_test,}),1).eval()
                print("第%d张图片，手写数字图片目标是:%d, 预测结果是:%d"%(i,ytrue_argmax_index,ypre_argmax_index))
    return None


if __name__ == '__main__':
    full_connected()