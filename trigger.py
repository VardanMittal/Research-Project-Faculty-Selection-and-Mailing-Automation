from datetime import datetime
import pytz

def trigger(zone):
    indian_timezone = pytz.timezone('Asia/Kolkata')
    indian_time = datetime.now(indian_timezone)
    foreign_timezone = pytz.timezone(zone)
    foreign_time = indian_time.astimezone(foreign_timezone)
    return foreign_time.time().hour
