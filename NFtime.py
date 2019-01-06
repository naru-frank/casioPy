import math

def hms2s(time):
  h = math.floor(time/10000)
  time = time-h*10000
  m = math.floor(time/100)
  time = time-m*100
  s = time
  total1 = h*3600+m*60+s
  return total1

def s2hms(ans):
	h2 = math.floor(ans/3600)
	ans = ans-h2*3600
	m2 = math.floor(ans/60)
	ans = ans-m2*60
	s2 = ans
	total2 = h2*10000+m2*100+s2
	total2 = total2/10000
	total2 = '{:.4f}'.format(total2)
	return total2
	
def calc(t1,t2,op):
	if op == '+':
		result = hms2s(t1)+hms2s(t2)
	if op == '-':
		result = hms2s(t1)-hms2s(t2)
	result = s2hms(result)
	return result
	
time1 = int(float(input('HH.MMSS?'))*10000)
time2 = int(float(input('time2?'))*10000)
operator = input('+ or -?')
print(calc(time1,time2,operator))


