import random


def merge_iter(L, R):
    n = len(L)
    m = len(R)
    out = [0]*(n+m)
    i, j, k = 0, 0, 0
    while i < n and j < m:
        if L[i] <= R[j]:
            out[k] = L[i]
            i += 1
        else:
            out[k] = R[j]
            j += 1
        k += 1
    while i < n:
        out[k] = L[i]
        i += 1
        k += 1
    while j < m:
        out[k] = R[j]
        j += 1
        k += 1
    return out


def count_inversiones(L, R):
    n, m = len(L),  len(R)
    count, i, j, k = 0, 0, 0, 0
    while i < n and j < m:
        if L[i] <= R[j]:
            i += 1
        else:
            count += n - i
            j += 1
        k += 1
    return count


def merge_sort_count(A):
    n = len(A)
    if n < 2:
        return A[:], 0
    L = A[:n//2]
    R = A[n//2:]
    L_sorted, L_count = merge_sort_count(L)
    R_sorted, R_count = merge_sort_count(R)
    L_R_merge = merge_iter(L_sorted, R_sorted)
    L_R_merge_count = count_inversiones(L_sorted, R_sorted)
    return L_R_merge, L_R_merge_count + L_count + R_count


def merge_sort_s_count(A):
    n = len(A)
    if n < 2:
        return A[:], 0
    L = A[:n//2]
    R = A[n//2:]
    L_sorted, L_count = merge_sort_s_count(L)
    R_sorted, R_count = merge_sort_s_count(R)
    L_R_merge = merge_iter(L_sorted, R_sorted)
    L_R_merge_count = count_inversiones(L_sorted,  [2*r for r in R_sorted])
    return L_R_merge, L_R_merge_count + L_count + R_count


def count_nxn(A):
    n = len(A)
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if A[j] < A[i]:
                count += 1
    return count


def count_s_nxn(A):
    n = len(A)
    count = 0
    inv = set()
    for i in range(n):
        for j in range(n):
            if i < j and 2*A[j] < A[i]:
                count += 1
                inv.add((i, j))
    return count, inv


def main():
    A = [random.randint(-1000, 1000) for _ in range(10)]
    print(A)

    A_sorted, inversions = merge_sort_count(A)
    print(f"Inversiones encontradas {inversions}/{count_nxn(A)}")
    print(A_sorted)

    A_sorted, inversions = merge_sort_s_count(A)
    inv_count, inv_set = count_s_nxn(A)
    print(
        f"Inversiones significativas encontradas {inversions}/{inv_count}")
    print(inv_set)
    print(len(inv_set))


if __name__ == "__main__":
    main()
