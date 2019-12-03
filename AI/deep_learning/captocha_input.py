import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string("tfrecords_dir","./tfrecords/captcha.tfrecords","验证码tfrecords文件")
tf.app.flags.DEFINE_string("captcha_dir","../data/Genpics/","验证码图片路径")
tf.app.flags.DEFINE_string("letter","ABCDEFGHIJKLMNOPQRSTUVWXYZ","验证码字符的种类")


def deal_lab(label_str):
    '''
    将字母转换为数字
    :param label_str:
    :return:
    '''
    # 构建字母和数字的对应字典，形如{'A':0, 'B':1...}
    num_letter = dict(enumerate(list(FLAGS.letter)))
    letter_num = dict(zip(num_letter.values(),num_letter.keys()))

    # 将大写字母组成的标签，根据上面创建的字典，转换为数字列表
    # 对标签数据进行处理[[b"NZPP"]...]
    num_li = []
    for i in label_str:
        lettet_li = []
        for letter in i[0].decode('utf-8'):
            lettet_li.append(letter_num[letter])
        num_li.append(lettet_li)

    print(num_li)
    '''
    [[13, 25, 15, 15], 
    [22, 10, 7, 10], 
    [22, 15, 18, 9], 
    [16, 6, 13, 10], 
    [1, 0, 8, 17], 
    [0, 9, 24, 14]...]
    '''

    # 将构建的列表，转换为tensor类型
    return tf.constant(num_li)


def get_captcha_img():
    '''
    读取验证码图片文件，转换为特征值数据
    :return:
    '''
    # 构建文所有图片的文件名,
    # 因为用os.listdir()文件会乱序，所以要自己构建文件名称
    f_name_li = []
    for i in range(len(os.listdir(FLAGS.captcha_dir))):
        string = str(i) + ".jpg"
        f_name_li.append(string)
    file_list = [os.path.join(FLAGS.captcha_dir, file) for file in f_name_li]

    # 构造文件队列
    file_queue = tf.train.string_input_producer(file_list, shuffle=False)

    # 构造阅读器
    reader = tf.WholeFileReader()

    # 读取第一张图片的内容
    key,value = reader.read(file_queue)

    # 解码图片数据
    image = tf.image.decode_jpeg(value)

    # 改变图片数据形状
    image.set_shape([20,80,3])

    # 批处理图片数据[6000, 20, 80, 3]
    image_batch = tf.train.batch([image], batch_size=6000, num_threads=1, capacity=6000)

    return image_batch


def get_captcha_lab():
    '''
    读取保存有图片标签的文件
    :return:
    '''
    file_queue = tf.train.string_input_producer(["../data/Genpics/labels.csv"],shuffle=False)
    reader = tf.TextLineReader()
    key,value = reader.read(file_queue)
    records = [[1],["None"]]
    num,label = tf.decode_csv(
        value,
        record_defaults=records
    )
    lab_batch = tf.train.batch(
        [label],
        batch_size=6000,
        num_threads=1,
        capacity=6000,
    )

    return lab_batch


def build_tf(img_bat,lab_bat):
    '''
    将图片内容和标签写入到tfrecords文件当中
    :param img_bat:特征值
    :param lab_bat:标签值
    :return:
    '''
    # 转换标签数据类型
    lab_bat = tf.cast(lab_bat,tf.uint8)

    # 建立TFRecords 存储器
    writter = tf.python_io.TFRecordWriter(FLAGS.tfrecords_dir)

    # 循环将每一个图片上的数据构造example协议块，序列化后写入
    for i in range(len(os.listdir(FLAGS.captcha_dir))):
        # 取出第i个图片数据，转换相应类型,图片的特征值要转换成字符串形式
        img_str = img_bat[i].eval().tostring()
        lab_str = lab_bat[i].eval().tostring()

        # 构造协议块
        example = tf.train.Example(
            features=tf.train.Feature(feature={
                "image": tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_str])),
                "label": tf.train.Feature(bytes_list=tf.train.BytesList(value=[lab_str]))
            })
        )

    writter.close()
    return None


if __name__ == '__main__':
    # 获取验证码文件当中的图片
    img_batch = get_captcha_img()

    # 获取验证码文件当中的标签数据
    label = get_captcha_lab()

    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        # [b'NZPP' b'WKHK' b'WPSJ' ..., b'FVQJ' b'BQYA' b'BCHR']
        label_str = sess.run(label)

        # 将字符串标签转换为数字张量
        lab_batch = deal_lab(label_str)

        # 将图片特征数据和内容，写入到tfrecords文件中
        build_tf(img_batch, lab_batch)

        coord.request_stop()
        coord.join(threads)