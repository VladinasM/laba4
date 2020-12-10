#1 
def f(x):
   return x**2 - 2


def func(f, a, b, accuracy):
   while abs(b - a) > accuracy:
      x = (a + b)/2
      fx = f(x)
      fa = f(a)
      if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
         a = x
      else:
         b = x
   return x

t = func(f, 0, 5, 0.001)
print(t)















def f(x):
    return x ** 2 - 2


def bis_method(a, b, accuracy):
    global x
    if f(a)*f(b) <= 0:
        if (b - a)/2.0 > accuracy:
            x = (a + b)/2.0
        if f(a)*f(x) < 0:
            a = x
        else:
            b = x
            return bis_method(a, b, accuracy)
    return x

print("Ответ:", bis_method(0, 5, 0.0001))

