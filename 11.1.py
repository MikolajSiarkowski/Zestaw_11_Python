import random
import math
def a(n):
    L = list(range(n))
    random.shuffle(L)
    print(L)

def b(n):
    L=list(range(n))
    L=sorted(range(n),key = lambda x: x + random.randint(-3,3))
    print(L)

def c(n):
    L=list(range(n))
    L=sorted(range(n),key = lambda x: x + random.randint(-3,3),reverse=True)
    print(L)

def d(n):
    L=list(range(n))
    L=[random.gauss(3,4) for i in range(n)]
    print(L)

def e(n):
    L = list(range(n))
    L= [random.randint(0, int(math.sqrt(n))) for i in range(n)]
    print(L)

