# 国家能源集团
import shutil
import note
import requests
import random
import header
from bs4 import BeautifulSoup
import time
import csv


requests.packages.urllib3.disable_warnings()


class spider_1:

    def __init__(self, *args, **kwargs):
        self.big_data = []
        self.url = "https://zhaopin.chnenergy.com.cn/annc/annclist?ggtype=1"
        self.headers = {
            'User-agent': random.choice(header.USER_AGENTS),  # 设置get请求的User-Agent，用于伪装浏览器UA
        }
        self.__data = {
            'pagenum': '1',  # 页面
            'ggtype': '1'
        }
        self.num = self.get_page()
        print(self.num[0], self.num[1])

    def run_(self):
        for i in range(self.num[0]):
            time.sleep(1)
            self.__data['pagenum'] = str(i)
            try:
                req = requests.post(self.url, data=self.__data, headers=self.headers, verify=False)
            except Exception as e:
                print(e)
                return
            req.encoding = 'utf-8'
            html = req.text
            soup = BeautifulSoup(html, "lxml")
            item = soup.find_all('li', class_='list-group-item')
            for j in item:
                item_dict = {}
                item_soup = BeautifulSoup(str(j), 'lxml')
                item_dict['title'] = ''.join(str(item_soup.find('a').text).split())
                item_dict['time'] = ''.join(str(item_soup.find('span').text).split())
                self.big_data.append(item_dict)
        print("sp_1 data_num:" + str(len(self.big_data)))
        self.save_file()

    def get_page(self):
        self.__data['pagenum'] = '0'
        try:
            req = requests.post(self.url, data=self.__data, headers=self.headers, verify=False)
        except Exception as e:
            print(e+"\n网络问题，或requests问题")
        req.encoding = 'utf-8'
        html = req.text
        soup = BeautifulSoup(html, "lxml")
        return int(soup.find_all('li', class_='page-item')[-1].text[
                   soup.find_all('li', class_='page-item')[-1].text.index('，') + 2:-1]), int(
            soup.find_all('li', class_='page-item')[-1].text[
            1:soup.find_all('li', class_='page-item')[-1].text.index('，') - 1])

    def save_file(self):
        with open(r'.\data_temp\国家能源集团.csv', 'w', newline='', encoding='GBK') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['title', 'date'])
            for i in self.big_data:
                writer.writerow([i['title'], i['time']])
            csv_file.close()
        if not header.file_same(r'.\data_temp\国家能源集团.csv',r'.\data\国家能源集团.csv'):
            note.run_note('<big>国家能源集团更新了，快来看看！</big>')
            note.log('sp_1:网站已更新\n')
            shutil.copyfile(r'.\data_temp\国家能源集团.csv', r'.\data\国家能源集团.csv')
        else:
            print('网站没有更新')




def go_to():
    try:
        c = spider_1()
        c.run_()
    except Exception as e:
        note.log(note.log_time()+'sp_1出现问题，错误:'+str(e)+'\n')


