def grid_search(function, lines):
    points_of_interest = []
    for num in lines[0]:
        for num2 in lines[1]:
            points_of_interest.append([num,num2])

    lowest_val = function(points_of_interest[0][0],points_of_interest[0][1])
    point_for_val = points_of_interest[0]
    

    for point in points_of_interest:
        

        if function(point[0],point[1]) < lowest_val:
            lowest_val = function(point[0],point[1])
            point_for_val = point
    return point_for_val

def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3

x_lines = [0, 0.25, 0.75]
y_lines = [0.9, 1, 1.1, 1.2]
grid_lines = [x_lines, y_lines]
print('Testing grid_search')
assert grid_search(two_variable_function, grid_lines) == [0.75,0.9]
print("Passed")