
# Q7: Closures and loop variable problem
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)

for f in funcs:
    print(f())  # 0, 1, 2 — each function remembers its value
