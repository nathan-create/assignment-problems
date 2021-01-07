import random

def random_draw(distribution):
    sum = 0
    cumulative_dist=[]
    for prob in distribution:
        sum+=prob
        cumulative_dist.append(sum)
    probability=random.randint(0,1000)/1000
    for num in cumulative_dist:
        if num>=probability:
            return cumulative_dist.index(num)

test=[random_draw([0.5,0.5]) for num in range(0,1001)]
test_sum = 0
exp_val = 0
for num in range(len(test)):
    exp_val += num * test[num]
    #print(num)
    test_sum+=test[num]

print('True E[X]:0.5')
print('Sample value:',test_sum/len(test))

test=[random_draw([0.25,0.25,0.5]) for num in range(0,1001)]
test_sum = 0
exp_val = 0
for num in range(len(test)):
    exp_val += num * test[num]
    #print(num)
    test_sum+=test[num]

print('True E[X]:1.25')
print('Sample value:',test_sum/len(test))

test=[random_draw([0.05,0.2,0.15,0.3,0.1,0.2]) for num in range(0,1001)]
test_sum = 0
exp_val = 0
for num in range(len(test)):
    exp_val += num * test[num]
    #print(num)
    test_sum+=test[num]

print('True E[X]:2.8')
print('Sample value:',test_sum/len(test))