import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


def picfile_read(filelist):
    '''
    读取图片文件，并且转换为张量
    :param filelist:文件路径+ 名字的列表
    :return:每张图片的张量
    '''
    # 1、构造文件队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2、构造文件读取对象，读取图片文件（默认只能读取一张图片）
    reader = tf.WholeFileReader()
    # key是文件名，value是文件
    key,value = reader.read(file_queue)
    # print(value)
    '''
    Tensor("ReaderReadV2:1", shape=(), dtype=string)
    '''

    # 3、对读取的图片数据进行解码
    image = tf.image.decode_jpeg(value)
    # print(image)
    '''
    Tensor("DecodeJpeg:0", shape=(?, ?, ?), dtype=uint8)
    '''

    # 4、统一图片的大小，使得所有图片都是一样的像素
    image_resized = tf.image.resize_images(image,[200,200])
    # print(image_resized)
    '''
    Tensor("resize/Squeeze:0", shape=(200, 200, ?), dtype=float32)
    '''

    # 5、固定样本数据的形状为：[200, 200, 3],表示图片的长、宽、颜色
    # 在进行批处理的时候，要求所有数据形状必须被定义
    image_resized.set_shape([200,200,3])
    # print(image_resized)
    '''
    Tensor("resize/Squeeze:0", shape=(200, 200, 3), dtype=float32)
    '''

    # 6、批处理图片文件
    image_batch = tf.train.batch([image_resized],batch_size=5,num_threads=1,capacity=5)
    # print(image_batch)
    '''
    Tensor("batch:0", shape=(5, 200, 200, 3), dtype=float32)
    '''
    return image_batch


if __name__ == '__main__':
    # 构建所有数据文件的绝对路径
    file_name_li = os.listdir("data_source/picfiles")
    file_path_li = [os.path.join("data_source/picfiles",file_name) for file_name in file_name_li]
    # print(file_path_li)

    # 读取图片文件，返回图片文件向量
    image_batch = picfile_read(file_path_li)

    with tf.Session() as sess:
        # 定义一个用于控制子线程的线程协调器
        coord = tf.train.Coordinator()

        # 搜索所有的子线程开始运行
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 打印读取的内容
        print(sess.run([image_batch,]))
        '''
        [array([[[[8.20000000e+01, 6.00000000e+01, 3.90000000e+01],
         [8.90000000e+01, 6.70000000e+01, 4.40000000e+01],
         [8.88399963e+01, 6.38399963e+01, 4.18399963e+01],
         ...,
        '''
        # 停止读取文件的子线程，子线程结束，则主线程结束
        coord.request_stop()
        coord.join(threads)