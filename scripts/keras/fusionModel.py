
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.layers import Input, Dense, Conv1D, GRU, Dropout
from keras.layers import concatenate, Lambda
from keras.models import Model
from keras.optimizers import Adam
import keras.backend as K
from keras.utils import plot_model
# from tensorflow.python.client import device_lib  # 检查
# print(device_lib.list_local_devices())


# 输入数据格式为每行代表一条样本，最后一列代表标签，同时时序数据同一时间节点放置在相邻位置，非时序数据统一放在时序数据的右侧
# day1_feature1, day1_feature2, day2_feature1, day2_feature2, ..., not_time_f1, not_time_f2，label
time_step = 10  # 时间步长，用10天的数据来预测则该值为10
multi_time_feature_dim = 1  # 时序特征的维度
not_time_feature_dim = 2  # 非时序特征的维度
hidR = 100  # RNN层输出维度
hidC = 100  # CNN层输出维度
hidS = 50  # Skip-RNN层输出维度
Ck = 5  # CNN层kernel大小
skip = 0  # Skip-RNN周期长度
dropout = 0.2
lr = 1e-4
batch_size = 4
epochs = 10
validation_split = 0.5
time_feature_length = multi_time_feature_dim * time_step

df = pd.read_csv('../../docs/dd.txt')
Y = df['y']
X = np.array(df.drop(columns=['y'], axis=1))
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)
input_1 = x_train[:, :time_feature_length]
input_1 = np.reshape(input_1, (input_1.shape[0], time_step, multi_time_feature_dim))
input_2 = x_train[:, time_feature_length:]
test_1 = x_test[:, :time_feature_length]
test_1 = np.reshape(test_1, (test_1.shape[0], time_step, multi_time_feature_dim))
test_2 = x_test[:, time_feature_length:]


class LSTNet(object):
    def __init__(self):
        super(LSTNet, self).__init__()
        self.time_step = time_step
        self.multi_time_feature_dim = multi_time_feature_dim
        self.hidR = hidR
        self.hidC = hidC
        self.hidS = hidS
        self.Ck = Ck
        self.skip = skip
        # self.pt = int((self.time_step-self.Ck+1)/self.skip) if (self.time_step-self.Ck+1)/self.skip > 1 else 1
        self.dropout = dropout
        self.lr = lr

    def make_model(self):

        input_1 = Input(shape=(self.time_step, self.multi_time_feature_dim,), name='input_1')
        # CNN
        c = Conv1D(self.hidC, self.Ck, activation='relu')(input_1)
        c = Dropout(self.dropout)(c)
        # RNN

        r = GRU(self.hidR)(c)
        r = Lambda(lambda k: K.reshape(k, (-1, self.hidR)))(r)
        r = Dropout(self.dropout)(r)

        # skip-RNN
        if self.skip > 0:
            # c: batch_size*steps*filters, steps=P-Ck
            s = Lambda(lambda k: k[:, int(-self.pt * self.skip-1):, :])(c)
            s = Lambda(lambda k: K.reshape(k, (-1, self.pt, self.skip, self.hidC)))(s)
            s = Lambda(lambda k: K.permute_dimensions(k, (0, 2, 1, 3)))(s)
            # 输入skip-rnn的时间步长为self.pt
            s = Lambda(lambda k: K.reshape(k, (-1, self.pt, self.hidC)))(s)

            s = GRU(self.hidS)(s)
            s = Lambda(lambda k: K.reshape(k, (-1, self.skip * self.hidS)))(s)
            s = Dropout(self.dropout)(s)
            r = concatenate([r, s])

        res = Dense(multi_time_feature_dim, activation='sigmoid')(r)
        input_2 = Input(shape=(not_time_feature_dim,), name='input_2')
        x2 = Dense(not_time_feature_dim, activation='sigmoid')(input_2)
        feature_concat = concatenate([res, x2])
        feature_concat = Dense(50, activation='relu')(feature_concat)
        final = Dense(1, activation='sigmoid')(feature_concat)
        model = Model(inputs=[input_1, input_2], outputs=final)
        plot_model(model, 'time_series_model.png')
        model.compile(optimizer=Adam(lr=self.lr), loss="binary_crossentropy")
        model.summary()
        return model


model = LSTNet().make_model()

model.fit(
    x=[input_1, input_2],
    y=y_train,
    batch_size=batch_size,
    epochs=epochs,
    validation_split=validation_split
)

print(model.evaluate([test_1, test_2], y_test))
