[toc]

# Python数据处理知识汇总

## Pandas

---

### 读取数据文件

pd.read_csv() 参数说明：<br>
- names 若文件中包含列名，则对读取的列重命名，若没有列名，则指定列名
- parse_dates 指定要识别为日期的字符串列
  date_parser 指定日期字符串的格式，如`date_parser=lambda x: pd.to_datetime(x, format='%Y/%m/%d')`
---

### 查看dataframe信息
```python
df.info()  # df的数据类型和空值数
df.isnull().sum()  # 每列的空值数
df_origin.describe()  # 每列的统计值
df[col].dtypes  # col列的数据类型
df.shape  # df的形状，即行列数
```

### 修改df数据类型(待补充)
```python
df[col].astype('object')  # astype会有隐藏的错误
# 参考：https://zhuanlan.zhihu.com/p/35287822
```

### 去重

`df_unique = df_origin.drop_duplicates(subset=['column_name'], keep='first')`<br>
- df_origin中可以包含其他列；<br>
- keep为`first`表示保留第一次出现重复值的行，`last`反之，也可以为`False`, 表示删除有重复的行；<br>
---

### 判空
`df.empty`  df是否为空
- return True or False

`df['col']` 某列值是否为Nan
- return True or False

---

### 空值替换

`df.fillna(0)` or `df['col'].fillna(0)`
- 不仅可以传入0, 也可以传`df['col_else']`其他列

---

### 取出为null指的列 or 删除某列为空值的行

`df[df['col'].isnull()]`
`df_drop = df.dropna(subset=['col'], axis=0)`

--- 

### 排序
```python
df.sort_values(by='create_dt', ascending=True, inplace=True)
df.reset_index(drop=True, inplace=True)  # 排序后index会打乱，根据需要reset_index
```
---

### 分组聚合

`df_agg = df_origin.groupby('spread_source_code').agg({'total_cnt':np.sum,'pay_cnt':np.sum,'called_cnt':np.sum,'invalid_cnt':np.sum})`

---

### 实现hive中的窗口函数

`df['row_number'] = df['predict_true'].groupby(df['id']).rank(ascending=False, method='first')`
- method控制排名方式<br>
- [参考链接](https://www.jianshu.com/p/6ef54e943ad0)
---

### 根据已有列判断或计算生成新的列

1. `df['new_column'] = np.select([(df['total_cnt'] != 0), (df['total_cnt'] == 0)], [df['called_cnt'] / df3['total_cnt'], 0])`
    - `.select()` 第一个参数列表是不同的条件，第二个列表对应的是不同条件对应的不同值
2. 也可以写个函数作用于某一列，如: `df[col_new] = df['col'].map(fuc)`

---

### 对行列索引重命名

`df.rename(columns={'col_orgn1': 'col_new1', 'col_orgn2': 'col_new2'}, index={})` 该方法既可以修改列名也可以修改行名; <br>

---

### 选取指定行列索引, 并添加新行列

`df.reindex(index=[], columns=[])` 选取已有的列，没有的列值会用NaN填充; <br>

---

### 打乱df中的行

`data_shuffle = data.sample(frac=1)` `.sample()`随机抽样

---

### 获取整个df的前百分之n行的df

`train = df_sample[df_sample.index <= df_sample['label'].count()*0.8]` 取`df_sample`的前80%作为新的df

---


### 根据列值筛选，删除某行

`df.drop(df[(df['col1'] == 1) & (df['col2'] >= 1)].index)`
- 运算符：`&` 且; `|` 或

---

### 获取某个值

`df[df['id']=='1']['grade_id'].values[0]`
  - `df[df['id']=='1']['grade_id']`这样取会带索引

---

### 通过`.loc[] .iloc[]`获取或增加df中的数据

`df.loc[]`通过索引获取数据: `df.loc["line1":"line2", "row1":"row2"]` 逗号前后是行列; 取的数据包含`line2`和`row2`; 获取指定列:`df.loc[:, "row1"]`; 
df.loc[df['sex']=='f','sex'] = 0
<br>
`df.iloc[]`通过行列位置获取数据: `df.iloc[n1:n2, n3:n4]` 行列数从0起, n1表示第n1行; 取的数据不包含`n2`和`n4`; 取指定行的时候使用:`df.iloc[[n1, n2]] or df.iloc[n1:n2:1]`;

---

### 计算日期列时间差

```python
import pandas as pd
from datetime import datetime

data = [{'teacher_id': 12, 'entry_dt': '2021-02-05'}, {'teacher_id': 123, 'entry_dt': '2021-02-15'}]
df = pd.DataFrame(data, columns=['teacher_id', 'entry_dt'])

today = datetime(2200, 1, 1)
# df['days_diff'] = list(map(lambda x: x.days, df['entry_dt'] - pd.to_datetime('today')))

df['entry_dt'] = pd.to_datetime(df['entry_dt'])
df['days_diff'] = (df['entry_dt'] - today).apply(lambda x: x.days)
```

---

### dataframe字符串日期转datetime64
```python
df_origin['create_time'] = pd.to_datetime(df_origin['create_time'].str[:-2], format='%Y-%m-%d%H:%M:%S')  # 2021-02-2419:52:55.0
```

---

### df写入数据库

```python {.highlight=3-4}
from sqlalchemy import create_engine

engine_api_mobdb = create_engine("mysql+pymysql://usrname:pwdword@host:port/dbname?charset=utf8")
df.to_sql("table_name", con=engine_api_mobdb, if_exists='replace', index=False)
```
- replace 会先删掉表后重建表 
---

### df通过sql创建

```python {.line-numbers}
import pymysql

sql5 = '''select ...'''
connect_api_mobdb = pymysql.connect(user=user, passwd=passwd, host=host[3], port=port[3], db=db[3], charset='utf8')
df_api = pd.read_sql(sql=sql5, con=connect_api_mobdb)
```
---

### 通用参数解释

- axis: 0 表示操作后行数会变，1 表示操作后列数会变<br>
- 
---

### 待解析的复杂语句

- 每个渠道评级按score_rank出现最多的取，如果最多的score_rank有多个，取等级最高的<br>
  ```python
  from collections import Counter
  # 每个渠道评级按score_rank出现最多的取，如果最多的score_rank有多个，取等级最高的
  df7.loc[:, 'score_rank'] = df7.groupby('spread_source_code')['score_rank'].transform(lambda x: Counter(x).most_common(1)[0][0])
  ```
---

### Pandas使用感悟

- 遍历dataframe中的行(`df.iterrows()` or `df.itertuples()`)返回的是series，不方便操作, 可以把df转换为字典列表(`df.to_dict('records')`)会更好操作，至少目前这样认为；


