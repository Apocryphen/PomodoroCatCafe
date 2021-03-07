import time
import threading

exitFlag = 0
currentTime = 0
currentTime = time.perf_counter();
elapsedTime = 1

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      timeCounter()
      print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

def timeCounter():
    currentTime = time.perf_counter();
    while True:
        if (time.perf_counter() - currentTime) > elapsedTime:
            currentTime = time.perf_counter();
            print("WOWIE")


thread1 = myThread(1, "Thread-1", 1)

print("thread created")
#thread1.start()
print("Thread Started")
