import pandas as pd
import datetime
import time
from odps import ODPS
from bs4 import BeautifulSoup
import argparse
import os 

parser=argparse.ArgumentParser()
parser.add_argument('folder_path',type = str)
args = parser.parse_args()

############### 日期参数设置
now = datetime.datetime.now()
#取前一天的时间
yes = now + datetime.timedelta(days = -1)
#当前月的天数
days = time.localtime(time.mktime((yes.year,yes.month+1,1,0,0,0,0,0,0))-86400).tm_mday
month_interval = str(yes.month)+'月'+'1'+'日'+'-'+str(yes.month)+'月'+str(yes.day)+'日'
date_interval=str(yes.month)+'.'+'1'+'-'+str(yes.month)+'.'+str(yes.day)
month_process='{:.0%}'.format(yes.day/days) 
st_date=str(datetime.datetime(now.year, now.month, 1))[0:10].replace('-','')
ed_date=str(now + datetime.timedelta(days=-1))[0:10].replace('-','')
m_last_day = datetime.date(now.year, now.month, 1) - datetime.timedelta(days=1)
lst_date=str(datetime.date(m_last_day.year, m_last_day.month, 1))[0:10].replace('-','')
led_date=str(m_last_day)[0:10].replace('-','')
yyf_date=str(now + datetime.timedelta(days=-7))[0:10].replace('-','')
yyl_date=str(now + datetime.timedelta(days=-1))[0:10].replace('-','')

###############读取sql文件
with open(os.path.join(args.folder_path,'t1_sql_all.sql'),encoding='utf-8') as r:
    t1_sql_all=r.read().format(st_date=st_date,ed_date=ed_date,lst_date=lst_date,led_date=led_date)
with open(os.path.join(args.folder_path,'t1_sql_org3.sql'),encoding='utf-8') as r:
    t1_sql_org3=r.read().format(st_date=st_date,ed_date=ed_date,lst_date=lst_date,led_date=led_date)
with open(os.path.join(args.folder_path,'t2_sql_org2.sql'),encoding='utf-8') as r:
    t2_sql_org2=r.read().format(st_date=st_date,ed_date=ed_date,lst_date=lst_date,led_date=led_date)
with open(os.path.join(args.folder_path,'t3_sql_comcode.sql'),encoding='utf-8') as r:
    t3_sql_comcode=r.read().format(st_date=st_date,ed_date=ed_date)
with open(os.path.join(args.folder_path,'t4_sql_org3.sql'),encoding='utf-8') as r:
    t4_sql_org3=r.read().format(yyf_date=yyf_date,yyl_date=yyl_date)
with open(os.path.join(args.folder_path,'t5_sql_org3.sql'),encoding='utf-8') as r:
    t5_sql_org3=r.read()
with open(os.path.join(args.folder_path,'t5_sql_detail.sql'),encoding='utf-8') as r:
    t5_sql_detail=r.read().format(yyf_date=yyf_date)
	

#读取数据库数据
odps = ODPS('LTAI4GHt625TWvmy8VTHupU6', 'AFPC3xYIuMaetVFS73FxA9gBmXkmbc', 'wywk_dt_dev',endpoint='http://service.odps.aliyun.com/api')
with odps.execute_sql(t1_sql_all).open_reader(tunnel=False)  as reader:
    t1_df_all = reader.to_pandas()
with odps.execute_sql(t1_sql_org3).open_reader(tunnel=False)  as reader:
    t1_df_org3 = reader.to_pandas()
with odps.execute_sql(t2_sql_org2).open_reader(tunnel=False)  as reader:
    t2_df_org2 = reader.to_pandas()
with odps.execute_sql(t3_sql_comcode).open_reader(tunnel=False)  as reader:
    t3_df_comcode = reader.to_pandas()
with odps.execute_sql(t4_sql_org3).open_reader(tunnel=False)  as reader:
    t4_df_org3 = reader.to_pandas()
with odps.execute_sql(t5_sql_org3).open_reader(tunnel=False)  as reader:
    t5_df_org3 = reader.to_pandas()
with odps.execute_sql(t5_sql_detail).open_reader(tunnel=False)  as reader:
    t5_df_detail = reader.to_pandas()
	
####表1修改
t1_df_all_1=t1_df_all[['区域', '店日均售卡量', '店日均售卡量月环比', '店日均销售额', '鱼乐卡总销售额', '有资格购卡销售转换率', '鱼乐卡渗透率', '鱼乐卡当月指标', '当月指标完成率', '新用户当天购卡转化率',
       '当月鱼乐卡销售额占gtv比例']]
