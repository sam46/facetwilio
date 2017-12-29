from multiprocessing import Process, Pipe
from fb2twilio import run as runF2T
from twilio2fb import run as runT2F


if __name__ == '__main__':
    Process(target=runF2T, args=()).start()
    Process(target=runT2F, args=()).start()
    print 'Facetwilio active...'
