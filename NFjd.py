from math import *

date=float(input('YYYY.MMDD?'))
y=floor(date)
m=floor((date-y)*100)
d=floor((date-y)*10000-m*100)
if m<3:
  y=y-1
  m=m+12
y1=floor(365.25*y)
y2=floor(y/400)
y3=floor(y/100)
m1=floor(30.59*(m-2))
mjd=y1+y2-y3+m1+d-678912
print(mjd)