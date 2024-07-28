

# https://www.hackerrank.com/challenges/time-conversion/problem

import re
def dateconverter(s):
    comps = re.compile(r'\d\d|AM|PM')
    parts = comps.findall(s)

    if parts[3] == 'PM':
        x = int(parts[0])+12
        y = str(x)
        del(parts[0])
        parts.insert(0, y)

    answer = parts[0]+':'+parts[1]+":"+parts[2]
    return answer


list1 = ['07:05:45PM', '07:05:45AM',
'10:12:24:AM',
'10:12:24:PM',
'12:12:24:AM',
'12:12:24:PM',
'01:05:45PM',
'02:05:45AM',
         '00:12:24:PM',
         '01:05:45PM',
         '00:05:45AM',
         ]

for i in list1:
    print((dateconverter(i)))
















