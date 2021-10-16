#  importing necessary modules


import time
from win10toast import ToastNotifier
import datetime
  
  #  setting up reminder 


def getTimeInput():

    print("what to remind?")
    hour = int(input("hours of interval :"))
    minutes = int(input("Mins of interval :"))
    seconds = int(input("Secs of interval :"))
    time_interval = seconds+(minutes*60)+(hour*3600)
    return time_interval
  
  #  writes into .txt 


def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
        f.write(f"You did task  {now} \n")
    return 0
  
  
def notify():
    notification = ToastNotifier()
    notification.show_toast("Time to od task")
    log()
    return 0
  
  
def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        notify()
  
  
if __name__ == '__main__':
    time_interval = getTimeInput()
    starttime(time_interval)