t1_df_org3_1=t1_df_org3[['区域', '店日均售卡量', '店日均售卡量月环比', '店日均销售额', '鱼乐卡总销售额', '有资格购卡销售转换率',
        '鱼乐卡渗透率', '鱼乐卡当月指标', '当月指标完成率', '新用户当天购卡转化率',
       ]]
t1_df_org3_2=t1_df_org3_1.sort_values(by='当月指标完成率',ascending=False)
#表1修改value格式
pd.options.mode.chained_assignment = None
t1_df_all_1.loc[:, '店日均售卡量月环比']=t1_df_all_1.loc[:, '店日均售卡量月环比'].apply(lambda x: format((x+0.000001), '.2%'))
t1_df_all_1.loc[:, '有资格购卡销售转换率']=t1_df_all_1['有资格购卡销售转换率'].apply(lambda x: format((x+0.000001), '.2%'))
t1_df_all_1.loc[:, '鱼乐卡渗透率']=t1_df_all_1['鱼乐卡渗透率'].apply(lambda x: format((x+0.000001), '.2%'))
t1_df_all_1.loc[:, '当月指标完成率']=t1_df_all_1['当月指标完成率'].apply(lambda x: format((x+0.000001), '.2%'))
t1_df_all_1.loc[:, '新用户当天购卡转化率']=t1_df_all_1['新用户当天购卡转化率'].apply(lambda x: format((x+0.000001), '.2%'))
t1_df_all_1.loc[:, '当月鱼乐卡销售额占gtv比例']=t1_df_all_1['当月鱼乐卡销售额占gtv比例'].apply(lambda x: format((x+0.000001), '.2%'))
t1_df_all_1['店日均售卡量']=t1_df_all_1['店日均售卡量'].apply(lambda x: ("%.2f")%x)
t1_df_all_1['店日均销售额']='￥' +t1_df_all_1['店日均销售额'].apply(lambda x: ("%.0f")%x).astype(str)
t1_df_all_1['鱼乐卡总销售额']='￥' +t1_df_all_1['鱼乐卡总销售额'].astype(str)
t1_df_all_1['鱼乐卡当月指标']='￥' +t1_df_all_1['鱼乐卡当月指标'].apply(lambda x: ("%.0f")%x).astype(str)
t1_df_org3_2.loc[:, '店日均售卡量月环比']=t1_df_org3_2.loc[:, '店日均售卡量月环比'].apply(lambda x: format(x,".2%"))
t1_df_org3_2.loc[:, '有资格购卡销售转换率']=t1_df_org3_2['有资格购卡销售转换率'].apply(lambda x: format(x,".2%"))
t1_df_org3_2.loc[:, '鱼乐卡渗透率']=t1_df_org3_2['鱼乐卡渗透率'].apply(lambda x:format(x,".2%"))
t1_df_org3_2.loc[:, '当月指标完成率']=t1_df_org3_2['当月指标完成率'].apply(lambda x: format(x,".2%"))
t1_df_org3_2.loc[:, '新用户当天购卡转化率']=t1_df_org3_2['新用户当天购卡转化率'].apply(lambda x: format(x,".2%"))
t1_df_org3_2['店日均售卡量']=t1_df_org3_2['店日均售卡量'].apply(lambda x: ("%.2f")%x)
t1_df_org3_2['店日均销售额']='￥' +t1_df_org3_2['店日均销售额'].apply(lambda x: ("%.0f")%x).astype(str)
t1_df_org3_2['鱼乐卡总销售额']='￥' +t1_df_org3_2['鱼乐卡总销售额'].astype(str)
t1_df_org3_2['鱼乐卡当月指标']='￥' +t1_df_org3_2['鱼乐卡当月指标'].apply(lambda x: ("%.0f")%x).astype(str)
#表1增删改查等操作
t1=pd.concat([t1_df_all_1, t1_df_org3_2], axis=0)
t1['当月鱼乐卡销售额占gtv比例']=t1['当月鱼乐卡销售额占gtv比例'].fillna('-')
t1.insert(9, '{}月时间进度'.format(yes.month),month_process,allow_duplicates = False)
table1 = t1[~t1['区域'].str.contains('小店测试项目组')]
table1.rename(columns={'鱼乐卡当月指标': '鱼乐卡{}月指标'.format(yes.month),'当月指标完成率': '{}月指标完成率'.format(yes.month),'当月鱼乐卡销售额占gtv比例':'{}月鱼乐卡销售额占gtv比例'.format(yes.month)}, inplace=True)
#表1增加合并单元格
table1.columns=pd.MultiIndex.from_tuples([("鱼乐卡（线下）{month}月总进度（{month}.1-{month}.{day}）".format(month=yes.month,day=yes.day), field) for field in table1.columns])
#表1获取文字填充参数
t1_finish_rate=t1.set_index('区域').loc['全国整体','当月指标完成率']
t1_shop_avg_card=t1.set_index('区域').loc['全国整体','店日均售卡量']
t1_shop_avg_amount=t1.set_index('区域').loc['全国整体','店日均销售额'].replace('￥','')
t1_qualification_rate=t1.set_index('区域').loc['全国整体','有资格购卡销售转换率']
t1_ylk_rate=t1.set_index('区域').loc['全国整体','鱼乐卡渗透率']
t1_new_users_rate=t1.set_index('区域').loc['全国整体','新用户当天购卡转化率']
t1_sale_gtv_rate=t1.set_index('区域').loc['全国整体','当月鱼乐卡销售额占gtv比例']

