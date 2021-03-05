gradeToNum ['A'] = 4
gradeToNum ['B'] = 3
gradeToNum ['C'] = 2
gradeToNum ['D'] = 1
gradeToNum ['F'] = 0

calcGPA grades = fromIntegral(sum(map(gradeToNum) grades))/fromIntegral(length(grades))

main = print(calcGPA ["A", "B", "B", "C", "C", "C", "D", "F"]) 