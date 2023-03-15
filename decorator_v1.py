from functools import wraps

def deco(a, b):
    def in_deco(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            if a:
                print(f"deco args {a}")
                return func(*args, **kwargs)

        return wrap

    return in_deco

@deco(1, 2)
def hello(a, b, c):
    """hello function"""
    return "hello world"

print(hello(10, 20, 30))
# deco args 1
# hello world
print(help(hello))
