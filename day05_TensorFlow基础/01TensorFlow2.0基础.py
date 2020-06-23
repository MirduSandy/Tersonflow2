import tensorflow as tf
a = tf.constant(2, name="input_a")
b = tf.constant(3, name="input_b")
c = tf.add(a, b, name="add_c")
# sess = tf.Session()  # AttributeError: module 'tensorflow' has no attribute 'Session'
# print(sess.run(c))
# sess.close()
print(a+b)