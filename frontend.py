import time
import threading

exitFlag = 0
elapsedTime = 1

class threadElement (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      timeCounter()
      print ("Exiting " + self.name)

def timeCounter():
    currentTime = time.perf_counter();
    while True:
        if (time.perf_counter() - currentTime) > elapsedTime:
            currentTime = time.perf_counter();
            print("WOWIE")

def startFrontEnd():
    pomodoroThread = threadElement(1, "Thread-1", 1)

    print("thread created")
    pomodoroThread.start()
    print("Thread Started")
