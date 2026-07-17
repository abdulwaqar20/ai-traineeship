import math
import random
import numpy as np


def dot_product(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total

def magnitude(v):
    total = 0
    for x in v:
        total += x * x
    return math.sqrt(total)

def mean(v):
    return sum(v) / len(v)

def variance(v):
    m = mean(v)
    total = 0
    for x in v:
        total += (x - m) ** 2
    return total / len(v)

for i in range(100):

    a = [random.uniform(-100, 100) for _ in range(10)]
    b = [random.uniform(-100, 100) for _ in range(10)]

    if abs(dot_product(a, b) - np.dot(a, b)) > 1e-9:
        print("Dot Product Failed")

    if abs(magnitude(a) - np.linalg.norm(a)) > 1e-9:
        print("Magnitude Failed")

    if abs(mean(a) - np.mean(a)) > 1e-9:
        print("Mean Failed")

    if abs(variance(a) - np.var(a)) > 1e-9:
        print("Variance Failed")

print("All tests passed!")