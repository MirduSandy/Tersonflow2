# 导入TensorFlow，查看版本
import tensorflow as tf
print(tf.__version__)

# 查看当前主机上的运算设备
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
cpus = tf.config.experimental.list_physical_devices(device_type='CPU')
print("GPU:", gpus)
print("CPU:", cpus)

# 指定在CPU上执行
with tf.device('/cpu:0'):
    cpu_a = tf.random.normal([10000, 1000])
    cpu_b = tf.random.normal([1000, 2000])
    cpu_c = tf.matmul(cpu_a, cpu_b)
print("cpu_a", cpu_a.device)
print("cpu_b", cpu_b.device)
print("cpu_c", cpu_c.device)

# 指定在GPU上执行
# 查看GPU是否可以用
print(tf.test.is_gpu_available())

# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())
# 第二条警告：如果你没有安装GPU版本的tensorflow,也会输出false。你可以使用tf.test.is.built_with_cuda()来验证是否与CUDA建立联系。
print(tf.test.is_built_with_cuda())
