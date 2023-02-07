def insertion_sort(A, reverse=False):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        if reverse:
            while j >= 0 and key > A[j]:
                A[j + 1] = A[j]
                j -= 1
        else:
            while j >= 0 and key < A[j]:
                A[j + 1] = A[j]
                j -= 1
        A[j + 1] = key
    return A
