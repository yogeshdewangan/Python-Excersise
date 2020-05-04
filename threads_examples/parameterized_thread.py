import threading

class myThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):
        print("Thread name is :" + self.thread_name)


thread1 = myThread("First Thread")
thread1.start()