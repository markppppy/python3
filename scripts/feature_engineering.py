#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : featurn_engineering.py
# @Desc    : 
# @Time    : 2021/4/14 17:08
# @Author  : songpeiyao
# @Version : 1.0

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

# 读取数据，如果需要按时间顺序划分样本数据，生成文档前把数据按时间排序
# names对文档中的列重命名
df = pd.read_excel(r'D:\Documents\A算法组-PY应用和算法服务开发集成\试听直排重构\数据\0402扩展学生侧特征\0408全部样本扩展学生侧特征.xlsx'
                   , header=0
                   , names=[''])

# 数据复制
df_origin = copy.deepcopy(df)

# 提取其中的特征列名、标签列名、唯一标志列名
columns = list(df_origin.columns)
only_col = columns[: 1]  # 唯一列名
lbl_feat = columns[6: -1]  # 标签列名、特征列名
only_col.extend(lbl_feat)

# 输出各列缺失值数量：缺失值分布; 删除主要列如标签列，唯一列缺失的样本
shp = df_origin.shape  # tuple
null_statistic = df_origin.isnull().sum()  # Series
print(shp)
print(null_statistic)

# 删除主要列如标签列，唯一列等缺失的样本
df_origin.dropna(subset=['arrange_way'], axis=0, inplace=True)
df_origin.reset_index(drop=True, inplace=True)

# 属性特征每个类别样本占比 每个类别分布
attribute_col = ['']  # 指定属性列名
for col in attribute_col:
    attribute_lv = df_origin.groupby(col)[col].count() / df_origin[col].count()  # attribute_lv Series

# 特征处理 - 属性特征缺失值处理  怎么用代码判断一列是数值还是属性；
# 属性特征缺失填充，不论缺失多少都不删除特征; 填充后可以做特征扩展;
# 确认属性列能否用0替换：0本身在这个类别中没有含义
attribute_col = ['']  # 指定属性列名
for col in attribute_col:
    df_origin[col].fillna(0, inplace=True)

# 属性特征：null值占比大于0.4，删除；反之，用值填充
# for col in attribute_col:
#     if df_origin[col].isnull().sum() / df_origin[col].isnull().count() > 0.4:
#         # df_origin.drop(col, axis=1, inplace=True)
#         only_col.remove(col)
#     else:
#         df_origin[col].fillna(0, inplace=True)

# 特征处理 - 数值特征缺失值处理
# 数值列: 只对缺失值填充, 不删除特征; 数值型处理方式不统一，如trf_tate可以用0填充，高考距今月数就不能
# numerical_col = ['']  # 指定数值列名
# 个性化处理
process_df = df_origin['create_dt'].map(lambda x: x.month)
df_origin.loc[df_origin['gk_mon_diff'] < 0, 'gk_mon_diff'] = (12 - df_origin['reg_grade']) * 12 - process_df + 6
df_origin.loc[df_origin['gk_mon_diff'] < 0, 'gk_mon_diff'] = df_origin['gk_mon_diff'] + 12
df_origin.loc[df_origin['diff_dt'].isnull(), 'diff_dt'] = df_origin['diff_dt'].median()
df_origin.fillna(0, inplace=True)

# 特征处理 - 离群值处理
alone_col = ['']  # 指定需要处理的列名, 通常是数值型的列; 或者所有列  only_col


# 根据箱线图的上下限进行异常值的填充
def boxplot_fill(_col):
    # 计算iqr：数据四分之三分位值与四分之一分位值的差
    iqr = _col.quantile(0.75) - _col.quantile(0.25)
    # 根据iqr计算异常值判断阈值
    u_th = _col.quantile(0.75) + 1.5 * iqr  # 上界
    l_th = _col.quantile(0.25) - 1.5 * iqr  # 下界

    # 定义转换函数：如果数字大于上界则用上界值填充，小于下界则用下界值填充。
    def box_trans(x):
        if x > u_th:
            return u_th
        elif x < l_th:
            return l_th
        else:
            return x

    return _col.map(box_trans)


for col in alone_col:
    # 确定该列的上下界
    df_origin[col] = boxplot_fill(df_origin[col])


