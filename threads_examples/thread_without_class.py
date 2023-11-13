import threading
from threading import Thread

def worker(number):
    print ('I am thread: ' + str(number) + '\n')


thread = threading.Thread(target=worker, args=(i,))
thread.start()