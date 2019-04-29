import datetime


def log(msg):
    print(str(datetime.datetime.now().strftime("%H:%M:%S")) + ": " + msg)