# 特征处理 - 纠偏
rectify = ['']  # 需要转化为正态分布的列, 通常为数值列;
pt = preprocessing.PowerTransformer(method='yeo-johnson', standardize=True, copy=False)  # standardize 将转化后的数据标准化
dt_fit = df_origin[rectify]
pt.fit(dt_fit)
pt.transform(dt_fit)
dt_fit = pd.DataFrame(dt_fit, columns=rectify)
df_origin[rectify] = dt_fit  # 是给df_origin中的rectify这些列赋值

# 特征处理 - 标准化(省略，lgbm暂时不需要) 归一化 在计算方法和含义上的区别 标准化需要数据服从正态分布? 那就在纠偏之后做

# 特征处理 - 线性相关性(省略，这一步的目的是防止多重共线性，这种现象不会影响决策树)
# 多重共线性怎么在线性回归中成为问题: https://blog.csdn.net/weixin_26750481/article/details/108499848
# 相关性计算方法有：Pearson Kendall Spearman, 其中 Kendall Spearman 都可用于计算类别特征相关性，具体使用条件待查
df_origin[['gk_mon_diff', 'label']].corr()

# 类别特征编码：one-hot和哑编码 lgbm不需要这一步，其会对类别特征值两两组合分类，以验证效果；

# 特征筛选：根据特征重要性排序，循环删除重要性最低的特征，保证特征删除后，auc的值下降不超过0.02
auc_lst = []
feature_importance = []
auc_diff = 0
drop_feature = ''
max_auc = 0
param = {
    'max_depth': 6
    , 'max_bin': 255
    , 'num_leaves': 31  # 待调整
    , 'learning_rate': 0.01
    , 'lambda_l1': 0.1
    , 'lambda_l2': 0.1
    , 'objective': 'binary'
    , 'boosting_type': 'gbdt'
    , 'metric': ['auc', 'binary_logloss']
    #     , 'categorical_feature': [3, 4, 5, 7, 8]
    , 'is_unbalance': True
    #     , 'early_stopping_round': 20
}
feature_cols = only_col[3:]  # 指定特征列名


def get_params_return_model(_params: dict, _df: pd.DataFrame, _feature_cols=None,  appoint_df=None):
    """
    传入特征列、参数、df返回模型
    :param appoint_df:
    :param _feature_cols: 特征列名
    :param _params: 模型参数
    :param _df: 原始df
    :return: _model、_x_test、_y_test
    """
    if appoint_df is None:
        _df_new = _df[_feature_cols]
    else:
        _df_new = appoint_df
    _df_new['label'] = _df['label']
    # 特征筛选2：数据集划分,  并输出训练集和测试集的正负例数和占比
    # 样本按时间排序(取数时已排序)，7:3划分训练集和测试集
    _df_train = _df_new[_df_new.index < _df_new['label'].count() * 0.7]
    _df_tst = _df_new[_df_new.index >= _df_new['label'].count() * 0.7]
    # 以指定比例划分标志，区分测试数据中的样本排课方式
    # _agreement_id = _df[['agreement_id', 'arrange_way']]
    # _agreement_id_tst = agreement_id[(agreement_id.index >= agreement_id['agreement_id'].count() * 0.7)]
    #  验证按时间分正负例分布是否均匀
    print("训练集：%s, %s" % (_df_train[_df_train['label'] == 1]['label'].count(), _df_train['label'].count()))
    print("测试集：%s, %s" % (_df_tst[_df_tst['label'] == 1]['label'].count(), _df_tst['label'].count()))
    print('训练集正例占比：%s, 测试集正例占比：%s' % (_df_train[_df_train['label'] == 1]['label'].count() / _df_train['label'].count()
                                      , _df_tst[_df_tst['label'] == 1]['label'].count() / _df_tst['label'].count()))
    # 特征筛选3：构造特征数据
    _x_train = _df_train.drop(columns=['label'], axis=1)
    _x_test = _df_tst.drop(columns=['label'], axis=1)
    _y_train = _df_train[['label']]
    _y_test = _df_tst[['label']]
    _train_data = lgb.Dataset(data=_x_train, label=_y_train)
    _test_data = lgb.Dataset(data=_x_test, label=_y_test)
    # 特征筛选4：设置参数并训练模型
    _model = lgb.train(param, _train_data, valid_sets=[_test_data])
    return _model, _x_test, _y_test


