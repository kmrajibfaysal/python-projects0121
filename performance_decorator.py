from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"\ntook {t2-t1}s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000000):
        i = i


long_time()