####表2修改
t2_df_org2_1=t2_df_org2[['标准区', '店日均售卡量', '店日均销售额', '鱼乐卡总销售额', '有资格购卡销售转换率', '当月指标完成率', '新用户当天购卡转化率']]
t2_df_org2_2=t2_df_org2_1.sort_values(by='当月指标完成率',ascending=False).reset_index(drop=True)
#表2修改value格式
t2_df_org2_2['店日均售卡量']=t2_df_org2_2['店日均售卡量'].apply(lambda x: ("%.2f")%x)
t2_df_org2_2['店日均销售额']='￥' +t2_df_org2_2['店日均销售额'].apply(lambda x: ("%.0f")%x).astype(str)
t2_df_org2_2['鱼乐卡总销售额']='￥' +t2_df_org2_2['鱼乐卡总销售额'].astype(str)
t2_df_org2_2.loc[:, '有资格购卡销售转换率']=t2_df_org2_2['有资格购卡销售转换率'].apply(lambda x: format(x,".2%"))
t2_df_org2_2.loc[:, '当月指标完成率']=t2_df_org2_2['当月指标完成率'].apply(lambda x: format(x,".2%"))
t2_df_org2_2.loc[:, '新用户当天购卡转化率']=t2_df_org2_2['新用户当天购卡转化率'].apply(lambda x: format(x,".2%"))
#表2增删改查等操作
t2 = t2_df_org2_2[~t2_df_org2_2['标准区'].str.contains('开发东区项目组')]
t2.insert(6, '{}月时间进度'.format(yes.month),month_process,allow_duplicates = False)
table2=t2.drop(t2.loc[t2['店日均售卡量'].astype(float)== 0 ].index)
table2.rename(columns={'店日均售卡量': '店日均销量','当月指标完成率': '预算达成率'}, inplace=True)
#表2增加合并单元格
table2.columns=pd.MultiIndex.from_tuples([("鱼乐卡{month}月数据（{month}.1-{month}.{day}）".format(month=yes.month,day=yes.day), field) for field in table2.columns])
#表2获取文字填充参数
t2_finish_rate1=t2['当月指标完成率'][0]
t2_finish_rate2=t2['当月指标完成率'][1]
t2_finish_rate3=t2['当月指标完成率'][2]
t2_finish_rate1_area=t2['标准区'][0]
t2_finish_rate2_area=t2['标准区'][1]
t2_finish_rate3_area=t2['标准区'][2]

#####表3获取文字填充参数
open_shops=t3_df_comcode.shape[0]
less_one_card=t3_df_comcode[(t3_df_comcode['店日均售卡量']<=1) ].shape[0]
fail_shops=t3_df_comcode[(t3_df_comcode['当月指标完成率']<=yes.day/days)  & (t3_df_comcode['是否设置目标预算'])==1].shape[0]

