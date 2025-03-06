from datetime import datetime
import pytz

time_Moscow = pytz.timezone('Europe/Moscow')
datetime_M = datetime.now(time_Moscow)
print('Moscow date and time: ', datetime_M.strftime('Date: %d-%m-%Y, Time: %H:%M:%S'))
