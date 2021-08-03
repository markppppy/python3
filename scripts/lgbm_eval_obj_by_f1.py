#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : lgbm_eval_obj_by_f1.py
# @Desc    : 
# @Time    : 2021/8/3 9:44
# @Author  : songpeiyao
# @Version : 1.0
import typing as array
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv()  # label, feature_1, feature_2, ...
df_x = df[:, 1:]
df_y = df[:, :1]

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.3, random_state=36)
# stratify 指定的是数据集，如 stratify=df_y, 以 test_size 分割后的 train/test 正负样本比例和 stratify 指定的数据集一致

lgb_train = lgb.Dataset(x_train, y_train,
                        free_raw_data=False)  # weight 指定每个样本的权重  free_raw_data 释放原始数据？如果为True, 变量x_train和y_train会被清空?
lgb_eval = lgb.Dataset(x_train, y_test, reference=lgb_train, free_raw_data=False)  # 验证数据会被建议reference设为训练数据

params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': 'binary_logloss',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0
}


# self-defined objective function
# f(preds: array, train_data: Dataset) -> grad: array, hess: array
# log likelihood loss
def loglikelihood(preds, train_data):
    labels = train_data.get_label()
    preds = 1. / (1. + np.exp(-preds))
    grad = preds - labels  # 预测值和实际标签值之间的差 1列n行 一阶导数
    hess = preds * (1. - preds)  # 二阶导数
    return grad, hess


def binary_f1_loss(preds, train_data):
    # 计算出 f1 然后用 1 - f1 作为loss

    return


# self-defined eval metric
# f(preds: array, train_data: Dataset) -> name: string, eval_result: float, is_higher_better: bool
# binary error
# NOTE: when you do customized loss function, the default prediction value is margin
# This may make built-in evaluation metric calculate wrong results
# For example, we are doing log likelihood loss, the prediction is score before logistic transformation
# Keep this in mind when you use the customization
def binary_error(preds, train_data):
    labels = train_data.get_label()
    preds = 1. / (1. + np.exp(-preds))
    return 'error', np.mean(labels != (preds > 0.5)), False


# metric f1
# return name: string, eval_result: float, is_higher_better: bool
def binary_f1_metric(preds: array, train_data):
    y_true = train_data.get_label()
    # scikits f1 doesn't like probabilities
    # y_hat = np.round(y_hat)
    # get threshold
    _fpr, _tpr, _thresholds = metrics.roc_curve(y_true, preds)
    _max_index = (_tpr - _fpr).tolist().index(max(_tpr-_fpr))
    _threshold = _thresholds[_max_index]
    preds = np.where(preds >= _threshold, 1, 0)
    return 'f1', metrics.f1_score(y_true, preds), True


gbm = lgb.train(params,
                lgb_train,
                num_boost_round=10,  # 模型迭代次数
                # init_model=gbm,  # init_model
                fobj=loglikelihood,  # 自定义的目标函数名 和 params 中的 objective是相同的设置, 优先params中设置的
                feval=binary_error,  # 自定义的评价指标名
                valid_sets=lgb_eval)