####表4修改
t4_df_org3_1=t4_df_org3[['营运大区', '店日均销量', '店日均销售额', '鱼乐卡销售总量','销售总金额','鱼乐卡转化率', '有资格购卡销售转换率']]
t4_df_org3_2=t4_df_org3_1.sort_values(by='销售总金额',ascending=False).reset_index(drop=True)
#表4修改value格式
t4_df_org3_2['店日均销量']=t4_df_org3_2['店日均销量'].apply(lambda x: ("%.2f")%x)
t4_df_org3_2['店日均销售额']='￥' +t4_df_org3_2['店日均销售额'].apply(lambda x: ("%.0f")%x).astype(str)
t4_df_org3_2['销售总金额']='￥' +t4_df_org3_2['销售总金额'].astype(str)
t4_df_org3_2.loc[:, '鱼乐卡转化率']=t4_df_org3_2['鱼乐卡转化率'].apply(lambda x: format(x,".2%"))
t4_df_org3_2.loc[:, '有资格购卡销售转换率']=t4_df_org3_2['有资格购卡销售转换率'].apply(lambda x: format(x,".2%"))
#表4获取文字填充参数
yyf_datetime=datetime.datetime.strptime(yyf_date, '%Y%m%d')
yyl_datetime=datetime.datetime.strptime(yyl_date, '%Y%m%d')
week=yyl_datetime.isocalendar()[1]
week_interval=str(yyf_datetime.month)+'.'+str(yyf_datetime.day)+'-'+str(yyl_datetime.month)+'.'+str(yyl_datetime.day)
t4_sale_rate1=t4_df_org3_2['销售总金额'][0]
t4_sale_rate2=t4_df_org3_2['销售总金额'][1]
t4_sale_rate3=t4_df_org3_2['销售总金额'][2]
t4_sale_rate1_area=t4_df_org3_2['营运大区'][0]
t4_sale_rate2_area=t4_df_org3_2['营运大区'][1]
t4_sale_rate3_area=t4_df_org3_2['营运大区'][2]
#表4增加合并单元格
table4=t4_df_org3_2.copy()
table4.columns=pd.MultiIndex.from_tuples([("鱼乐卡第{}周数据（{}）-营运大区".format(week,week_interval), field) for field in table4.columns])

####表5修改
t5=t5_df_org3.copy()
t5['wk']='第' +t5['wk'].astype(str)+'周转化率'
t5['newuser_convert']=t5['newuser_convert'].apply(lambda x: format(x,".0%"))
#表5行转列修改参数
table5=t5.set_index(['大区','wk'])['newuser_convert'].unstack()
table5.columns.name=None
table5=table5.reset_index()
table5=table5[~table5['大区'].str.contains('小店测试项目组')]
table5=table5.sort_values(by=table5.columns[-1],ascending=False).fillna('-')

#打开原始邮件格式并基于上面数据填充
f3=open(os.path.join(args.folder_path,'email4.html'),'r',encoding='utf-8')
soup3 = BeautifulSoup(f3,'lxml')
soup3.find_all('span')[3].string='{}，当月时间进度{}，全国门店鱼乐卡销售数据如下：'.format(month_interval,month_process)
soup3.find_all('b')[0].string='一、全国门店{}月售卡整体表现：'.format(yes.month)
soup3.find_all('span')[5].string="1）截止到{}月{}日，全国鱼乐卡{}月指标完成率".format(yes.month,yes.day,yes.month)
soup3.find_all('span')[11].string="，{}月鱼乐卡销售额占GTV比例为".format(yes.month)
soup3.find_all('b')[1].string= t1_finish_rate
soup3.find_all('b')[2].string=t1_shop_avg_card
soup3.find_all('b')[3].string=t1_shop_avg_amount
soup3.find_all('b')[4].string=t1_qualification_rate
soup3.find_all('b')[5].string=t1_ylk_rate
soup3.find_all('b')[6].string=t1_new_users_rate
soup3.find_all('b')[7].string='{};'.format(t1_sale_gtv_rate)

soup3.find_all('span')[16].string='{month}月（{month}.1-{month}.{day}）'.format(month=yes.month,day=yes.day)
soup3.find_all('span')[18].string='截止{}月{}日'.format(yes.month,yes.day)
soup3.find_all('span')[20].string='{}'.format(t2_finish_rate1_area)
soup3.find_all('span')[24].string='{}'.format(t2_finish_rate2_area)
soup3.find_all('span')[28].string='{}'.format(t2_finish_rate3_area)
soup3.find_all('b')[12].string=t2_finish_rate1
soup3.find_all('b')[14].string=t2_finish_rate2
soup3.find_all('b')[16].string=t2_finish_rate3

soup3.find_all('span')[33].string='三、营运门店 {month}月（{month}.1-{month}.{day}）鱼乐卡销售数据'.format(month=yes.month,day=yes.day)
soup3.find_all('span')[34].string='（仅统计{}月份营业过的{}家门店）：'.format(yes.month,open_shops)
soup3.find_all('span')[37].string='家门店预算达成率＜{}，达成率低于{}月时间进度'.format(month_process,yes.month)
soup3.find_all('span')[39].string='，门店表格见附件{month}.1-{month}.{day}门店达成率数据，请查收；'.format(month=yes.month,day=yes.day)
soup3.find_all('font')[3].string='{}'.format(less_one_card)
soup3.find_all('font')[4].string='{}'.format(fail_shops)

