import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(7.0)

c = tf.add(a,b)

mygraph = tf.get_default_graph()

with tf.Session(graph=mygraph) as sess:
    print(sess.run(c))