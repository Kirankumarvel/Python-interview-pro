
# Q8: List comprehensions and side effects
squares = [x*x for x in range(5)]
print(squares)

# Side effects with functions
def effect(x):
    print(f"Processing {x}")
    return x * x

result = [effect(i) for i in range(3)]
