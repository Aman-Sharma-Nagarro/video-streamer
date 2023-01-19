from time import time, sleep

class Camera(object):
    def __init__(self):
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        with open('videoplayback.mp4', 'rb') as f:
            frame = f.read(1024)
            while frame:
                yield frame
        # start_time = time()
        # interval = 0.5
        # sleep(start_time + interval - time())
        # print(int(time()) % 3)
        # return self.frames[int(time()) % 3]

    def complex_logic(n: int):
        return n*n

    def business_logic(n: str, t: int):
        return n * t