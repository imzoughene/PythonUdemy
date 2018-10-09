import _thread
import time
def CounterDown(ThreadName):
    counter=10
    while(counter>=0):
        print("{},Count : {}".format(ThreadName,counter))
        counter-=1
        time.sleep(2)
def main():
    try:
        _thread.start_new_thread(CounterDown,("Thread1",))
        _thread.start_new_thread(CounterDown,("Thread2",))

    except:
        print("Error unable to start thread ")
    while 1:
        pass
if __name__ == '__main__':main()