soup3.find_all('span')[43].string='第{}周'.format(week)
soup3.find_all('span')[44].string='({})'.format(week_interval)
soup3.find_all('b')[23].string=t4_sale_rate1_area
soup3.find_all('span')[50].string=t4_sale_rate2_area
soup3.find_all('span')[55].string=t4_sale_rate3_area
soup3.find_all('b')[24].string=t4_sale_rate1
soup3.find_all('b')[26].string=t4_sale_rate2
soup3.find_all('b')[28].string=t4_sale_rate3
soup3.find_all('span')[63].string='第{}周'.format(week)
soup3.find_all('span')[64].string='({})'.format(week_interval)
#得到最终邮件数据和格式
html_email=str(soup3).format(table1=table1.to_html(index=False,classes='table1'),
                              table2=table2.to_html(index=False,classes='table2'),
                              table3=table4.to_html(index=False,classes='table3'),
                              table4=table5.to_html(index=False,classes='table4'))

with open(os.path.join(args.folder_path,'myhtml.html'),encoding='utf-8',mode='w') as f:
    f.write(html_email)
f3.close()


## 附件保存
a1_name='{month}.1-{month}.{day}门店达成率数据.csv'.format(month=yes.month,day=yes.day)
a2_name='{}.{}-{}.{}新客当天购卡率(大区-标准区-城市分区-门店）.csv'.format((now + datetime.timedelta(days=-7)).month,(now + datetime.timedelta(days=-7)).day,yes.month,yes.day)
t3_df_comcode.to_csv(os.path.join(args.folder_path,'{month}.1-{month}.{day}门店达成率数据.csv'.format(month=yes.month,day=yes.day)),index=False,encoding='gbk')
t5_df_detail.to_csv(os.path.join(args.folder_path,'{}.{}-{}.{}新客当天购卡率(大区-标准区-城市分区-门店）.csv'.format((now + datetime.timedelta(days=-7)).month,(now + datetime.timedelta(days=-7)).day,yes.month,yes.day)),index=False,encoding='gbk')

#邮件发送脚本
import openpyxl
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from email.utils import parseaddr,formataddr

def send(receivers, msg, mail_title, filename=None):

    # receivers:接受人邮箱，多个人需要用list
    # msg:邮件正文
    # mail_title:邮件标题
    # filename:邮件附件，可没有
    # 设置发送邮箱的服务器、用户账号及密码
    mail_host = "smtp.exmail.qq.com"  # 设置服务器
    mail_user = "songpeiyao@wywk.cn"  # 用户名
    mail_pass = "68527sPy94"  # 口令

    sender = mail_user
    # 插入一个网页链接/可以按照网页的形式来插正文
    mail_msg = """
    %s
    """  % (msg)

    message = MIMEText(mail_msg, 'html', 'utf-8')
    subject = '%s' %  mail_title  # 邮件标题
    message['Subject'] = Header(subject, 'utf-8')

    ##os.getcwd() # 获取当前脚本所在的路径
    current_path=args.folder_path
    
    filename1=filename[0]
    filename2=filename[1]
    # 添加附件1
    pdfFile1=os.path.join(current_path, filename1)
    pdfApart1 = MIMEApplication(open(pdfFile1, 'rb').read())
    pdfApart1.add_header('Content-Disposition', 'attachment', filename=filename1)
    
    # 添加附件12
    pdfFile2=os.path.join(current_path, filename2)
    pdfApart2 = MIMEApplication(open(pdfFile2, 'rb').read())
    pdfApart2.add_header('Content-Disposition', 'attachment', filename=filename2)

    # 信息添加
    m = MIMEMultipart()
    m.attach(message)
    m.attach(pdfApart1)
    m.attach(pdfApart2)
    m['Subject'] = Header(subject, 'utf-8')


    m['From'] =  sender
    m['To'] = Header(','.join(receivers), 'utf-8')  # 收件人名称

    try:
        smtpObj = smtplib.SMTP_SSL(host=mail_host)
        smtpObj.connect(host=mail_host, port=465)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender,receivers,m.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

#发送邮件
receivers=['dongyukang@wywk.cn','daiwenbing@wywk.cn','lvzhaochang@wywk.cn']
msg=html_email
mail_title="鱼乐卡第{}周（{}）鱼乐卡销售数据".format(week,week_interval)
filename=[a1_name,a2_name]
send(receivers, msg, mail_title, filename)
