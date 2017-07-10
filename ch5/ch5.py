## Conditionals and recursion

import time

unix_time = time.time()

def print_time(unix):
    days = unix / 60 / 60 / 24
    print(int(days), 'days since 1 January 1970')

    seconds_in_day =  24 * 60 * 60


print_time(unix_time)