##美团H5版爬虫，最终可以顺利爬取所有城市，所有网咖店面的评分
import requests
import time
import random
import pandas as pd
from bs4 import BeautifulSoup

net_bar=[] 
city={
'西安':'42',
'无锡':'52',
'长沙':'70',
'天津':'40',
'大连':'65',
'济南':'96',
'北京':'1',
'珠海':'108',
'苏州':'80',
'沈阳':'66',
'昆明':'114',
'杭州':'50',
'深圳':'30',
'武汉':'57',
'青岛':'60',
'成都':'59',
'广州':'20',
'南京':'55',
'上海':'10',
}
for key,value in city.items():
    for page in range(1,100):
        n = random.randint(1, 4)
        time.sleep(n)
        url = 'http://i.meituan.com/s/a'  
        refer_o = "http://i.meituan.com/s/-网咖/?p={}".format(page)
        cookie_o = '__mta=20395527.1648867423092.1648989986655.1650016030975.15; uuid=428f82cf746d74e9ab8d.1615877759.1.0.0; _lxsdk_cuid=1783fc46d06c8-08d7cb97442812-5771133-384000-1783fc46d06c8; _ga=GA1.2.783433310.1644213814; iuuid=D6CEC1292E199D9B9B8C75E91C640323584A9B5F3D8FA1E3A4FF1231638DFD0F; _lxsdk=D6CEC1292E199D9B9B8C75E91C640323584A9B5F3D8FA1E3A4FF1231638DFD0F; webp=1; mtcdn=K; JSESSIONID=node0111yapf86eq5b1bpzolg0hh8md55299646.node0; IJSESSIONID=node0111yapf86eq5b1bpzolg0hh8md55299646; __utmc=74597006; rvct=114,10,1,59,80,66,42,50,20,55,30; ci3=10; WEBDFPID=v8y6917499v359ywz63v086u677wvvxv818zv2649y197958x152y817-1656575601885-1656489201317SWQSCIQfd79fef3d01d5e9aadc18ccd4d0c95071632; __utmz=74597006.1656489283.7.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ci={}; cityname={}; u=45249329; n=董胖dyk; lt=CiWGpncAZHHD7g6mTl089OWtXkkAAAAAjBIAAJfU4H32XSm7HAeCiIE1-UZx-i61BQriFeIXs_ir4DvPxrIjFXy5oToBq6gKvmJwmQ; mt_c_token=CiWGpncAZHHD7g6mTl089OWtXkkAAAAAjBIAAJfU4H32XSm7HAeCiIE1-UZx-i61BQriFeIXs_ir4DvPxrIjFXy5oToBq6gKvmJwmQ; token=CiWGpncAZHHD7g6mTl089OWtXkkAAAAAjBIAAJfU4H32XSm7HAeCiIE1-UZx-i61BQriFeIXs_ir4DvPxrIjFXy5oToBq6gKvmJwmQ; token2=CiWGpncAZHHD7g6mTl089OWtXkkAAAAAjBIAAJfU4H32XSm7HAeCiIE1-UZx-i61BQriFeIXs_ir4DvPxrIjFXy5oToBq6gKvmJwmQ; unc=董胖dyk; isid=CiWGpncAZHHD7g6mTl089OWtXkkAAAAAjBIAAJfU4H32XSm7HAeCiIE1-UZx-i61BQriFeIXs_ir4DvPxrIjFXy5oToBq6gKvmJwmQ; oops=CiWGpncAZHHD7g6mTl089OWtXkkAAAAAjBIAAJfU4H32XSm7HAeCiIE1-UZx-i61BQriFeIXs_ir4DvPxrIjFXy5oToBq6gKvmJwmQ; logintype=normal; idau=1; __utma=74597006.783433310.1644213814.1656489283.1656494472.8; _lx_utm=utm_source=Baidu&utm_medium=organic; firstTime=1656494483451; i_extend=GimthomepagesearchH__a100005__b8; _lxsdk_s=181aebd1cdf-11f-cd1-7c8||189; webloc_geo=31.09843,121.316784,wgs84,-1; latlng=31.09843,121.316784,1656496138284; __utmb=74597006.28.9.1656496150103'.format(value,key)
        refer=refer_o.encode('UTF-8')
        cookie = cookie_o.encode('UTF-8')
        headers ={
            "Referer": refer,
            "Host":'i.meituan.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
            'Cookie':cookie }

        data = {
            'cid':'-1',
            'bid':'-1',
            'sid':'defaults',
            'p': page,
            'ciid':value,
            'bizType':'area',
            'csp':'',
            'nocount':'true',
            'stid_b':'_b2',
            'w':'网咖,'
        }
        print(refer_o,key,value)
        response = requests.get(url, params=data, headers=headers)
        print(response)
        soup=BeautifulSoup(response.text,'lxml')
        ilist = soup.find_all('dd',{'class':'poi-list-item'})
        if response.status_code==403:
            print(page)
            break
        elif ilist==[]:
            break
        else:
            for i in ilist:
                name = i.find('span',{'class':'poiname'}).get_text()
                score = i.find('div',{'class':'kv-line-r'}).get_text().replace("\n","")
                dic={
                    '城市':key,
                    '店名':name,
                    '评分':score
                }
                net_bar.append(dic)
print(net_bar)
dd=pd.DataFrame.from_dict(net_bar)
dd.to_excel(r"C:\Users\110815\Desktop\mt_netbar2.xlsx",index=False)