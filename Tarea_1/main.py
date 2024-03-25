from Problem import Problem
from random import randint


#TESTING
problem = Problem("./data/1-2024.txt")

X = []

for _ in range(200):
    X.append(randint(0, 1))

print(problem._get_FO_value(X))