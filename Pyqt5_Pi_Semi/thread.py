import threading
import time

# 定义一个线程子类
class CountThread(threading.Thread):
    def __init__(self, name, count_to):
        threading.Thread.__init__(self)
        self.name = name
        self.count_to = count_to

    def run(self):
        print(f"线程 '{self.name}' 启动")
        for i in range(1, self.count_to + 1):
            print(f"线程 '{self.name}' : {i}")
            time.sleep(1)
        print(f"线程 '{self.name}' 完成")

# 创建线程实例
thread1 = CountThread("Thread 1", 5)
thread2 = CountThread("Thread 2", 3)

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

print("主线程结束")
