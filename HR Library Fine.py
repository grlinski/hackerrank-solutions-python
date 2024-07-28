
# Library Fine
# https://www.hackerrank.com/challenges/library-fine/problem

def libraryFine(d1, m1, y1, d2, m2, y2):
    dd = d2-d1
    md = m2-m1
    yd = y2-y1


    tm = 0

    if yd == 0:
        pass
    else:
        tm = (yd*12)-md
        return tm*500+dd*




    print(dd,md,yd)









d1,m1,y1 = 9,6,2015
d2,m2,y2 = 6,6,2015




libraryFine(d1, m1, y1, d2, m2, y2)




