from datetime import datetime
import pytz


def struct(time):
    return {
        "date":time.date(),
        "hr":time.time().hour,
        "min":time.time().minute
    }
def trigger(zone):
    indian_timezone = pytz.timezone('Asia/Kolkata')
    indian_time = datetime.now(indian_timezone)
    foreign_timezone = pytz.timezone(zone)
    foreign_time = indian_time.astimezone(foreign_timezone)
    return [struct(foreign_time), struct(indian_time)]