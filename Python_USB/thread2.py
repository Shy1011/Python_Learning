import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(1.5)

# 创建线程
number_thread = threading.Thread(target=print_numbers)
letter_thread = threading.Thread(target=print_letters)

# 启动线程
number_thread.start()
letter_thread.start()
"""
这段代码展示了如何在Python中使用threading模块创建和启动线程。
在Python中，线程是通过创建Thread对象来实现的，这个对象在被创建时可以指定要执行的目标函数（通过target参数）。
然后，通过调用这个Thread对象的start()方法来启动线程，这会导致Python在一个单独的流程中执行目标函数。
"""

##############################################
import threading
import time

class StoppableThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        while not self.stopped():
            print("线程正在运行...")
            time.sleep(1)
        print("线程结束")

# 创建并启动线程
my_thread = StoppableThread()
my_thread.start()

# 运行一段时间后停止线程
time.sleep(5)
my_thread.stop() # 停止这个线程

