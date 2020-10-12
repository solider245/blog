一个 多线程爬视频的 py 脚本,我想看下总的执行时间,求大佬帮忙看看???

```

# -*- coding: utf-8 -*-
# @Author : 徐燚敏
# @File : movie_multiple.py
# @Project: python_spider
# @CreateTime : 2020-06-22 10
# encoding utf-8
import requests
from queue import Queue
import threading
import time

start_total_time = 0
end_total_time = 0
# 创建线程 生产者负责获取 URL，并且解析 URL
class Procuder(threading.Thread):

    def __init__(self, num_queue, ts_queue, *args, **kwargs):
        super(Procuder, self).__init__(*args, **kwargs)
        self.num_queue = num_queue
        self.ts_queue = ts_queue

    def run(self):
        while True:
            if self.num_queue.empty():
                # 如果队列为空就，线程执行完成，跳出死循环，结束 run
                print("Procuder 队列为空")
                break
            url = self.num_queue.get()
            self.download_ts(url)

    def download_ts(self, url):
        r = requests.get(url)
        ret = r.content
        # 倒数 8 位,取到文件名
        filename = url[-8:]
        self.ts_queue.put((ret, filename))

# 创建线程 消费者 负责下载
class Consumer(threading.Thread):

    def __init__(self, num_queue, ts_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.num_queue = num_queue
        self.ts_queue = ts_queue

    def run(self):
        while True:
            if self.ts_queue.empty() and self.num_queue.empty():
                # 如果队列为空就，线程执行完成，跳出死循环，结束 run
                print("Consumer 队列为空")
                end_total_time = time.time()
                break
            start_time = time.time()
            ret, filename = self.ts_queue.get()
            # 将 ts 文件保存到文件夹里
            with open('./mp4/{}'.format(filename), 'wb') as f:
                f.write(ret)
            end_time = time.time()
            print('{}下载完成!,耗时:{}'.format(filename,end_time - start_time) )

def main():

    # 定义线程
    num_queue = Queue(500)
    ts_queue = Queue(500)
    # 先自定义好总共爬取的数量
    # for i in range(470):
    for i in range(30):
        url = " https://us8.wl-cdn.com/hls/20200619/e1c5cc36967e6dac688b5e9c4006a567/film_" + '{0:05d}'.format(i) + ".ts"
        num_queue.put(url)

    # time.sleep(1)
    # 定义生产者
    for x in range(5):
        print("Procuder")
        t = Procuder(num_queue, ts_queue)
        t.start()
    # 定义消费者
    for x in range(5):
        print("Consumer")
        t = Consumer(num_queue, ts_queue)
        t.start()

if __name__ == '__main__':
    start_total_time = time.time()
    lock = threading.RLock()
    # 加锁
    lock.acquire()
    try:
        main()
    finally:
        # 修改完成，释放锁
        lock.release()
        print("完成下载,总耗时{}".format(end_total_time - start_total_time))
```