# 当前筛选方法是根据auc的变化依次删掉特征重要性最弱的特征；但实际上特征重要性强弱是相对的，这次删除的重要性最弱的特征，可能在多了或少了其他特征之后成为重要性强的特征
while auc_diff < 0.02:
    if drop_feature in feature_cols:
        feature_cols.remove(drop_feature)
    model, x_test, y_test = get_params_return_model(param, df_origin, feature_cols)

    # 特征筛选5：记录排序后的特征重要性，并取出重要性最低的特征
    importance_list = model.feature_importance()  # importance_type='gain'
    feature_list = model.feature_name()
    feature_dict = {feature_list[i]: importance_list[i] for i in range(len(feature_list))}
    result = sorted(feature_dict.items(), key=lambda x: x[1], reverse=True)
    feature_importance.append(result)
    drop_feature = result[-1][0]
    # 测试数据预测
    ypred = model.predict(x_test)
    # 特征筛选6：模型评价指标-auc; 记录每次删除特征后的auc
    fpr, tpr, thresholds = metrics.roc_curve(y_test, ypred)
    cur_auc = metrics.auc(fpr, tpr)
    auc_lst.append(float(cur_auc))
    max_auc = max(auc_lst)
    auc_diff = max_auc - auc_lst[-1]

# 在上面根据特征重要性筛选出相对中要的特征组合后，对筛选后的特征进行扩展
# 获取上一步筛选后，模型效果最好的特征
feature_lst_tuple = feature_importance[auc_lst.index(max_auc)]
feature_name_lst = [tp[0] for tp in feature_lst_tuple]
# 对比特征扩展后的模型效果 cur_auc 和之前的模型效果 max_auc
polynomy = preprocessing.PolynomialFeatures(degree=2)
np_new = polynomy.fit_transform(df_origin[feature_cols])
df_new = pd.DataFrame(np_new)
model, x_test, y_test = get_params_return_model(param, df_origin, appoint_df=df_new)
# 测试数据预测
ypred = model.predict(x_test)
fpr, tpr, thresholds1 = metrics.roc_curve(y_test, ypred)
cur_auc = metrics.auc(fpr, tpr)

# 参数搜索: 需要从数据集中划分出验证集
# https://zhuanlan.zhihu.com/p/76206257


# 效果统计：根据最后确定的特征训练出的模型，统计在测试数据上的效果，并输出 auc
ypred = model.predict(x_test)
y_pred = pd.DataFrame(data=ypred, columns=['predict'])
y_test_df = y_test.reset_index(drop=True)
# agreement_id_tst = agreement_id_tst.reset_index(drop=True)
y = pd.concat([y_pred, y_test_df], axis=1)  # , agreement_id_tst
# y = y[y['arrange_way'] == 1.0]  # 只取测试数据中的直排样本
# division = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# 调整为上下界为预测分值的最大值和最小值，并分为10等分
division = []
max_pre = y['predict'].max()
min_pre = y['predict'].min()
diff = max_pre - min_pre
division.extend(min_pre)
division.extend(max_pre)
for i in range(10):
    division.extend(min_pre + (i + 1) * diff / 9)
# 分值区间 转化数 总样本数 区间转化率
lst_df = []
for i in range(len(division) - 1):
    row_lst = []
    row_lst.extend((division[i], division[i + 1]))
    if y[(y['predict'] >= division[i]) & (y['predict'] < division[i + 1]) & (y['label'] == 1)]['label'].count() > 0:
        row_lst.extend(
            y[(y['predict'] >= division[i]) & (y['predict'] < division[i + 1]) & (y['label'] == 1)]['label'].count())
        row_lst.extend(
            y[(y['predict'] >= division[i]) & (y['predict'] < division[i + 1]) & (y['label'] == 1)]['label'].count()
            / y[(y['predict'] >= division[i]) & (y['predict'] < division[i + 1])]['label'].count())
    else:
        row_lst.append(0)
        row_lst.append(0)
    lst_df.append(row_lst)
result = pd.DataFrame(lst_df, columns=['section', 'trf_cnt', 'section_cnt'])
print(result)

# 根据roc确定最佳阈值
i = np.arange(len(tpr))
roc = pd.DataFrame({'tf' : pd.Series(tpr-(1-fpr), index=i), 'threshold' : pd.Series(thresholds, index=i)})
roc_t = roc.iloc[(roc.tf-0).abs().argsort()[:1]]
print(list(roc_t['threshold']))

