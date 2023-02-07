def counting_sort(array, reverse=False):
    n = len(array)
    k = max(array) + 1
    C = [0] * k

    for i in range(n):
        C[array[i]] += 1

    if reverse:
        for i in range(k - 2, 0, -1):
            C[i] += C[i + 1]
    else:
        for i in range(1, k):
            C[i] += C[i - 1]

    B = [0] * n
    if reverse:
        for i in range(n - 1, -1, -1):
            B[C[array[i]] - 1] = array[i]
            C[array[i]] -= 1
    else:
        for i in range(n):
            B[C[array[i]] - 1] = array[i]
            C[array[i]] -= 1

    return B
