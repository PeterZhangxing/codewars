
import tensorflow as tf
import os
# 不显示程序运行过程中出现的警告信息
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 在以命令行方式运行代码时，将参数从命令行读入到脚本
# 1、首先定义有哪些参数需要在运行时候指定
# 2、程序当中获取定义命令行参数
# 3、参数：名字，默认值，说明
tf.app.flags.DEFINE_integer("max_step", 100, "模型训练的步数")
tf.app.flags.DEFINE_string("model_dir", "tmp/ckpt/", "模型文件的加载的路径")

# 定义存储了命令行参数的对象
FLAGS = tf.app.flags.FLAGS


def myregression():
    '''
    自己实现的线性回归算法
    :return:
    '''
    # 定义一个命名空间，提高程序可读性，并且在图中更易读
    with tf.variable_scope("raw_data"):
        # 1、准备数据，x 特征值 [100, 1]   y 目标值[100]
        # 随机生成100行1列的特征值数据，分别指定平均值、标准差，和在图中x的名字
        x = tf.random_normal([100,1],mean=1.75,stddev=0.5,name="x_data")
        # 利用矩阵乘法，生成与特征值对应的目标值
        # 矩阵相乘必须是二维的
        y_true = tf.matmul(x,[[0.7]]) + 0.8

    with tf.variable_scope("model"):
        # 2、建立线性回归模型 1个特征，1个权重， 一个偏置 y = x w + b
        # 随机给一个权重和偏置的值，让他去计算损失，然后再当前状态下优化
        # 用变量定义才能优化
        # trainable参数：指定这个变量是否能跟着梯度下降一起优化
        weight = tf.Variable(tf.random_normal([1,1], mean=0.0, stddev=1.0),name="weight")
        bias = tf.Variable(0.0,name="bias")
        y_predict = tf.matmul(x,weight) + bias

    with tf.variable_scope("loss"):
        # 3、建立损失函数，计算均方误差
        # 先求真实值和预测值的差的平方，然后把每个平方值加在一起，再求平均值
        loss = tf.reduce_mean(tf.square(y_true-y_predict))

    with tf.variable_scope("optimizer"):
        # 4、指定梯度下降的速率，训练线性回归模型
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # 收集tensor,用于展示在tensorboard中
    # 收集一维tensor
    tf.summary.scalar("losses",loss)
    # 收集多维tensor
    tf.summary.histogram("weights",weight)
    # 合并收集到的tensor
    merged = tf.summary.merge_all()

    # 定义初始化变量的op,变量不初始化不能使用
    init_op = tf.global_variables_initializer()

    # 定义一个保存模型训练到过程中产生的数据的对象，使得下次训练可以从断点开始，而不是从头开始
    saver = tf.train.Saver()

    # 开启会话，运行程序
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 打印随机初始化的权重和偏置
        print("随机初始化的参数权重为：%f, 偏置为：%f" % (weight.eval(), bias.eval()))

        # 建立事件文件，保存收集到的tensor和图等数据
        filewriter = tf.summary.FileWriter("tmp/summary/test/",graph=sess.graph)

        # 判断是不是保存过模型的训练过程中产生的参数，
        # 如果有则覆盖模型当中随机定义的参数，从上次训练的参数结果开始训练
        if os.path.exists("tmp/ckpt/checkpoint"):
             saver.restore(sess,"tmp/ckpt/")

        # 循环训练模型，运行优化模型
        for i in range(FLAGS.max_step):
            sess.run(train_op)

            # 获取合并的参数，写入到事件文件中
            summary = sess.run(merged)
            filewriter.add_summary(summary,i)

            print("第%d次优化的参数权重为：%f, 偏置为：%f" % (i, weight.eval(), bias.eval()))

        saver.save(sess,"tmp/ckpt/")

    return None


if __name__ == '__main__':
    myregression()