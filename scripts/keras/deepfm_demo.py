import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler,Normalizer,StandardScaler
from deepctr.models import DeepFM
from deepctr.feature_column import SparseFeat, DenseFeat, get_feature_names
from keras.optimizers import Adam



## 1.
train = pd.read_csv('train_0218_dfm.csv')

target = ['tag']
sparse_features = ['C' + str(i) for i in range(1, 4)]
dense_features = ['I'+str(i) for i in range(1, 14)]

# 对类别型特征做label编码
for feat in sparse_features:
    lbe = LabelEncoder()
    train[feat] = lbe.fit_transform(train[feat])

#对数值型特征归一化
mms = Normalizer()
train[dense_features] = mms.fit_transform(train[dense_features])

# print(train[sparse_features].nunique())
# print(data[sparse_features])
# sparse_feature_columns = [SparseFeat(feat, vocabulary_size=train[feat].nunique()+50, embedding_dim=4)
#                           for i, feat in enumerate(sparse_features)]

sparse_feature_columns = [SparseFeat(feat, vocabulary_size=1000,embedding_dim=5, use_hash=True)
                          for feat in sparse_features]


dense_feature_columns = [DenseFeat(feat, 1)
                         for feat in dense_features]

dnn_feature_columns = sparse_feature_columns + dense_feature_columns
linear_feature_columns = sparse_feature_columns + dense_feature_columns
feature_names = get_feature_names(linear_feature_columns + dnn_feature_columns)


train_model_input = {name:train[name].values for name in feature_names}
# 模型类别初始化
model = DeepFM(linear_feature_columns,dnn_feature_columns,task='binary')
# 调用compile，配置模型的优化器，损失函数，评估函数
model.compile(optimizer  = Adam(lr = 0.0001),
              loss  = "binary_crossentropy",
              metrics=["AUC","acc"] )

# 模型训练
model.fit(train_model_input, train[target].values,
                    batch_size=512, epochs=200, verbose=2, validation_split=0.2 )
# 模型保存
from tensorflow.python.keras.models import  save_model,load_model
save_model(model, '0301.h5')

