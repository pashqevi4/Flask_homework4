import asyncio
import time
from random import randint


async def count_nums():
    sum_nums = 0
    arr = []
    print('Подсчет начался')
    for _ in range(1000001):
        arr.append(randint(1, 101))
    print('Подсчет закончился')
    return sum(arr)


async def main():
    tasks = []

    for i in range(5):
        task = asyncio.create_task(count_nums())
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print('Finish')
    print(f'{time.time() - start_time: .2f}')
