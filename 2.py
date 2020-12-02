#1 
def f(x):
   return x**2 - 2


def func(f, a, b, accuracy = 0.00001):
   while abs(b - a) > accuracy:
      x = (a + b)/2
      fx = f(x)
      fa = f(a)
      if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
         a = x
      else:
         b = x
   return x

x = func(f, 0, 5)
print(x)

