from typing import List
from random import shuffle, randint, sample


def subSum(nums: List[int], k: int) -> bool:
    print(f"{k}: {nums}")
    if k == 0:
        return True
    elif k < 0 or nums == []:
        return False
    else:
        return subSum(nums[:-1], k-nums[-1]) or subSum(nums[:-1], k)


def main():
    k: int = randint(1, 1000)
    lista: List[int] = sample(range(1, 1000), k//2)
    lista.sort()
    print(subSum(lista, k))


if __name__ == '__main__':
    main()
