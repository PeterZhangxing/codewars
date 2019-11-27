import tensorflow as tf

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("job_name","worker","启动服务的类型ps/worker")
tf.app.flags.DEFINE_integer("task_index",0,"指定ps或worker当中的哪一台服务器是task:0,哪个是task:1")


def main(argv):
    '''
    tf.app.run()会自动调用此函数
    :param argv:
    :return:
    '''
    # 定义全局计数的op，给钩子列表当中的训练步数使用，记录训练到第几步
    global_step = tf.contrib.framework.get_or_create_global_step()

    # 定义集群对象，定义一个集群包括哪些机器
    cluster = tf.train.ClusterSpec(
        {"ps":["10.1.1.128:2222"],
         "worker":["10.1.1.1:2222"]}
    )

    # 根据参数创建不同的服务
    server = tf.train.Server(
        cluster,
        job_name=FLAGS.job_name,
        task_index=FLAGS.task_index
    )

    # 让不同服务做不同的事情
    # ps:去更新保存参数，worker:指定设备去运行模型计算
    if FLAGS.job_name == "ps":
        # 参数服务器什么都不用干，是需要等待worker传递参数
        server.join()
    else:
        # 指定设备为worker
        worker_device = "/job:worker/task:%d/cpu:0/"%FLAGS.task_index
        with tf.device(tf.train.replica_device_setter(
            worker_device=worker_device,
            cluster=cluster
        )):
            # 做一个矩阵乘法运算
            x = tf.Variable([[1, 2, 3, 4]])
            w = tf.Variable([[2], [2], [2], [2]])
            mat = tf.matmul(x, w)

        # 创建分布式会话，运行计算
        with tf.train.MonitoredTrainingSession(
            master="grpc://10.1.1.1:2222",# 指定主worker
            is_chief=(FLAGS.task_index == 0),# 判断是否是主worker
            config=tf.ConfigProto(log_device_placement=True),# 打印设备信息
            hooks=[tf.train.StopAtStepHook(last_step=100)],# 指定计算的步数
        ) as mon_sess:
            while not mon_sess.should_stop():
                print(mon_sess.run(mat))


if __name__ == '__main__':
    tf.app.run()
    '''
    运行脚本：
        在ps服务器上：python3.5 dist_tensor.py --job_name="ps" --task_index=0
        在worker上：python dist_tensor.py --job_name="worker" --task_index=0
    '''