#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : funnel_graph.py
# @Desc    : 
# @Time    : 2021/8/24 11:39
# @Author  : songpeiyao
# @Version : 1.0

import pandas as pd
from pyecharts.charts import Funnel
import numpy as np
from pyecharts import options as opts

df = pd.DataFrame(data=[{'stage': '计划送检课程预计上课时长', 'course_hour': 171320.25, 'rate': 1}
                        , {'stage': '出席课程的预计上课时长', 'course_hour': 147472.75, 'rate': 0.86}
                        , {'stage': '调用接口判断要送检的课程预计上课时长', 'course_hour': 125207.75, 'rate': 0.73}
                        , {'stage': 'asr解析成功课程预计上课时长', 'course_hour': 75471, 'rate': 0.44}
                        , {'stage': 'asr解析成功课程录制时长', 'course_hour': 77126.736, 'rate': 0.45}])

attrs = df['stage'].tolist()
attr_value = (np.array(df['rate']) * 100).tolist()

# pyecharts==1.9.0
# https://pyecharts.org/#/zh-cn/intro

c = (
    Funnel(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        "课程送检环节"
        , [list(z) for z in zip(attrs, attr_value)]
        , sort_="descending"
        , label_opts=opts.LabelOpts(position="inside", formatter='{b}:{c}%')
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="课程送检环节"))
    .render("funnel_sort_desc.html")  # 会在同目录下生成文件
)

