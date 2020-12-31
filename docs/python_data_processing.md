[toc]

# Python数据处理知识汇总
## Pandas
### 读取数据文件
pd.read_csv() 参数说明：<br>
- names 若文件中包含列名，则对读取的列重命名，若没有列名，则指定列名
- parse_dates 指定要识别为日期的字符串列
  date_parser 指定日期字符串的格式，如`date_parser=lambda x: pd.to_datetime(x, format='%Y/%m/%d')`
### 通用参数解释
axis: 0 表示操作后行数会变，1 表示操作后列数会变<br>
