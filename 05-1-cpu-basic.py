import os
import time
import threading
from unittest import result

# nums = [50, 63, 32]
nums = [30] * 100

def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():  # 28.532921075820923 / 16.48397397994995
    results = [cpu_bound_func(num) for num in nums]
    print(results)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)