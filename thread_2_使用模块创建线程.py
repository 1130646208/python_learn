#我们可以通过直接从 threading.Thread 继承创建一个新的子类，
#并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    
    def __init__(self, threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name=name
        self.counter = counter
            
    def run(self):
        
        print("开始线程："+self.name)
        print_time (self.name,self.counter,5)
        print("退出线程："+self.name )

def print_time(threadName,delay,counter):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print("%s:%s"%(threadName,time.ctime(time.time())))
            counter -= 1
    

thread1 = myThread(1,"Thread_1",1)
thread2 = myThread(2,"Thread_2",2)
#start new thread
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("退出主线程")
