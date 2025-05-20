
# Q1: Difference between 'is' and '=='
a = [1, 2, 3]
b = a
c = list(a)

print(a == c)  # True: Values are equal
print(a is c)  # False: Different memory locations
print(a is b)  # True: Same memory reference
