import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


def csv_read(filelist):
    '''
    使用子线程读取数据放入队列，
    主线程从队列中读取数据处理，训练模型
    :param filelist:文件路径+名字的列表
    :return:读取的内容
    '''
    # 1、构造内容为文件路径的队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2、构造csv阅读器对象，读取队列的第一行数据
    reader = tf.TextLineReader()
    key,value =reader.read(file_queue)

    # 3、对读取的每行内容进行解码，设定每一列是什么类型的值
    # record_defaults:指定每一个样本的每一列的类型，指定默认值[["None"], [4.0]]
    records = [["None"],["None"]]
    example,label = tf.decode_csv(value,record_defaults=records)
    # print(example,label)
    '''
    Tensor("DecodeCSV:0", shape=(), dtype=string) 
    Tensor("DecodeCSV:1", shape=(), dtype=string)
    '''

    # 4、通过批处理方法，一次从样本队列中读取多个样本,
    # batch_size:一次读取多少个样本，num_threads：开启几个子线程读取，capacity:队列的大小,
    # 返回值是每一列的数据组成的数组
    example_batch,label_batch = tf.train.batch([example,label],batch_size=9,num_threads=1,capacity=9)
    # print(example_batch, label_batch)
    '''
    Tensor("batch:0", shape=(9,), dtype=string) 
    Tensor("batch:1", shape=(9,), dtype=string)
    '''

    return example_batch, label_batch


if __name__ == '__main__':
    # 构建所有数据文件的绝对路径
    file_name_li = os.listdir("data_source/csvdata")
    file_path_li = [os.path.join("data_source/csvdata",file_name) for file_name in file_name_li]
    # print(file_path_li)

    # 运行批量读取csv文件的函数
    example_batch, label_batch = csv_read(file_path_li)
    # print(example_batch, label_batch)

    with tf.Session() as sess:
        # 定义一个用于控制子线程的线程协调器
        coord = tf.train.Coordinator()

        # 搜索所有的子线程开始运行
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 打印读取的内容
        print("batch:",sess.run([example_batch, label_batch]))
        '''
        batch: [array([b'test3a', b'test3b', b'test3c', b'test1a', b'test1b', b'test1c',
           b'test2a', b'test2b', b'test2c'], dtype=object), 
           array([b'csv3a', b'csv3b', b'csv3c', b'csv1a', b'csv1b', b'csv1c',
           b'csv2a', b'csv2b', b'csv2c'], dtype=object)]

        '''
        # 停止读取文件的子线程，子线程结束，则主线程结束
        coord.request_stop()
        coord.join(threads)