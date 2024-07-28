
import time
from datetime import datetime

#t1 = input()
#t2 = input()

Day = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
Month = ['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']

t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'

from datetime import datetime
pattern = '%a %d %b %Y %H:%M:%S %z'
epoch1 = int(datetime.strptime(t1,pattern).timestamp())
epoch2 = int(datetime.strptime(t2,pattern).timestamp())
diff=epoch1-epoch2
print(str(abs(diff)))







