from random import randint
import time
import threading


def count_nums(num):
    print(f'Подсчет номер {num} начался')
    arr = []
    for _ in range(1000000):
        arr.append(randint(1, 101))
    print(f'Подсчет номер {num} закончился')
    return sum(arr)


def main():
    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=count_nums, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f'{time.time() - start_time: .2f}')
