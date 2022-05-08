import random

def rollDice(min_value,max_value):
  roll = random.randint(min_value,max_value)
  if roll != 0:
    roll = 1/roll
  else:
    answer = 0
  return roll

def montecarlo(rep,min_value,max_value):
  round = 0
  sum = 0
  while round < rep:
    x = rollDice(min_value,max_value)
    sum = sum + x
#print(result,round/rep*100,"%")
    round = round + 1
  print(sum/rep)

import random
import time

def montecarlo_pi(rep):
  start_time = time.time()
  round = 0
  sum = 0
  while round < rep:
  # The random functio is open in the upper bounded interval. That should not bias the estimation as it's impossible to draw an exact number from an infinite line.
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1:
      sum = sum + 1
    else:
      sum = sum
    round = round + 1
  elapsed_time = time.time() - start_time
  print("Numerical approx. of",4*sum/rep, "calculated in", elapsed_time,"seconds")

montecarlo_pi(5000000)
