
# Q6: Mutable default argument danger
def func(data=[]):
    data.append("X")
    return data

print(func())  # ['X']
print(func())  # ['X', 'X'] — reused mutable object!
