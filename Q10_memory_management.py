
# Q10: Python memory management
import sys
a = [1] * 1000
b = a
print(sys.getrefcount(a))  # Reference count
print(id(a), id(b))  # Same object
