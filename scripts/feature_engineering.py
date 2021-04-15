import pandas as pd
import lightgbm as lgb
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pickle
import numpy as np
import copy 

import warnings
warnings.filterwarnings("ignore")

# 读取数据

df = pd.read_excel(r'D:\Documents\A算法组-PY应用和算法服务开发集成\试听直排重构\数据\0402扩展学生侧特征\0408全部样本扩展学生侧特征.xlsx'
                   , header=0
                   , names=[''])

# 数据复制
df_origin = copy.deepcopy(df)

# 输出各列缺失值
shp = df_origin.shape  # tuple
null_statistic = df_origin.isnull().sum()  # Series
print(shp)
print(null_statistic)

# 提取其中的特征列名、标签列名、唯一标志列名
columns = list(df_origin.columns)
only_col = columns[: 1]  # 唯一列名
lbl_feat = columns[6: -1]  # 标签列名、特征列名
only_col.extend(lbl_feat) 

# 特征处理 - 缺失值处理  怎么判断一列是数值还是属性；
# 属性列：null大于40%的删除，反之，类别值用0填充
# 确认属性列能否用0替换：0本身在这个类别中没有含义
attribute_col = ['']  # 指定属性列名
for col in attribute_col:
    if df_origin[col].isnull().sum() / df_origin[col].isnull().count() > 0.4:
        # df_origin.drop(col, axis=1, inplace=True)  
        only_col.remove(col)
    else:  
        df_origin[col].fillna(0, inplace=True)
        
# 数值列: 数值型处理方式不统一，如trf_tate可以按常规方式处理，高考距今月数就不能
# numerical_col = ['']  # 指定数值列名
# 个性化处理
process_df = df_origin['create_dt'].map(lambda x: x.month)
df_origin.loc[df_origin['gk_mon_diff']<0, 'gk_mon_diff'] = (12 - df_origin['reg_grade'])*12 - process_df + 6
df_origin.loc[df_origin['gk_mon_diff']<0, 'gk_mon_diff'] = df_origin['gk_mon_diff'] + 12
df_origin.loc[df_origin['diff_dt'].isnull(), 'diff_dt'] = df_origin['diff_dt'].median()
df_origin.fillna(0, inplace=True)

# 特征处理 - 离群值处理
alone_col = ['']  # 指定需要处理的列名, 通常是数值型的列; 或者所有列  only_col
# 根据箱线图的上下限进行异常值的填充
def boxplot_fill(col):
    # 计算iqr：数据四分之三分位值与四分之一分位值的差
    iqr = col.quantile(0.75)-col.quantile(0.25)
    # 根据iqr计算异常值判断阈值
    u_th = col.quantile(0.75) + 1.5*iqr # 上界
    l_th = col.quantile(0.25) - 1.5*iqr # 下界
    # 定义转换函数：如果数字大于上界则用上界值填充，小于下界则用下界值填充。
    def box_trans(x):
        if x > u_th:
            return u_th
        elif x < l_th:
            return l_th
        else:
            return x
    return col.map(box_trans)
for col in alone_col:
    # 确定该列的上下界
    df_origin[col] = boxplot_fill(df_origin[col])

# 特征处理 - 标准化(省略，lgbm暂时不需要)

# 特征处理 - 纠偏
rectify = ['']  # 需要转化为正态分布的列, 通常为数值列
pt = preprocessing.PowerTransformer(method='yeo-johnson', standardize=True, copy=False)  # standardize 将转化后的数据标准化 
dt_fit = df_origin[rectify]
pt.fit(dt_fit)
pt.transform(dt_fit)
dt_fit = pd.DataFrame(dt_fit, columns=rectify)
df_origin[rectify] = dt_fit

# 特征处理 - 线性相关性(省略，这一步的目的是防止多重共线性，这种现象不会影响决策树)
# 多重共线性如何在线性回归中成为问题: https://blog.csdn.net/weixin_26750481/article/details/108499848
# 相关性计算方法有：Pearson Kendall Spearman, 其中 Kendall Spearman 都可用于计算类别特征相关性，具体使用条件待查

