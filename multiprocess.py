from random import randint
import time
import multiprocessing


def work(num):
    print(f'Подсчет номер {num} начался')
    arr = []
    for _ in range(1000000):
        arr.append(randint(1, 101))
    print(f'Подсчет номер {num} закончился')
    return sum(arr)


if __name__ == '__main__':
    start_time = time.time()

    processes = []
    for i in range(1, 6):
        p = multiprocessing.Process(target=work, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'{time.time() - start_time: .2f}')
