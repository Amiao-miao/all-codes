from threading import Thread
from time import sleep

class myThread(Thread):
    def __init__(self, song):
        self.song=song
        super().__init__()

    def run(self):
        for i in range(3):
            sleep(2)
            print(f"播放:{self.song}")
my_thread=myThread("黄河大合唱")
my_thread.start()
my_thread.join()