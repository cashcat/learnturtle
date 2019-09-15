import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

train_X = np.linspace(-1,1,100)
noiseData = np.random.randn(*train_X.shape)
train_Y = 2*train_X + noiseData*0.3
print(noiseData)
print(train_X.shape)

plt.plot(train_X,train_Y,'ro',label='Original data')
plt.legend()
plt.show()