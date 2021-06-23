# 中国华电集团
import csv
import shutil

import requests
import random
import header
import json
import time

import note


class spider_4:

    def __init__(self, *args, **kwargs):
        self.big_data = []
        self.url = "http://www.chd.com.cn/nodejsService/articleListSearch/?callback=jQuery191010481630463705138_1624114102630&website_id=c802da7172754e8f8a3fc3bc02d7bfd7&perPage=20&startNum=(page)" \
                   "&oc=2&_=1624114102631"
        self.headers = {
            'User-agent': random.choice(header.USER_AGENTS),  # 设置get请求的User-Agent，用于伪装浏览器UA
        }

    def run_(self):
        j = 1
        while True:
            time.sleep(1)
            req = requests.get(self.url.replace('(page)', str(j)), headers=self.headers, timeout=10)
            req.encoding = 'utf-8'
            html = req.text[req.text.find('(') + 1:-1]
            if html == '[]':
                print('结束！')
                break
            data_dict = json.loads(html)
            for i in data_dict:
                item_dict = {'title': i['TITLE'], 'date': i['RELEASE_DATE']}
                self.big_data.append(item_dict)
            j += 1
        print("sp_4 data_num:"+str(len(self.big_data)))
        self.save_file()

    def save_file(self):
        with open(r'.\data_temp\中国华电集团.csv', 'w', newline='', encoding='GBK') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['title', 'date'])
            for i in self.big_data:
                writer.writerow([i['title'], i['date']])
            csv_file.close()
        if not header.file_same(r'.\data_temp\中国华电集团.csv',r'.\data\中国华电集团.csv'):
            note.run_note('<big>中国华电集团更新了，快来看看！</big>')
            note.log('sp_4:网站已更新\n')
            shutil.copyfile(r'.\data_temp\中国华电集团.csv', r'.\data\中国华电集团.csv')
        else:
            print('网站没有更新')


def go_to():
    try:
        c = spider_4()
        c.run_()
    except Exception as e:
        note.log(note.log_time()+'sp_4出现问题，错误:' + str(e) + '\n')

