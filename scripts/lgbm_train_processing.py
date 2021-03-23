import pandas as pd
import lightgbm as lgb
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pickle
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# 读取数据文件
df = pd.read_excel(r'D:\Documents\A算法组-PY应用和算法服务开发集成\试听直排重构\数据\新增学生意向后的匹配模型数据\新增学生出席意向后的匹配模型数据.xlsx'
                 , header=0
                 , names=['agreement_id', 'arrange_way', 'teacher_id', 'student_id', 'customer_id', 'create_dt', 'label', 'trf_rate'
                          , 'trial_course_total_cnt', 'spr_code1', 'teach_ks', 'current_user_cnt', 'loss_avg_course_hour', 'if_contain'
                          , 'visit_cnt', 'connected_total_cnt', 'diff_dt', 'rn'])

# 数据处理
df = df.fillna(0)
# df['create_dt'] = pd.to_datetime(df['create_dt'], format='%Y/%m/%d')

df = df.drop(df[df['create_dt']==0].index)
# df = df.dropna(subset=['create_dt'])

# 数据按照排课时间划分正负例
df.sort_values(by='create_dt', ascending=True, inplace=True)
df.reset_index(drop=True, inplace=True)

df_feature = df.drop(['agreement_id', 'arrange_way', 'teacher_id', 'student_id', 'customer_id', 'create_dt', 'rn'], axis=1)

# 以指定比例划分样本数据
df_train = df_feature[df_feature.index < df['label'].count()* 0.5]
# df_valid = df[(df['label'].count()* 0.6 <= df.index) & (df.index < df['label'].count()* 0.8)]
df_tst = df_feature[(df_feature.index >= df_feature['label'].count()* 0.5)]

agreement_id = df[['agreement_id', 'arrange_way']]
agreement_id_tst = agreement_id[(agreement_id.index >= agreement_id['agreement_id'].count()* 0.5)]

#  验证按时间分正负例分布是否均匀
print("训练集：%s, %s" % (df_train[df_train['label']==1]['label'].count(), df_train['label'].count()))
# print("验证集：%s, %s" % (df_valid[df_valid['label']==1]['label'].count(), df_valid['label'].count()))
print("测试集：%s, %s" % (df_tst[df_tst['label']==1]['label'].count(), df_tst['label'].count()))

'''
# 构造训练数据和测试数据
X = df_now_sample.drop(columns=['label'], axis=1)  # , 'had_trial_course_cnt', 'bind_cnt'
# X = df[['spr_code1', 'city_id', 'child_grade']]
Y = df_now_sample[['label']]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2, stratify=Y)
train_data = lgb.Dataset(data=x_train, label=y_train)
test_data = lgb.Dataset(data=x_test, label=y_test)
'''


# 构造训练和测试数据
x_train = df_train.drop(columns=['label'], axis=1)
x_test = df_tst.drop(columns=['label'], axis=1)
y_train = df_train[['label']]
y_test = df_tst[['label']]
train_data = lgb.Dataset(data=x_train, label=y_train)
test_data = lgb.Dataset(data=x_test, label=y_test)

# 设置参数和模型训练
param = {
    'max_depth': 6
    , 'max_bin': 255
    , 'num_leaves': 31
    , 'learning_rate': 0.05
    , 'lambda_l1': 0.1
    , 'lambda_l2': 0.1
    , 'objective': 'binary'
    , 'boosting_type': 'gbdt'
    , 'metric': ['auc','binary_logloss']
    , 'categorical_feature': [2, 6]
    , 'is_unbalance': True
    # , 'early_stopping_round': 20
}
model = lgb.train(param, train_data, valid_sets=[test_data])

# 测试数据预测, 测试数据统计
ypred = model.predict(x_test)
y_pred = pd.DataFrame(data=ypred, columns=['predict'])
y_test_df = y_test.reset_index(drop=True)
agreement_id_tst = agreement_id_tst.reset_index(drop=True)
y = pd.concat([y_pred, y_test_df, agreement_id_tst], axis=1)

y = y[y['arrange_way']==1.0]

division = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
for i in range(10):
    print('i: %s' % i)
    if y[(y['predict']>=division[i]) & (y['predict'] <division[i+1])]['label'].count() != 0:
            print(y[(y['predict']>=division[i]) & (y['predict']<division[i+1])]['label'].count())
            print(y[(y['predict']>=division[i]) & (y['predict']<division[i+1]) & (y['label']==1)]['label'].count())
            print(y[(y['predict']>=division[i]) & (y['predict']<division[i+1]) & (y['label']==1)]['label'].count() 
                  / y[(y['predict']>=division[i]) & (y['predict']<division[i+1])]['label'].count())
    else:   
            print(0)

# 特征重要性
importance_list = model.feature_importance()  # importance_type='gain'
feature_list = model.feature_name()
feature_dict = {feature_list[i]: importance_list[i] for i in range(len(feature_list))}
result = sorted(feature_dict.items(), key=lambda x: x[1], reverse=True)
print(result)

# auc
fpr, tpr, thresholds = metrics.roc_curve(y_test, ypred)  # thresholds阈值
print(metrics.auc(fpr, tpr))

# 绘制ROC曲线
import matplotlib.pyplot as plt
plt.plot(fpr,tpr)
plt.show()

# 最佳阈值
i = np.arange(len(tpr)) 
roc = pd.DataFrame({'tf' : pd.Series(tpr-(1-fpr), index=i), 'threshold' : pd.Series(thresholds, index=i)})
roc_t = roc.iloc[(roc.tf-0).abs().argsort()[:1]]
print(list(roc_t['threshold']))

# 保存模型
pickle.dump(model, open('model_20210303.pkl', 'wb'))

# 读取模型
model = pickle.load(open('model_20210303.pkl', 'rb'))