# 特征筛选：根据特征重要性排序，循环删除重要性最低的特征，保证特征删除后，auc的值下降不超过0.02 
auc_lst = []
feature_importance = []
auc_diff = 0
drop_feature = ''
pre_model = None
param = {
    'max_depth': 6
    , 'max_bin': 255
    , 'num_leaves': 31  # 待调整
    , 'learning_rate': 0.01
    , 'lambda_l1': 0.1
    , 'lambda_l2': 0.1
    , 'objective': 'binary'
    , 'boosting_type': 'gbdt'
    , 'metric': ['auc','binary_logloss']
#     , 'categorical_feature': [3, 4, 5, 7, 8]
    , 'is_unbalance': True
#     , 'early_stopping_round': 20
}
while auc_diff < 0.02:
    # 特征筛选1：特征扩展
    feature_cols = only_col[3: ]
    if drop_feature in feature_cols or drop_feature == '':
        if drop_feature <> '':
            feature_cols.remove(drop_feature) # 删除特征重要性最低的特征名
            pre_model = model
        polynomy = preprocessing.PolynomialFeatures(degree=2)
        df_new = polynomy.fit_transform(df_origin[feature_cols])
        df_new = pd.DataFrame(df_new)
        df_new['agreement_id'] = df_origin['agreement_id']
        df_new['label'] = df_origin['label']
    else:
        df_new.drop(drop_feature, axis=1, inplace=True)
    # 特征筛选2：数据集划分,  并输出训练集和测试集的正负例数和占比
    # 样本按时间排序(取数时已排序)，7:3划分训练集和测试集
    df_train = df_new[df_new.index < df_new['label'].count()* 0.7]
    df_tst = df_feature[df_feature.index >= df_feature['label'].count()* 0.7]
    # 以指定比例划分标志，区分测试数据中的样本排课方式 
    agreement_id = df_origin[['agreement_id', 'arrange_way']]
    agreement_id_tst = agreement_id[(agreement_id.index >= agreement_id['agreement_id'].count()* 0.7)]
    #  验证按时间分正负例分布是否均匀 
    print("训练集：%s, %s" % (df_train[df_train['label']==1]['label'].count(), df_train['label'].count()))
    print("测试集：%s, %s" % (df_tst[df_tst['label']==1]['label'].count(), df_tst['label'].count()))
    print('训练集正例占比：%s, 测试集正例占比：%s'%(df_train[df_train['label']==1]['label'].count() / df_train['label'].count()
          , df_tst[df_tst['label']==1]['label'].count() / df_tst['label'].count()))
    # 特征筛选3：构造特征数据
    x_train = df_train.drop(columns=['label'], axis=1)
    x_test = df_tst.drop(columns=['label'], axis=1)
    y_train = df_train[['label']]
    y_test = df_tst[['label']]
    train_data = lgb.Dataset(data=x_train, label=y_train)
    test_data = lgb.Dataset(data=x_test, label=y_test)
    # 特征筛选4：设置参数并训练模型
    model = lgb.train(param, train_data, valid_sets=[test_data])
    # 特征筛选5：记录排序后的特征重要性，并取出重要性最低的特征
    importance_list = model.feature_importance()  # importance_type='gain'
    feature_list = model.feature_name()
    feature_dict = {feature_list[i]: importance_list[i] for i in range(len(feature_list))}
    result = sorted(feature_dict.items(), key=lambda x: x[1], reverse=True)
    feature_importance.append(result)
    drop_feature = result[-1][0]
    # 特征筛选6：记录auc
    fpr, tpr, thresholds = metrics.roc_curve(y_test, ypred)
    cur_auc = metrics.auc(fpr, tpr)
    auc_lst.extend(cur_auc)
    if len(auc_lst) >= 2:
        auc_diff = auc_lst[-1] - auc_lst[-2]
model = pre_model
# 效果统计：根据最后确定的特征训练出的模型，统计在测试数据上的效果，并输出 auc
ypred = model.predict(x_test)
y_pred = pd.DataFrame(data=ypred, columns=['predict'])
y_test_df = y_test.reset_index(drop=True)
agreement_id_tst = agreement_id_tst.reset_index(drop=True)
y = pd.concat([y_pred, y_test_df, agreement_id_tst], axis=1)
y = y[y['arrange_way']==1.0]  # 只取测试数据中的直排样本
# division = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  
# 调整为上下界为预测分值的最大值和最小值，并分为10等分
division = []
max_pre = y['predict'].max()
min_pre = y['predict'].min()
diff = max_pre - min_pre
division.extend(min_pre)
division.extend(max_pre)
for i in range(10):
    division.extend(min_pre + (i+1)*diff/9)
# 分值区间 转化数 总样本数 区间转化率
lst_df = []
for i in range(len(division)-1):  # 调整输出格式
    row_lst = []
    row_lst.extend((division[i], division[i+1]))
    if y[(y['predict']>=division[i]) & (y['predict']<division[i+1]) & (y['label']==1)]['label'].count() > 0:
        row_lst.extend(y[(y['predict']>=division[i]) & (y['predict']<division[i+1]) & (y['label']==1)]['label'].count())
        row_lst.extend(y[(y['predict']>=division[i]) & (y['predict']<division[i+1]) & (y['label']==1)]['label'].count() 
                      / y[(y['predict']>=division[i]) & (y['predict']<division[i+1])]['label'].count())
    else:
        row_lst.extend(0)
        row_lst.extend(0)
    lst_df.append(row_lst)
result = pd.DataFrame(lst_df, columns=['section', 'trf_cnt', 'section_cnt'])
print(result)

# 参数调整：数据集划分增加验证集
# https://zhuanlan.zhihu.com/p/76206257


