import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


# 定义cifar的数据等命令行参数
FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("cifar_dir", "data_source/cifar10/cifar-10-batches-bin/", "图片二进制文件的目录")
tf.app.flags.DEFINE_string("cifar_tfrecords", "tmp/cifar.tfrecords", "目标tfrecords文件")


class CifarRead(object):
    '''
    从存储图片信息的二进制文件中读取图片特征和分类，
    并且写进tfrecords文件，或者读取tfrecords文件
    '''
    def __init__(self,filelist,height=32,width=32,channel=3):
        # 要读取的文件的路径列表
        self.filelist = filelist

        # 定义读取的图片的一些属性
        self.height = height
        self.width = width
        self.channel = channel

        # 定义图片特征值及所属类别占的字节数，求出每张图片总的字节数
        self.label_bytes = 1
        self.image_bytes = self.height * self.width * self.channel
        self.bytes = self.label_bytes + self.image_bytes


    def binary_read_decode(self):
        '''
        读取二进制文件的内容，并解码
        :return:
        '''
        # 1、构造文件队列
        file_queue = tf.train.string_input_producer(self.filelist)

        # 2、构造二进制文件读取对象，读取文件内容, 要设定每个样本的字节数，即每次读取多少字节
        reader = tf.FixedLengthRecordReader(self.bytes)
        key,value = reader.read(file_queue)

        # 3、解码内容, 二进制文件内容的解码
        label_image = tf.decode_raw(value,tf.uint8)
        # print(label_image)
        '''
        Tensor("DecodeRaw:0", shape=(?,), dtype=uint8)
        '''

        # 4、分割出图片和标签数据，切出特征值和目标值
        label = tf.cast(tf.slice(label_image,[0],[self.label_bytes]),tf.int32)
        image = tf.slice(label_image,[self.label_bytes],[self.image_bytes])

        # 5、可以对图片的特征数据进行形状的改变 [3072] --> [32, 32, 3]
        image_reshaped = tf.reshape(image,[self.height, self.width, self.channel])
        # print(label,image_reshaped)
        '''
        Tensor("Cast:0", shape=(1,), dtype=int32) 
        Tensor("Reshape:0", shape=(32, 32, 3), dtype=uint8)
        '''

        # 6、批处理数据
        label_batch,image_batch = tf.train.batch(
            [label,image_reshaped],
            batch_size=10,
            num_threads=1,
            capacity=10,
        )
        # print(label_batch,image_batch)
        '''
        Tensor("batch:0", shape=(10, 1), dtype=int32) 
        Tensor("batch:1", shape=(10, 32, 32, 3), dtype=uint8)
        '''

        return label_batch,image_batch


    def write_to_tfrecords(self,image_batch,label_batch):
        '''
        将图片的特征值和目标值存进tfrecords
        :param image_batch:10张图片的特征值
        :param label_batch:10张图片的目标值
        :return:
        '''
        # 1、建立TFRecord存储器
        writer = tf.python_io.TFRecordWriter(FLAGS.cifar_tfrecords)

        # 2、循环将所有样本写入文件，每张图片样本都要构造example协议
        # print(image_batch.shape[0])
        for i in range(image_batch.shape[0]):
            # 取出第i个图片数据的特征值和目标值
            image = image_batch[i].eval().tostring()
            label = int(label_batch[i].eval()[0])

            # 构造一个样本的example,就是tfrecord文件的一行数据
            example =  tf.train.Example(features=tf.train.Features(feature={
                "image": tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),
                "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
            }))

            # 写入一个样本到文件（写入前需要先序列化）
            writer.write(example.SerializeToString())

        # 关闭文件
        writer.close()

        return None


    def read_from_tfrecords(self):
        '''
        从已经存在的tfrecords文件中读取样本的特征值和目标值
        :return:
        '''
        # 1、构造文件队列
        file_queue = tf.train.string_input_producer([FLAGS.cifar_tfrecords])

        # 2、构造文件阅读器，读取example内容,value是一个样本序列化后的example
        reader = tf.TFRecordReader()
        key,value = reader.read(file_queue)

        # 3、解析读取的example
        features = tf.parse_single_example(
            value,
            features={
                "image":tf.FixedLenFeature([],tf.string),
                "label":tf.FixedLenFeature([],tf.int64)
            }
        )

        # 4、解码内容, 如果读取的内容格式是string需要解码，如果是int64,float32不需要解码
        image = tf.decode_raw(features["image"],tf.uint8)

        # 固定图片的形状，方便批处理
        image_reshaped = tf.reshape(image, [self.height, self.width, self.channel])
        label = tf.cast(features["label"],tf.int32)
        # print(image_reshaped,label)
        '''
        Tensor("Reshape:0", shape=(32, 32, 3), dtype=uint8) 
        Tensor("Cast:0", shape=(), dtype=int32)
        '''

        # 进行批处理
        image_batch,label_batch = tf.train.batch(
            [image_reshaped,label],
            batch_size=10,
            num_threads=1,
            capacity=10,
        )
        # print(image_batch,label_batch)
        '''
        Tensor("batch:0", shape=(10, 32, 32, 3), dtype=uint8) 
        Tensor("batch:1", shape=(10,), dtype=int32)
        '''

        return image_batch,label_batch


if __name__ == '__main__':
    # 1、找到文件，放入列表   路径+名字  ->列表当中
    file_name = os.listdir(FLAGS.cifar_dir)
    filelist = [os.path.join(FLAGS.cifar_dir, file) for file in file_name if file[-3:] == "bin"]

    cf = CifarRead(filelist)

    # 读取二进制数据
    # label_batch,image_batch = cf.binary_read_decode()

    # 读取tfrecods文件中的数据
    image_batch, label_batch = cf.read_from_tfrecords()

    # 开启会话运行图定义的程序
    with tf.Session() as sess:
        # 定义一个用于控制子线程的线程协调器
        coord = tf.train.Coordinator()

        # 搜索所有的子线程开始运行
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 将标准化后的二进制文件，存进tfrecords文件
        # print("开始存储")
        # cf.write_to_tfrecords(image_batch, label_batch)
        # print("结束存储")

        # 获取二进制文件中的图片特征值和分类标签
        print(sess.run([image_batch, label_batch]))
        '''
        [array([[[[178, 178, 178],
         [178, 179, 179],
         [179, 180, 180],
         ...,
         [177, 176, 176],
         [175, 175, 173],
         [171, 169, 167]],
         
         array([[0],[6],[0],[2],[7],[2],[1],[2],[4],[1]])]
         array([0, 0, 6, 7, 7, 0, 4, 1, 9, 6])
        '''

        # 停止读取文件的子线程，子线程结束，则主线程结束
        coord.request_stop()
        coord.join(threads)