import numpy as np

# Minimos de las ecuaciones.
def equation1(X):
    return (X**2) - 10 * np.cos(2 * np.pi * X) + 10
# d = 10, −5.12 ≤ xi ≤ 5.12 ∀i = 1, ..., d.

def equiation2(x1,x2):
    return 100*((x2-x1**2)**2)+(x1-1)**2
# d = 20, −30 ≤ xi ≤ 30 ∀i = 1, ..., d.

def equiation3(x,i):
    return np.sin(x)*(np.sin((i*x**2)/np.pi))**20
# d = 5, 0 ≤ xi ≤ π ∀i = 1, ..., d.

def solution1(d,x: list):
    sum = 0
    for i in range(d):
        sum += equation1(x[i])
    return sum

def solution2(d,x: list):
    sum = 0
    for i in range(d-1):
        sum += equiation2(x[i],x[i+1])
    return sum

def solution3(d,x: list):
    sum = 0
    for i in range (d):
        sum += equiation3(x[i],i+1)*-1
        #print(sum)
    return sum

