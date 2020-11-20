import matplotlib.pyplot as plt
plt.style.use('bmh')


def collatz_iterations(n):
    number_of_iterations = 0
    while n >1:
        if n%2 == 0:
            n = n/2
            number_of_iterations+=1
        else:
            n = 3*n + 1
            number_of_iterations+=1
    return number_of_iterations
    
        
print("Testing collatz_iterations..")
assert collatz_iterations(13) == 9, "actual output was {}".format(collatz_iterations(13))
print("Passed")

#answer to part b
def highest_collatz_iterations():
    high = 0
    for num in range(1,1001):
        if collatz_iterations(num)>high:
            high = num
    return num
print(highest_collatz_iterations())


x_coords = list(range(1,1000))
y_coords = list(collatz_iterations(n) for n in x_coords)
plt.plot(x_coords, y_coords)
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.title('This is the title of the plot!')
plt.savefig('plot.png')