def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def probability(num_heads, num_flips):
    total_flips = 2**num_flips
    head_flips = factorial(num_flips) / (factorial(num_heads) * factorial(num_flips - num_heads))
    return  head_flips/total_flips
   
#print("testing probability...")
#assert probability(5,8) == 0.21875, "The actual output was {}".format(probability(5,8))
#print("passed")

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
#print("Running monte_carlo_probability...")
#print("Probability is roughly {}".format(monte_carlo_probability(5,8)))

        
def five_instances():
    print(monte_carlo_probability(5,8))
    print(monte_carlo_probability(5,8))
    print(monte_carlo_probability(5,8))
    print(monte_carlo_probability(5,8))
    print(monte_carlo_probability(5,8))
print("Below are five five instances")
#five_instances()

print(probability(0,8),probability(1,8),probability(2,8),probability(3,8),probability(4,8),probability(5,8),probability(6,8),probability(7,8),probability(8,8))