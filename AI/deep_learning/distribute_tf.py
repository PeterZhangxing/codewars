import tensorflow as tf
import os
import sys


os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

class DisTf(object):

    def __init__(self,job_name,task_index):
        self.job_name = job_name
        self.task_index = task_index

    def calculate_task(self):
        x = tf.Variable([[1, 2, 3, 4]])
        w = tf.Variable([[2], [2], [2], [2]])

        res = tf.matmul(x, w)
        return res

    def run_task(self):
        # global_step = tf.contrib.framework.get_or_create_global_step()
        global_step =  tf.train.get_or_create_global_step()

        cluster = tf.train.ClusterSpec(
            {
                "ps":['192.168.31.235:2222'],
                "worker":['192.168.31.178:2222','192.168.31.116:2222']
            }
        )

        # 定义生成的是ps还是worker
        server = tf.train.Server(
            cluster,
            job_name=self.job_name,
            task_index=self.task_index
        )

        if self.job_name == "ps":
            server.join()
        else:
            # 指定在某台设备上运行下面定义的op运算
            worker_device = "/job:worker/task:%d/cpu:0/"%self.task_index
            with tf.device(tf.train.replica_device_setter(
                worker_device=worker_device,
                cluster=cluster,
            )):
                res = self.calculate_task()

            # 定义一个进行运算的clustersession对象
            with tf.train.MonitoredTrainingSession(
                master="grpc://192.168.31.178:2222",
                is_chief=(self.task_index==0),
                hooks=[tf.train.StopAtStepHook(num_steps=20)],
                config=tf.ConfigProto(log_device_placement=True),
            ) as mon_sess:
                while not mon_sess.should_stop():
                    print(mon_sess.run(res))

def get_params():
    job_name = sys.argv[1]
    task_index = sys.argv[2]
    if job_name not in ["ps","worker"] or not task_index.isdigit():
        raise Exception("Invalid input params!")
    return job_name,int(task_index)


if __name__ == '__main__':
    job_name,task_index = get_params()

    distf_obj = DisTf(job_name,task_index)
    distf_obj.run_task()