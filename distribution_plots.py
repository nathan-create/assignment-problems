import matplotlib.pyplot as plt
from random import random
def probability(num_heads, num_flips):
    total_flips = 2**num_flips
    head_flips = factorial(num_flips) / (factorial(num_heads) * factorial(num_flips - num_heads))
    return  head_flips/total_flips

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



plt.style.use('bmh')
plt.plot([0,1,2,3,4,5,6,7,8],[0.00390625,0.03125, 0.109375, 0.21875, 0.2734375,0.21875,0.109375,0.03125,0.00390625],linewidth=2.5)
plt.plot([0,1,2,3,4,5,6,7,8],[monte_carlo_probability(0,8),monte_carlo_probability(1,8),monte_carlo_probability(2,8),monte_carlo_probability(3,8),monte_carlo_probability(4,8),monte_carlo_probability(5,8),monte_carlo_probability(6,8),monte_carlo_probability(7,8),monte_carlo_probability(8,8)],linewidth=0.75)
plt.plot([0,1,2,3,4,5,6,7,8],[monte_carlo_probability(0,8),monte_carlo_probability(1,8),monte_carlo_probability(2,8),monte_carlo_probability(3,8),monte_carlo_probability(4,8),monte_carlo_probability(5,8),monte_carlo_probability(6,8),monte_carlo_probability(7,8),monte_carlo_probability(8,8)],linewidth=0.75)
plt.plot([0,1,2,3,4,5,6,7,8],[monte_carlo_probability(0,8),monte_carlo_probability(1,8),monte_carlo_probability(2,8),monte_carlo_probability(3,8),monte_carlo_probability(4,8),monte_carlo_probability(5,8),monte_carlo_probability(6,8),monte_carlo_probability(7,8),monte_carlo_probability(8,8)],linewidth=0.75)
plt.plot([0,1,2,3,4,5,6,7,8],[monte_carlo_probability(0,8),monte_carlo_probability(1,8),monte_carlo_probability(2,8),monte_carlo_probability(3,8),monte_carlo_probability(4,8),monte_carlo_probability(5,8),monte_carlo_probability(6,8),monte_carlo_probability(7,8),monte_carlo_probability(8,8)],linewidth=0.75)
plt.plot([0,1,2,3,4,5,6,7,8],[monte_carlo_probability(0,8),monte_carlo_probability(1,8),monte_carlo_probability(2,8),monte_carlo_probability(3,8),monte_carlo_probability(4,8),monte_carlo_probability(5,8),monte_carlo_probability(6,8),monte_carlo_probability(7,8),monte_carlo_probability(8,8)],linewidth=0.75)
plt.legend(['True','MC 1','MC 2', 'MC 3','MC 4','MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 8 Coin Flips')
plt.savefig('plot.png')