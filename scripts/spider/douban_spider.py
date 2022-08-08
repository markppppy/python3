import requests
from bs4 import BeautifulSoup
import time


for page in range(0,5):
    start=page*20  #url页面起始标记
    time.sleep(1)  #睡眠一秒
    print('页数：', page)
    db_url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T'.format(start) #得到请求的页面地址


    #请求头参数
    headers ={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    resp = requests.get(db_url,headers=headers) #获取返回的对象
    soup = BeautifulSoup(resp.text,'lxml') #解析返回的数据

    names = soup.find_all('div',attrs={"class":"info"}) #获取书本所有信息
    for name in names:
        book_name = name.find('h2').get_text().strip() #获取书名
        score = name.find('span',attrs={'class':'rating_nums'}).get_text().strip() #获取评分

        print(book_name, score)

