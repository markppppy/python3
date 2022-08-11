#点评网页
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_driver():
    # s = Service(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver_win32\chromedriver.exe")
    s = Service(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('--disable-javascript') # 禁用javascript
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument('--start-maximized') # 最大化运行（全屏窗口）,不设置，取元素会报错
    options.add_argument('--disable-infobars') # 禁止策略化
    options.add_argument('--incognito') # 隐身模式（无痕模式）
    #options.add_argument('--headless') # 浏览器不提供可视化页面
    driver = webdriver.Chrome(service=s,options=options)
    return driver

def get_info(city,driver):
    soup = BeautifulSoup(driver.page_source,"lxml")
    info = soup.find_all(class_ = "list-item border-bottom-new")
    a_list=[]
    for i in info:
        hotel_name=i.find(class_='item-shop-name').get_text()
        try:
            comment = i.find(class_="star star-0").get_text()
        except:
            try:
                comment = i.find(class_="seed-star_wrap").get_text()
            except:
                try:
                    comment = i.find(class_="seed-star_score seed-score_35").get_text()
                except:
                    comment= i.find(class_="item-comment").get_text() 
        print(hotel_name,comment)
        a_list.append([city,hotel_name,comment])
        sdata = pd.DataFrame(a_list,columns=['city','hotel_name','comment'])
    return sdata

    

def main():
    driver = get_driver()
    url = 'https://m.dianping.com/'
    # 未携带cookies打开网页
    driver.get(url)
    citys={ "上海":"S",
            # "北京":"B",
            # "广州":"G",
            # "深圳":"S",
            # "天津":"T",
            # "西安":"X",
            # "杭州":"H",
            # "南京":"N",
            # "武汉":"W",
            # "成都":"C",
            # "青岛":"Q",
            # "无锡":"W",
            # "长沙":"C",
            # "大连":"D",
            # "昆明":"K",
            # "珠海":"Z",
            # "济南":"J",
            # "苏州":"S",
            "沈阳":"S"
                }
    df = pd.DataFrame() 
    for city,position in citys.items():
        print(city,position)
        if city=='上海':
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/span").click()
            time.sleep(3)
            sinput=driver.find_element(By.ID, "search-banner-input")
            sinput.send_keys("网咖")
            time.sleep(3)
            sinput.send_keys(Keys.ENTER)
            time.sleep(6)
            js='return document.body.scrollHeight;'
            height=0
            while True:
                new_height = driver.execute_script(js)
                if new_height > height:
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    height = new_height
                    time.sleep(5)
                else:
                    print("滚动条已经处于页面最下方!")
                    driver.execute_script('window.scrollTo(0, 0)')#页面滚动到顶部
                    break
            info =get_info(city,driver)
            df=df.append(info)

        else:
            driver.find_element(By.CLASS_NAME,"newback").click()
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[1]/div[2]").click() 
            time.sleep(3)
            try:
                driver.find_element(By.LINK_TEXT,city).click()
            except:
                driver.find_element(By.XPATH,'//*[@id="{}"]/div[2]/ul/li[21]/a'.format(position)).click()
                time.sleep(3)    
                driver.find_element(By.LINK_TEXT,city).click()
            time.sleep(3)
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/span").click()
            time.sleep(3)
            sinput=driver.find_element(By.ID, "search-banner-input")
            sinput.send_keys("网咖")
            time.sleep(3)
            sinput.send_keys(Keys.ENTER)
            time.sleep(5)
            js='return document.body.scrollHeight;'
            height=0
            while True:
                new_height = driver.execute_script(js)
                if new_height > height:
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    height = new_height
                    time.sleep(5)
                else:
                    print("滚动条已经处于页面最下方!")
                    driver.execute_script('window.scrollTo(0, 0)')#页面滚动到顶部
                    break
            info =get_info(city,driver)
            df=df.append(info)
    print(df.count)
    df.to_excel(r"dp_netbar_0630_5.xlsx")

main()
