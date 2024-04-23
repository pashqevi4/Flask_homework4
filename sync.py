from random import randint
import time


def count_nums():
    sum_nums = 0
    arr = []
    print('Подсчет начался')
    for _ in range(1000001):
        arr.append(randint(1, 101))
    print('Подсчет закончился')
    return sum(arr)


start_time = time.time()
for _ in range(5):
    print(count_nums())
print(f'{time.time() - start_time: .2f}')
