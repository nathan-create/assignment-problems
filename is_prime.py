def is_prime(n):
    if n > 1: 
        for i in range(2, n): 
            if (n % i) == 0: 
                return False
                break
        else: 
            return True

print("testing is_prime on input '59'")
assert is_prime(59)==True, "Input is not a prime number"
print("Passed")

print("testing is on input '51'")
assert is_prime(51)==False, "Input is not a prime number"
print("Passed")