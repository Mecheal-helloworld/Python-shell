import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
 
## parameters
learning_rate = 0.8
training_epochs = 2000
display_step = 50
 
## create data
train_X = np.random.rand(100).astype(np.float32)
train_X.sort()
train_Y = (train_X-0.5)**2 + 0.3
n_samples = train_X.shape[0]
 
X = tf.placeholder("float")
Y = tf.placeholder("float")
 
w = tf.Variable(np.random.randn(), name='weight')
b = tf.Variable(np.random.randn(), name='bias')
 
pred = tf.add(tf.multiply((X-0.5)**2,w), b)
 
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
 
init = tf.global_variables_initializer()
 
 
with tf.Session() as sess:
    sess.run(init)
    plt.figure(num=3)
    
    for epoch in range(training_epochs):
        
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X:x, Y:y})
        if (epoch+1) % display_step == 0:
#             plt.figure(num=3)
            plt.ion()
            plt.cla()
            c = sess.run(cost, feed_dict={X:train_X, Y:train_Y})
            print("Epoch:", '%04d'%(epoch+1), "cost=", "{:.9f}".format(c),\
                 "W=", sess.run(w), 'b=', sess.run(b))
            ### draw the picture
            plt.plot(train_X, train_Y, 'ro', label='Orginal data')
            plt.plot(train_X, sess.run(w)*(train_X-0.5)**2+sess.run(b), label='Fitted line')
            plt.legend()
            
            plt.pause(0.05)
 
    plt.ioff()
#     plt.show()