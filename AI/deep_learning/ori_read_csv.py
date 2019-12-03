import tensorflow as tf
import os


def csvread(filelist):
    '''
    读取CSV文件
    :param filename:  路径+文件名的列表
    :return: 读取内容
    '''

    # 1. 构造文件的队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2. 构造csv阅读器读取队列数据（按一行）
    reader = tf.TextLineReader()

    key,value = reader.read(file_queue)

    # 3.对每行内容解码
    # record_defaults:指定每一个样本的每一列的类型，指定默认值[['None'],[4.0]]
    records = [['None'],['None']]

    example,label = tf.decode_csv(value,record_defaults=records)

    # batch_size跟队列，数据的数量没有影响，只决定这批次取多少数据
    # 4. 想要读取多个数据，就需要批处理
    example_batch,label_batch = tf.train.batch([example,label],batch_size=9,num_threads=1,capacity=9)
    # print(example,label)
    return example_batch,label_batch

if __name__ == '__main__':
    # 找到文件，构建列表
    filename = os.listdir('data_source')

    # 拼接路径 重新组成列表
    filelist = [os.path.join('data_source',file) for file in filename]
    print(filelist)

    # 调用函数传参
    example_batch,label_batch = csvread(filelist)

    # 开启会话
    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()

        # 开启读文件的线程
        threads = tf.train.start_queue_runners(sess,coord=coord)

        # 打印读取的内容
        print(sess.run([example_batch,label_batch]))


        # 回收子线程
        coord.request_stop()

        coord.join(threads)