# actionSeriesPrediction中的加载方式要求linux系统的cpu支持avx指令，这个脚本加载模型的方法，可以用来加载那个脚本中的模型
# 这种加载方式少加载了yaml文集，只用了h5文件

from keras.layers import LSTM
from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential

model = Sequential()
model.add(LSTM(input_shape=(30, 11), units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))
model.add(Activation("sigmoid"))
h5_path = 'model_plus.h5'
model.load_weights(h5_path)
print("Loaded model from disk")

