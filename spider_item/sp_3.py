# 中国大唐集团
import csv
import shutil
import requests
import random
import header
from bs4 import BeautifulSoup
import time

import note

data = {'__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': r'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',
        '__VIEWSTATEGENERATOR': '38DA7B24',
        '__EVENTVALIDATION': r'/wEdAAqth+RC8FZgChhLsyUgcqpYLYiKcf3VjDoMsj0b1FNslWUztZAzeswRKnahCURKq35QY'
                             r'/r2AzkJYMlcw1Cc3OAVSGsNsrb90Ynhta+JBnQpBKJmRSf+h3k9qEU4DrjV47t3bQTKjGPu8u9RVuAkYoq7L'
                             r'/e73HGPa2Tjyte80AaHJAsnqOMwEuRGYGf0hZft4tnWcILCMppSm6az2fgmS+jZa1xjC5QreH'
                             r'/yQ4NmsyNAciSI4CgVi4u9tGsU2Eq09QY=',
        'ctl00$hfRoot': r'/cdtrw',
        'ctl00$MainContent$BringListControl1$HdPageIndexGrad': '1',
        'ctl00$MainContent$BringListControl1$EPager$txtCurrentPage': '1',
        'ctl00$MainContent$BringListControl1$EPager$lbtnNext': '',
        'ctl00$MainContent$BringListControl1$hfReType': '2'}


class spider_3:

    def __init__(self, *args, **kwargs):
        self.big_data = []
        self.url = "http://www.cdtrczp.com/cdtrw/NewsCenter.aspx?Type=3"
        self.headers = {
            'User-agent': random.choice(header.USER_AGENTS),  # 设置get请求的User-Agent，用于伪装浏览器UA
        }
        self.page = self.get_page()

    def get_page(self):
        req = requests.post(self.url, data=data, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        page = soup.find('span', id='ctl00_MainContent_BringListControl1_EPager_lblPageCount').text
        page = page[1:page.find('页')]
        return int(page)

    def run_(self):
        # page
        for j in range(self.page):
            time.sleep(1)
            data['ctl00$MainContent$BringListControl1$EPager$txtCurrentPage'] = str(j)
            req = requests.post(self.url, data=data, headers=self.headers)
            req.encoding = 'utf-8'
            html = req.text
            soup = BeautifulSoup(html, 'lxml')
            time_ = soup.find_all('td', class_='sp2')
            title = soup.find_all('td', class_='sp1')
            for i in range(len(title)):
                item_dict = {'title': ''.join(str(title[i].text).split()), 'time': ''.join(str(time_[i].text).split())}
                self.big_data.append(item_dict)
        print("sp_3 data_num:"+str(len(self.big_data)))
        self.save_file()

    def save_file(self):
        with open(r'.\data_temp\中国大唐集团.csv', 'w', newline='', encoding='GBK') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['title', 'date'])
            for i in self.big_data:
                writer.writerow([i['title'], i['time']])
            csv_file.close()
        if not header.file_same(r'.\data_temp\中国大唐集团.csv', r'.\data\中国大唐集团.csv'):
            note.run_note('<big>中国大唐集团更新了，快来看看！</big>')
            note.log('sp_3:网站已更新\n')
            shutil.copyfile(r'.\data_temp\中国大唐集团.csv', r'.\data\中国大唐集团.csv')
        else:
            print('网站没有更新')

def go_to():
    try:
        c = spider_3()
        c.run_()
    except Exception as e:
        note.log(note.log_time()+'sp_3出现问题，错误:' + str(e) + '\n')

