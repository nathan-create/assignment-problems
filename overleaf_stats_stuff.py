c = 922741.86
v = 68
total = c/(v**4)
while total <= 0.95:
    v+=1
    total +=c/(v**4)
print(v)