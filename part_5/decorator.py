from time import time

def args_loger(func):
    def inner(*args):
        if Debug:
            print(f"I am args logger. Args: {args}")
        result = func(*args)
        return result
    return inner

def result_loger(func):
    def inner(*args):
        result = func(*args)
        if Debug:
            print(f"I am result loger. Result: {result}")
        return result
    return inner

def timer(func):
    def inner(*args):
        start = time()
        result = func(*args)
        stop = time()
        if Debug:
            print(f"I am timer. Run time: {stop-start}")
        return result
    return inner


@timer
@result_loger
@args_loger
def calc(x, y):
    result = x+y
    return result

Debug = True

print(calc(2, 78))   