# -*- coding: utf-8 -*-
import sugartensor as tf

# set log level to debug
tf.sg_verbosity(10)

# MNIST input tensor ( with QueueRunner )
data = tf.sg_data.Mnist()

# inputs
x = data.train.image.sg_squeeze()
y = data.train.label

# create training graph
logit = (x.sg_rnn(dim=200, act='relu', ln=True, last_only=True).sg_dense(dim=10))

# cross entropy loss with logit ( for training set )
loss = logit.sg_ce(target=y)

# accuracy evaluation ( for validation set )
acc = (logit.sg_reuse(input=data.valid.image).sg_softmax()
       .sg_accuracy(target=data.valid.label, name='val'))

# train
tf.sg_train(loss=loss, eval_metric=[acc], ep_size=data.train.num_batch, log_interval=10)

