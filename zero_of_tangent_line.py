def zero_of_tangent_line(c):
    f_x = c**3+c-1
    slope = 3*c**2+1
    x_intercept = ((1-c)**(1/3))/c
    tangent_line = slope*(x_intercept - c)-f_x
    return tangent_line 
    

answer = zero_of_tangent_line(0.5)
assert round(answer,6) == 0.714286,"unrounded:{}, rounded:{}".format(answer,round(answer,6))

def f(x):
    return x**3 + x - 1

def estimate_derivative(f, c, delta):
    function = f(c)