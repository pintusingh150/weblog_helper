import pandas as pd
import requests
from datetime import datetime
import pytz
import io


LOG_ENDPOINT = "https://s3.amazonaws.com/syseng-challenge/public_access.log.txt"
LOG_FILE = ""

log_content = requests.get(LOG_ENDPOINT).text

def parse_str(x):
    return x[1:-1]

def parse_datetime(x):
    dt = datetime.strptime(x[1:-7], '%d/%b/%Y:%H:%M:%S')
    dt_tz = int(x[-6:-3])*60+int(x[-3:-1])
    return dt.replace(tzinfo=pytz.FixedOffset(dt_tz))

def read_log_data():
    data = pd.read_csv(
        io.StringIO(log_content),
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
        engine='python',
        na_values='-',
        header=None,
        usecols=[0, 3, 4, 5, 6, 7, 8],
        names=['ip', 'time', 'request', 'status', 'size', 'referer', 'user_agent'],
        converters={'time': parse_datetime,
                    'request': parse_str,
                    'status': int,
                    'size': int,
                    'referer': parse_str,
                    'user_agent': parse_str})
    
    return data

    