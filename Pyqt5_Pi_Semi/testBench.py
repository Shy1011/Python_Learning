import threading

# 共享资源
counter = 0

# 乒乓算法实现的线程函数
def ping():
    global counter
    for _ in range(5):
        counter += 1
        print("Ping: Counter =", counter)

# 乒乓算法实现的线程函数
def pong():
    global counter
    for _ in range(5):
        counter -= 1
        print("Pong: Counter =", counter)

# 创建两个线程并启动
thread1 = threading.Thread(target=ping)
thread2 = threading.Thread(target=pong)
thread1.start()
thread2.start()

# 等待两个线程结束
thread1.join()
thread2.join()

print("Final Counter:", counter)
