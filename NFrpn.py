import math

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def truediv(a,b):
  return a/b

def xeq_sqrt(a):
  return math.sqrt(a)

two_p = {
	'+': add,
	'-': sub,
	'*': mul,
	'/': truediv
	}

one_p = {
	'sqrt()': xeq_sqrt
}

def max4(stack):
	if len(stack)>4:
	  del stack[0]

def eval_expression(tokens, stack):
  for token in tokens:
    if set(token).issubset(set("-0123456789")):
      stack.append(int(token))
      max4(stack)
    elif set(token).issubset(set("-0123456789.")):
      stack.append(float(token))
      max4(stack)
    elif token in two_p:
      if len(stack) < 2:
        raise ValueError('Must have at least two parameters to perform op')
      a = stack.pop()
      b = stack.pop()
      op = two_p[token]
      stack.append(op(b,a))
    elif token in one_p:
    	a = stack.pop()
    	op = one_p[token]
    	stack.append(op(a))
    else:
      raise ValueError("WTF? %s" % token)
  return stack

def rolldown(stack):
	pop_reg = stack.pop()
	stack.insert(0,pop_reg)

def rollup(stack):
  push_reg = stack.pop(0)
  stack.insert(-1,push_reg)

def swap(stack):
  swap_reg = stack.pop()
  stack.insert(-2,swap_reg)

def disp_stack(stack):
  if len(stack)>3:
    print('T:{:>12}'.format(stack[0]))
    print('Z:{:>12}'.format(stack[1]))
    print('Y:{:>12}'.format(stack[2]))
    print('X:{:>12}'.format(stack[3]))
  elif len(stack)>2:
    print('\n')
    print('Z:{:>12}'.format(stack[0]))
    print('Y:{:>12}'.format(stack[1]))
    print('X:{:>12}'.format(stack[2]))
  elif len(stack)>1:
    print('\n')
    print('\n')
    print('Y:{:>12}'.format(stack[0]))
    print('X:{:>12}'.format(stack[1]))
  else:
    print('\n')
    print('\n')
    print('\n')
    print('X:{:>12}'.format(stack[0]))


def main():
  stack = []
  while True:
    expression = input('> ')
    if expression in ['quit','q','exit']:
      quit()
    elif expression in ['clear','empty']:
      stack = []
      continue
    elif expression in ['rd']:
    	rolldown(stack)
    	disp_stack(stack)
    	continue
    elif len(expression)==0:
      continue
    stack = eval_expression(expression.split(), stack)
    disp_stack(stack)
    print(expression)
    
if (__name__ == '__main__')\
or(__name__ == 'NFrpn'):
	main()
