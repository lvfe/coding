import tensorflow as tf

def myregression():
    """
    liner regression
    :return: None
    :return:
    """
    with tf.variable_scope("data"):
        x = tf.random.normal([100,1],mean=1.75,stddev=0.5,name="x_data")
        y_true = tf.matmul(x,[[0.7]]) + 0.8
    with tf.variable_scope("model"):
        weight = tf.Variable(tf.random.normal([1,1],mean=0.0,stddev=1.0),name="weight")
        bias = tf.Variable(0.0,name="b")
        y_predict = tf.matmul(x,weight)+bias

    loss = tf.reduce_mean(tf.square(y_true - y_predict))
    train_op = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(loss)
    # collect tensor
    tf.summary.scalar("losses",loss)
    tf.summary.histogram("weights",weight)
    merged = tf.summary.merge_all()
    init_op = tf.compat.v1.global_variables_initializer()

    with tf.compat.v1.Session() as sess:
        sess.run(init_op)
        print("fist:weight %f,bias %f" % (weight.eval(),bias.eval()))
        filewriter = tf.summary.FileWriter("./tmp/summary/test/", graph=sess.graph)
        for i in range(100):
            sess.run(train_op)
            summary = sess.run(merged)
            filewriter.add_summary(summary,i)

            print("the %d:weight %f, bias %f" % (i,weight.eval(),bias.eval()))
    return None

if __name__ == "__main__":
    myregression()