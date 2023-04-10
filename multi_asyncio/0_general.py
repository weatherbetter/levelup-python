import time

start = time.time()
def my_func():
    for i in range(10):
        time.sleep(0.5)
        print(i)

my_func()
my_func()
my_func()
end = time.time()
print(end - start) # 15.032427072525024