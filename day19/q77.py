import timeit
import datetime
import time


t = timeit.Timer("for i in range(100): 1+1")
print(t.timeit())

print("*" * 20)
before = datetime.datetime.now()
for i in range(100):
    1 + 1
after = datetime.datetime.now()
execution_time = before - after

print("*" * 20)
before_execution = time.time()
for i in range(100):
    z = 1 + 1
after_execution = time.time()
running_time = before_execution - after_execution
print(running_time)
