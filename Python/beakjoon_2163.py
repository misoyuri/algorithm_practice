import sys
import datetime

if __name__ == '__main__':
    cur_time = datetime.datetime.now() + datetime.timedelta(hours=9)
    print("{}-{}-{}".format(cur_time.year, cur_time.month, cur_time.day))
    
    