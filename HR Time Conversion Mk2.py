
import random


def timeConversion(s):
    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]
    AMPM = s[8:11]
    answer = ""
    if AMPM == "PM" and hour == '12':
        hour = str(int(s[0:2]))
    elif AMPM == "PM":
        hour = str(int(s[0:2])+12)
    elif AMPM == 'AM' and hour == '12':
        hour = '00'


    answer=hour+":"+minute+":"+ second



    return answer


def date_gen():
    hour = str(random.randint(0,12))
    minute = str(random.randint(0, 60))
    second = str(random.randint(0,60))
    day = random.randint(0,1)
    if day == 0:
        AMPM = "AM"
    else:
        AMPM = 'PM'
    if len(hour) == 1:
        hour = '0'+hour
    if len(minute) == 1:
        minute = '0'+minute
    if len(second) == 1:
        second = '0'+second
    ans = hour+":"+minute+":"+second+AMPM
    return ans



#x = date_gen()
#x = '12:15:30AM'
#00:15:30

# 12:45:54PM
# 12:45:54
x = '12:45:54PM'



print(x)


print(timeConversion(x))




