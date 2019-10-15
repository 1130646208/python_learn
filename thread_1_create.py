import _thread
import time
#为线程定义函数
def print_time(threadName, delay):
    count = 0
    while count < 5 :
        time.sleep(delay)
        #count += 1
        print("%s: %s"% (threadName, time.ctime(time.time())) )

#创建两个线程

try:
    _thread.start_new_thread( print_time, ("thread-1",2))
    _thread.start_new_thread( print_time, ("thread-2",3))
except:
    print("error!")



while 1:
    pass
