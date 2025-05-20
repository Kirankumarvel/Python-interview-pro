
# Q2: Default argument pitfalls
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2] – reused list

# Correct way
def append_safe(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list
