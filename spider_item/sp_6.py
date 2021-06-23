# 中国电力公司投资集团
# http://www.spic.com.cn/2018rlzy/zpxx/index.html
import csv
import shutil

from selenium.webdriver import Chrome
import time

import header
import note


def run_():
    big_data = []
    brower = Chrome(executable_path=r'.\chromedriver.exe')
    url = 'http://www.spic.com.cn/2018rlzy/zpxx/index.html'
    brower.get(url)
    while True:
        data = brower.find_elements_by_xpath('//ul[@class="textcontent subpagelist"]/li')
        for i in data:
            line = ''.join(str(i.text).split())
            data_dict = {'title': line[:line.index('日期')], 'time': line[line.index('日期') + 3:]}
            big_data.append(data_dict)
        time.sleep(1)
        try:
            brower.find_element_by_xpath("//a[text()='下一页']").click()
        except Exception as e:
            break
    brower.close()
    save_file(big_data)


def save_file(big_data):
    with open(r'.\data_temp\中国电力公司投资集团.csv', 'w', newline='', encoding='GBK') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['title', 'date'])
        for i in big_data:
            writer.writerow([i['title'], i['time']])
        csv_file.close()
    if not header.file_same(r'.\data_temp\中国电力公司投资集团.csv', r'.\data\中国电力公司投资集团.csv'):
        note.run_note('<big>国家能源集团更新了，快来看看！</big>')
        note.log('sp_6:网站已更新\n')
        shutil.copyfile(r'.\data_temp\中国电力公司投资集团.csv', r'.\data\中国电力公司投资集团.csv')
    else:
        print('网站没有更新')


def go_to():
    try:
        run_()
    except Exception as e:
        note.log(note.log_time() + 'sp_6出现问题，错误:' + str(e) + '\n')
