sumFactorsList n = [x | x <- [1..n], n `mod` x == 0]
sumFactors = sum . sumFactorsList

main = print(sumFactors 10)