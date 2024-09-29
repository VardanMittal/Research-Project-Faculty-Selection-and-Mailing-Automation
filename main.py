from mail import mailSender
from trigger import trigger
from data_fetch import data

ZONE = "CET"

if __name__ == "__main__":
    time = trigger(ZONE)
    indian = time[1]
    foreign = time[0]