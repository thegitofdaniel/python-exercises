def fib(n):
  x = 1
  x0 = 0
  x1 = 1
  while x < n:
    #print(x0)
    x0, x1 = x1, x1 + x0
    x = x + 1
  print(x0)
