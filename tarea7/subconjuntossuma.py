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


def sub_sum_idx(idx: int, target: int, nums: List[int]) -> bool:
    print(f"{target} : {idx} : {nums}")
    if target == 0:
        return True
    if idx < 0 or target < 0:
        return False
    return sub_sum_idx(idx-1, target-nums[idx], nums) or sub_sum_idx(idx-1, target, nums)


def sum_subset_memo(idx: int, target: int, nums: List[int], cache: List[List[int]]) -> bool:
    print(f"{target} : {idx} : {nums}")
    if target < 0:
        return False
    if cache[idx+1][target] != -1:
        return bool(cache[idx+1][target])
    if target == 0:
        cache[idx+1][target] = 1
        return True
    if idx < 0:
        cache[idx+1][target] = 0
        return False
    res = sum_subset_memo(
        idx-1, target-nums[idx], nums, cache) or sum_subset_memo(idx-1, target, nums, cache)
    cache[idx+1][target] = int(res)
    return res


def sum_subset_pd(target: int, nums: List[int]) -> bool:
    print(f"{target} : {nums}")
    n = len(nums)
    table = [[False] * (target+1) for _ in range(n+1)]
    for i in range(n+1):
        table[i][0] = True

    for i in range(1, n+1):
        for j in range(1, target+1):
            if j - nums[i-1] < 0:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j-nums[i-1]] or table[i-1][j]
    print_table(target, n, table)

    return table[n][target]


def print_table(k, n, table):
    board = [
        ["T" if cell else "F" for cell in table[row]]
        for row in range(n+1)
    ]
    print("i\\k ", end="")
    for i in range(k+1):
        print(f"| {i:3d} ", end="")
    print("|")
    print("-" * (4 + 6 * (k+1) + 1))
    for i in range(n+1):
        for j in range(k+2):
            if j == 0:
                print(f"{i-1:3d} ", end="")
            else:
                print(f"| {board[i][j-1]:3s} ", end="")
        print("|")
        print("-" * (4 + 6 * (k+1) + 1))
    print("")


def main():
    k: int = randint(1, 20)
    lista: List[int] = sample(range(1, 20), randint(0, k-1))
    lista.sort()
    n = len(lista)
    print(sum_subset_pd(k, lista))


if __name__ == '__main__':
    main()
