
# Q4: GIL - Global Interpreter Lock (Simulated Behavior)
import threading

counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Counter:", counter)  # Output may not be 2,000,000 due to GIL and race condition
