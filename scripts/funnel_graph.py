#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : funnel_graph.py
# @Desc    : 
# @Time    : 2021/8/24 11:39
# @Author  : songpeiyao
# @Version : 1.0

import pandas as pd
from pyecharts import Funnel
import numpy as np

df = pd.DataFrame(data=[{'stage': '计划送检课程预计上课时长', 'course_hour': 171320.25, 'rate': 1}
                        , {'stage': '出席课程的预计上课时长', 'course_hour': 147472.75, 'rate': 0.86}
                        , {'stage': '调用接口判断要送检的课程预计上课时长', 'course_hour': 125207.75, 'rate': 0.73}
                        , {'stage': 'asr解析成功课程预计上课时长', 'course_hour': 75471, 'rate': 0.44}
                        , {'stage': 'asr解析成功课程录制时长', 'course_hour': 77126.736, 'rate': 0.45}])

attrs = df['stage'].tolist()
attr_value = (np.array(df['rate']) * 100).tolist()

funnel = Funnel("检测时长损失分析", width=800, height=400, title_pos='center')
funnel.add(name="课程送检环节",  # 指定图例名称
           attr=attrs,  # 指定属性名称
           value=attr_value,  # 指定属性所对应的值
           is_label_show=True,  # 指定标签是否显示
           label_formatter='{b}{c}%',  # 指定标签显示的格式
           label_pos="outside",  # 指定标签的位置
           is_legend_show=False)  # 指定图例不显示图例
# todo 还没没有画出满意的漏斗图
funnel.render()

