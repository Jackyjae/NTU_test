import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
from sklearn.metrics import r2_score

train_x = np.zeros((1, 3),dtype=np.float64)
train_y = np.zeros((1, 1),dtype=np.float64)
test_x = np.zeros((1, 3),dtype=np.float64)
val_x = np.zeros((1000, 3),dtype=np.float64)
val_y = np.zeros((1000, 3),dtype=np.float64)

# read train data, 1k for validation
trainData = open('train_data.txt') 
lines = trainData.readlines()[1:]

for i,j in enumerate(lines): 
	train_x_temp = np.zeros((1, 3),dtype=np.float64)
	train_x_temp = np.float64(j.split()[0]),np.float64(j.split()[1]),np.float64(j.split()[2])
	train_x = np.vstack((train_x, train_x_temp))
trainData.close()
val_x = train_x[1:1001]
train_x = train_x[1001:]

# read train truth, 1k for validation
trainTruth = open('train_truth.txt') 
lines = trainTruth.readlines()[1:]
for i,j in enumerate(lines): 
	train_y_temp = np.zeros((1, 1),dtype=np.float64)
	train_y_temp = np.float64(j)
	train_y = np.vstack((train_y, train_y_temp))
trainTruth.close()
val_y = train_y[1:1001]
train_y = train_y[1001:]

# read test data
testData = open('test_data.txt') 
lines = testData.readlines()[1:]
for i,j in enumerate(lines): 
	test_x_temp = np.zeros((1, 3),dtype=np.float64)
	test_x_temp = np.float64(j.split()[0]),np.float64(j.split()[1]),np.float64(j.split()[2])
	test_x = np.vstack((test_x, test_x_temp))
testData.close()
test_x = test_x[1:]

# I followed the keras tutorial to build the model
model = tf.keras.Sequential([
        tf.keras.layers.Dense(4, input_shape=(3,),activation='relu',dtype=np.float64),
        tf.keras.layers.Dense(4, activation='relu',dtype=np.float64),
        tf.keras.layers.Dense(1,dtype=np.float64)])

model.summary()

# optimizer and loss fuction
model.compile(optimizer='adam',  
              loss='mse')

history = model.fit(train_x, train_y , epochs=50)

# R square, R2=0.996286367784999
# R2 = r2_score(val_y, model.predict(val_x), multioutput='variance_weighted')
# print(R2)

# import matplotlib. pyplot as plt
# history.history.keys()
# plt.plot(history.epoch, history.history.get('loss'))
# plt.show()

# predict test data
result = model.predict(test_x)
print('y')
for i in range(result.shape[0]):
	print(result[i][0])

# f = open('test predicted.txt','w')
# f.write('y\n')
# for i in range(result.shape[0]):
# 	sstring = ''
# 	sstring = str(result[i][0])
# 	f.write(sstring)
# 	f.write('\n')
# f.close()