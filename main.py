import time
import threading
from configparser import ConfigParser
import sp_1
import sp_2
import sp_3
import sp_4
import sp_5
import sp_6
from note import log_time


def load_config():
    cfg = ConfigParser()
    cfg.read('config.ini', encoding='utf-8')
    return float(cfg.get('cfg', 'frequency'))


class dynamic_state_spider:
    def __init__(self, *args, **kwargs):
        self.hour_S = 3600
        self.config = load_config()
        self.run_time = time.time()

    def time_detection(self):
        while True:
            time.sleep(5)
            time_to = time.time() - self.run_time
            print('Resources start fetching after %.2fs' % (self.hour_S * self.config - time_to))
            if time_to >= (self.config * self.hour_S):
                print(log_time() + ' run:spider')
                self.run_time = time.time()
                self.run()

    def run(self):
        f = open('.\\log.txt', 'a', encoding='utf-8')
        f.write(log_time() + ' run : all spider\n')
        f.close()
        thread_list = [threading.Thread(target=sp_1.go_to), threading.Thread(target=sp_2.go_to),
                       threading.Thread(target=sp_3.go_to), threading.Thread(target=sp_4.go_to),
                       threading.Thread(target=sp_5.go_to), threading.Thread(target=sp_6.go_to)]
        for i in thread_list:
            i.start()
        for i in thread_list:
            i.join()


c = dynamic_state_spider()
c.time_detection()
