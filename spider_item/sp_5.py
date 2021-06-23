# 中国三峡
# http://rms.chinahr.com/api/news/all?token=00032eac-7ff4-451b-9e19-480954155547
import csv
import shutil
import requests
import random
import header
import json
import time

import note


class spider_5:

    def __init__(self, *args, **kwargs):
        self.big_data = []
        self.url = 'http://rms.chinahr.com/api/news/all?token=00032eac-7ff4-451b-9e19-480954155547'
        self.headers = {
            'User-agent': random.choice(header.USER_AGENTS),  # 设置get请求的User-Agent，用于伪装浏览器UA
        }

    def run_(self):
        req = requests.get(self.url, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        data_dict = json.loads(html)
        for i in data_dict['retMsg']:
            if i['type'] == '招聘公告':

                title = i['title']
                time_ = i['startTime']
                if title == '':
                    continue
                if i['startTime'] is None:
                    time_ = '未知'
                else:
                    time_ = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(i['startTime'] / 1000)))
                item_dict = {'title': title, 'time': time_}
                self.big_data.append(item_dict)
        print("sp_5 data_num:"+str(len(self.big_data)))
        self.save_file()

    def save_file(self):
        with open(r'.\data_temp\中国三峡.csv', 'w', newline='', encoding='GBK') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['title', 'date'])
            for i in self.big_data:
                writer.writerow([i['title'], i['time']])
            csv_file.close()
        if not header.file_same(r'.\data_temp\中国三峡.csv',r'.\data\中国三峡.csv'):
            note.run_note('<big>中国三峡更新了，快来看看！</big>')
            note.log('sp_5:网站已更新\n')
            shutil.copyfile(r'.\data_temp\中国三峡.csv', r'.\data\中国三峡.csv')
        else:
            print('网站没有更新')


def go_to():
    try:
        c = spider_5()
        c.run_()
    except Exception as e:
        note.log(note.log_time()+'sp_5出现问题，错误:' + str(e) + '\n')

