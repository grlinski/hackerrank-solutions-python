

import datetime
from datetime import datetime

def createTime(t1,t2):


    format = '%a %d %b %Y %H:%M:%S %z'


    time1 = int(datetime.strptime(t1, format).timestamp())
    time2 = int(datetime.strptime(t2, format).timestamp())
    print(time1-time2)



amt = int(input())
for i in range(amt):
    t1 = input()
    t2 = input()
    createTime(t1,t2)























