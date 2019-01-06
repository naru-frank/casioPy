# module
import math

#global vars
stack = []

# 2 parameters command
two_p = ['+','-','*','/','**']

def calc2(a,b,cmd):
  if cmd == '+':
    ans = b+a
  elif cmd == '-':
    ans= b-a
  elif cmd == '*':
    ans = b*a
  elif cmd == '/':
    ans = b/a
  elif cmd == '**':
    ans = b**a
  return ans

# 1 parameter command
one_p = [
	'sqrt()',
  '**2',
  'log10()',
  'log()',
  'exp()',
  'sin()',
  'asin()',
  'cos()',
  'acos()',
  'tan',
  'atan',
  '**-1'
  ]

def calc1(a,cmd):
  if cmd == 'sqrt()':
    ans = math.sqrt(a)
  if cmd == '**2':
    ans = a**2
  if cmd == 'log10()':
    ans = math.log10(a)
  if cmd == 'log()':
    ans = math.log(a)
  if cmd == 'exp()':
    ans = math.exp(a)
  if cmd == 'sin()':
    ans = math.sin(a)
  if cmd == 'asin()':
    ans = math.asin(a)
  if cmd == 'cos()':
    ans = math.cos(a)
  if cmd == 'acos()':
    ans = math.acos(a)
  if cmd == 'tan()':
    ans = math.tan(a)
  if cmd == 'atan()':
    ans = math.atan(a)
  if cmd == '**-1':
    ans = a**-1
  return ans

# Registers
def max4(stack):
	if len(stack)>4:
	  del stack[0]

def rolldown(stack):
	pop_reg = stack.pop()
	stack.insert(0,pop_reg)
	disp_stack(stack)

def rollup(stack):
  push_reg = stack.pop(0)
  stack.insert(-1,push_reg)
  disp_stack(stack)

def swap(stack):
  swap_reg = stack.pop()
  stack.insert(-2,swap_reg)
  disp_stack(stack)

def disp_stack(stack):
  if len(stack)==4:
    print('T:{:>12}'.format(stack[0]))
    print('Z:{:>12}'.format(stack[1]))
    print('Y:{:>12}'.format(stack[2]))
    print('X:{:>12}'.format(stack[3]))
  elif len(stack)==3:
    print('\n')
    print('Z:{:>12}'.format(stack[0]))
    print('Y:{:>12}'.format(stack[1]))
    print('X:{:>12}'.format(stack[2]))
  elif len(stack)==2:
    print('\n')
    print('\n')
    print('Y:{:>12}'.format(stack[0]))
    print('X:{:>12}'.format(stack[1]))
  elif len(stack)==1:
    print('\n')
    print('\n')
    print('\n')
    print('X:{:>12}'.format(stack[0]))
  else:
  	print('Hello!/Saluton!')

def clear_stack():
  global stack
  stack = []

cmd = {
	'q':'quit()',
	'quit':'quit()',
	'exit':'quit()',
	'clear':'clear_stack()',
	'rd':'rolldown(stack)',
  'ru':'rollup(stack)',
  'sw':'swap(stack)'
}

#operations
def eval_expression(tokens, stack):
  for token in tokens:
    if set(token).issubset(set("0123456789")):
      stack.append(int(token))
      max4(stack)
    elif set(token).issubset(set("0123456789.")):
      stack.append(float(token))
      max4(stack)
    elif token in two_p:
      if len(stack) < 2:
        raise ValueError('Must have at least two parameters to perform op')
      a = stack.pop()
      b = stack.pop()
      stack.append(calc2(a,b,token))
    elif token in one_p:
    	a = stack.pop()
    	stack.append(calc1(a,token))
    elif token in cmd:
    	print(token+' is done!/estas farita!')
#    else:
#      raise ValueError("WTF? %s" % token)
  return stack

def main():
#  stack = []
  global stack
  while True:
    expression = input('> ')
    if expression in cmd:
    	eval(cmd[expression])
    	continue
    elif len(expression)==0:
      continue
    expression = expression.replace(',',' ')
    stack = eval_expression(expression.split(), stack)
    disp_stack(stack)
    print(expression)

if (__name__ == '__main__')\
or(__name__ == 'NFrpn'):
	main()
