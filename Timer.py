import time
class Timer():
    def update(self,wantedtime,func,args):
        btime = time.time()
        dow = True
        while dow:
            endtime = time.time() - btime
            if int(endtime) == wantedtime:
                func(*args)
                dow = False
