import random

def normal_gen(mu,sigma,n):
#Normal Distribution
     x = 0
     while x < n:
             xi = random.gauss(mu,sigma)
             print(xi)
             x = x + 1

def lognormal_gen(mu,sigma,n):
#Lognormal Distribution
     x = 0
     while x < n:
             xi = random.lognormvariate(mu,sigma)
             print(xi)
             x = x + 1

def poisson_gen(lambd,n):
#Poisson Distribution (Exponential Distribution)
     x = 0
     while x < n:
             xi = random.expovariate(lambd)
             print(xi)
             x = x + 1

def weibull_gen(alpha,beta,n):
#Weibull Distribution
     x = 0
     while x < n:
             xi = random.weibullvariate(alpha,beta)
             print(xi)
             x = x + 1

def pareto_gen(alpha,n):
#Pareto Distribution
     x = 0
     while x < n:
             xi = random.paretovariate(alpha)
             print(xi)
             x = x + 1

def gamma_gen(alpha,beta,n):
#Gamma Distribution
     x = 0
     while x < n:
             xi = random.gammavariate(alpha,beta)
             print(xi)
             x = x + 1

def random_gen(n):
#Random numbers within [0,1)
     x = 0
     while x < n:
             xi = random.random()
             print(xi)
             x = x + 1

def uniform_gen(lower,upper,n):
#Random numbers within [lower,upper]
     x = 0
     while x < n:
             xi = random.uniform(lower,upper)
             print(xi)
             x = x + 1

def hypergeo_gen(pop,k,n):
#Hypergeometric (Sampling without replacement)
     x = 0
     while x < n:
             xi = random.sample(range(pop),k)
             print(xi)
             x = x + 1
