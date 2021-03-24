# -*- coding:utf-8 -*-
"""
#  Name     :  actionSeriesPrediction.py
#  Author   :  spy
#  Desc     :
#  Create   :  2020-06-30
#  Version  :  1.0
#  Command  :
#  Modify   :
#  Note     :
#  Emoji    : ⊙▂⊙ ⊙０⊙ ⊙︿⊙ ⊙ω⊙ ⊙﹏⊙ ⊙△⊙ ⊙▽⊙
"""
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense, Activation, Dropout
from keras.models import load_model
from keras.models import model_from_yaml
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('../../docs/data.txt')
print(df.head(10))
Y = df['y']
X = np.array(df.drop(columns=['y'], axis=1))

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=2)


def model_test_and_save(x_train, x_test, y_train, y_test):
    # 将输入数据从二维转化为LSTM所能接受的三维，其中x_train的shape被重塑为(7, 10, 1)，7为样本数，10为10个时间步，1为1个特征
    x_train = np.reshape(x_train, (x_train.shape[0], 10, 2))

    x_test = np.reshape(x_test, (x_test.shape[0], 10, 2))

    model = Sequential()  #

    # model.add(LSTM(input_shape=(x_train.shape[1], 1), units=50))
    model.add(LSTM(input_shape=(x_train.shape[1], 2), units=50))  # units输出空间的维度 input_shape dim=x_train.shape[1]
    model.add(Dropout(0.2))  # Dropout 训练中每次更新时，将输入单元按比率随机设为0 防止过拟合

    model.add(Dense(units=1))  # units 输出空间维度
    model.add(Activation("sigmoid"))  # 应用于输出的激活函数 ？

    model.compile(loss="binary_crossentropy", optimizer="adam",
                  metrics=['accuracy'])  # compile 方法用于配置训练模型 loss 定义损失函数名 optimizer 定义优化器对象 metrics
    # 分类问题一般看accuracy准确性，但accuracy本身是不可导的方程，所以使用交叉熵binary_crossentropy作为损失函数来优化，实际关心的还是accuracy
    model.fit(x_train, y_train, batch_size=10, epochs=10, validation_split=0.5)
    # fit 方法以固定数量的轮次训练模型 batch_size 每次梯度更新的样本数
    # epochs 训练模型迭代轮次 validation_split 用作验证集的训练数据的比例

    # 输出测试集的loss
    # loss = model.evaluate(x_test, y_test)
    # print(loss)  # loss[0] loss loss[1] Accuracy

    # 输出测试集每个个体的预测值 Accuracy
    # individualPredictionResult = model.predict(x_test)
    # print(individualPredictionResult)
    model_yaml = model.to_yaml()
    with open("../../docs/model.yaml", "w") as yaml_file:
        yaml_file.write(model_yaml)
    model.save_weights("../../docs/model.h5")
    # model.save("../../docs/model.h5")
    print("Saved model to disk")
    # model1 = load_model('lstm_model.h5')
    return model
    # print(type(model1))


def model_load_and_used(x_test, y_test):
    # load YAML and create model
    yaml_file = open('../../docs/model.yaml', 'r')
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    loaded_model = model_from_yaml(loaded_model_yaml)
    # load weights into new model
    loaded_model.load_weights("../../docs/model.h5")
    print("Loaded model from disk")

    # evaluate loaded model on test data
    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    score = loaded_model.evaluate(x_test, y_test)
    print(score)


def main():
    # model_test_and_save(x_train, x_test, y_train, y_test)
    model_load_and_used(x_test, y_test)


main()
