# 中国华能集团
import csv
import shutil

import requests
import random
import header
from bs4 import BeautifulSoup
import time

import note


def str_int(str_i):
    try:
        int(str_i)
        return True
    except:
        return False


class spider_2:

    def __init__(self, *args, **kwargs):
        self.big_data = []
        self.url = "https://www.chng.com.cn/list_zpxx/-/article/cQQKaBtwslFy/list/23524/(page).html"
        self.headers = {
            'User-agent': random.choice(header.USER_AGENTS),  # 设置get请求的User-Agent，用于伪装浏览器UA
        }
        self.page = self.get_page()

    def get_page(self):
        req = requests.get(self.url.replace('(page)', '1'), headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        item_all = soup.find('div', class_='layui-box layui-laypage layui-laypage-default')
        return int(item_all.find_all('a')[-2].text)

    def run_(self):
        for j in range(self.page):
            time.sleep(1)
            req = requests.get(self.url.replace('(page)', str(j)), headers=self.headers)
            req.encoding = 'utf-8'
            html = req.text
            soup = BeautifulSoup(html, 'lxml')
            item_all = soup.find_all('div', class_='news-list-item')
            for i in item_all:
                item = list(set(i.text.split(' ')))
                try:
                    del item[item.index('')]
                except:
                    pass
                try:
                    del item[item.index('微信扫描二维码')]
                except:
                    pass

                while len(item) > 3:
                    k = 0
                    len_k = 0
                    for j in range(len(item)):
                        if len(str(item[j])) > len_k:
                            k = j
                            len_k = len(str(item[j]))
                    del item[k]
                item_dict = {}
                for k in range(len(item)):
                    if str_int(item[k]):
                        item_dict['day'] = item[k]
                    elif len(item[k]) > 10:
                        item_dict['title'] = item[k]
                    else:
                        item_dict['date'] = item[k]
                self.big_data.append(item_dict)
        print("sp_2 data_num:"+str(len(self.big_data)))
        self.save_file()

    def save_file(self):
        with open(r'.\data_temp\中国华能集团.csv', 'w', newline='', encoding='GBK') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['title', 'date'])
            for i in self.big_data:
                try:
                    writer.writerow([i['title'], i['date'] + '-' + i['day']])
                except:
                    pass
            csv_file.close()
            if not header.file_same(r'.\data\中国华能集团.csv', r'.\data_temp\中国华能集团.csv'):
                note.run_note('<big>中国华能集团更新了，快来看看！</big>')
                note.log('sp_2:网站已更新\n')
                shutil.copyfile(r'.\data_temp\中国华能集团.csv',r'.\data\中国华能集团.csv')
            else:
                print('网站没有更新')


def go_to():
    try:
        c = spider_2()
        c.run_()
    except Exception as e:
        note.log(note.log_time()+'sp_2出现问题，错误:' + str(e) + '\n')


