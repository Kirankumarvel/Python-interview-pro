
# Q9: Generators vs Lists
def square_gen(n):
    for i in range(n):
        yield i * i

# Generator
g = square_gen(5)
for val in g:
    print(val)

# List version (uses more memory)
squares = [i*i for i in range(5)]
