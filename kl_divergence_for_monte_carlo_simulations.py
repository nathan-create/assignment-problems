import math

def kl_divergence(p,q):
    divergence = 0
    for num in range(len(p)):
        if p[num] != 0 and q[num] != 0:
            divergence -= p[num] * math.log(p[num]/q[num])
        else:
            divergence -= 0
    return -divergence
p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]
print("Testing kl divergence...")
assert kl_divergence(p,q) == -0.09637237851 
print("Passed")

def probability(num_heads, num_flips):
    total_flips = 2**num_flips
    head_flips = factorial(num_flips) / (factorial(num_heads) * factorial(num_flips - num_heads))
    return  head_flips/total_flips
   
from random import random

def monte_carlo_probability(num_heads,num_flips):
    samples = []
    outcome_with_desired_heads=0
    for i in range(1000):
        sample = [round(random()) for flips in range(num_flips)]
        heads = 0
        for i in sample:
            if i == 1:
                heads+=1
        if heads==num_heads:
            outcome_with_desired_heads+=1
        heads=0
        samples.append(sample)
    return outcome_with_desired_heads/1000

