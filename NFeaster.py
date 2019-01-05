import math

current_year = input('year?>')
y = int(current_year)
g = y%19
c = math.floor(y/100)
k = math.floor((c-17)/25)
h = (19*g+15+c-math.floor(c/4)-math.floor((c-k)/3))%30
i = h-math.floor(h/28)*(1-math.floor(29/(h+1)))*(math.floor((21-g)/11))
j = (y+math.floor(y/4)-c+math.floor(c/4)+i+2)%7
l = i-j
m = 3+math.floor((l+40)/44)
d = l+28-31*math.floor(m/4)
print(y,m,d)
