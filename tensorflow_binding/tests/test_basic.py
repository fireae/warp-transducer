import numpy as np
import tensorflow as tf
from warprnnt_tensorflow import rnnt_loss

acts = tf.placeholder(tf.float32, [None, None, None, None])
labels = tf.placeholder(tf.int32, [None, None])
input_length = tf.placeholder(tf.int32, [None])
label_length = tf.placeholder(tf.int32, [None])

B = 2; T = 4; U = 3; V = 6; blank = 5

acts = tf.nn.log_softmax(acts)
costs = rnnt_loss(acts, labels, input_length, label_length, blank)
grad = tf.gradients(costs, [acts])

a = np.array([[[[0.06535690384862791, 0.7875301411923206, 0.08159176605666074],
            [0.5297155426466327, 0.7506749639230854, 0.7541348379087998],
            [0.6097641124736383, 0.8681404965673826, 0.6225318186056529]],

            [[0.6685222872103057, 0.8580392805336061, 0.16453892311765583],
            [0.989779515236694, 0.944298460961015, 0.6031678586829663],
            [0.9467833543605416, 0.666202507295747, 0.28688179752461884]],

            [[0.09418426230195986, 0.3666735970751962, 0.736168049462793],
            [0.1666804425271342, 0.7141542198635192, 0.3993997272216727],
            [0.5359823524146038, 0.29182076440286386, 0.6126422611507932]],

            [[0.3242405528768486, 0.8007644367291621, 0.5241057606558068],
            [0.779194617063042, 0.18331417220174862, 0.113745182072432],
            [0.24022162381327106, 0.3394695622533106, 0.1341595066017014]]],

        [[[0.5055615569388828, 0.051597282072282646, 0.6402903936686337],
            [0.43073311517251, 0.8294731834714112, 0.1774668847323424],
            [0.3207001991262245, 0.04288308912457006, 0.30280282975568984]],

            [[0.6751777088333762, 0.569537369330242, 0.5584738347504452],
            [0.08313242153985256, 0.06016544344162322, 0.10795752845152584],
            [0.7486153608562472, 0.943918041459349, 0.4863558118797222]],

            [[0.4181986264486809, 0.6524078485043804, 0.024242983423721887],
            [0.13458171554507403, 0.3663418070512402, 0.2958297395361563],
            [0.9236695822497084, 0.6899291482654177, 0.7418981733448822]],

            [[0.25000547599982104, 0.6034295486281007, 0.9872887878887768],
            [0.5926057265215715, 0.8846724004467684, 0.5434495396894328],
            [0.6607698886038497, 0.3771277082495921, 0.3580209022231813]]]], dtype=np.float32)

b = np.array([[1, 2], [1, 1]], dtype=np.int32)
c = np.array([4, 4], dtype=np.int32)
d = np.array([2, 2], dtype=np.int32)

feed = {acts: a, labels: b, input_length: c, label_length: d}
with tf.Session() as sess:
    cost, grads = sess.run([costs, grad], feed_dict=feed)
    print(cost)
    print(grads)