def merge_sort(arr, reverse=False):
    if len(arr) <= 1:
        return arr

    q = len(arr) // 2
    left = arr[:q]
    right = arr[q:]

    left = merge_sort(left, reverse)
    right = merge_sort(right, reverse)

    return merge(left, right, reverse)


def merge(left, right, reverse):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if not reverse:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i] > right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result += left[i:]
    result += right[j:]
    return result
