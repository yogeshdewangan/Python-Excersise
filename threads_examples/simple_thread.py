import threading

class myThread(threading.Thread):

    def run(self):
        print("starting thread")

thread1 = myThread()
thread1.start()



