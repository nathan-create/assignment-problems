def first_n_terms(n):
    terms=[5]
    for i in range(n-1):
        last_term=terms[-1]
        next_term=3*last_term - 4
        terms.append(next_term)
    return terms

print("testing first_n_terms on input '10'")
assert first_n_terms(10)==[5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051], 'the test failed'
print('Passed')

#I was unable to figure out how to approach nth_term
#def nth_term(n):
    
     