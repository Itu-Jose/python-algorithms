def minimum(arr: list[int]) -> int:
    """
    Find minimum integer in list
    :param arr:
    :return: minimum integer in arr
    """
    min_val = float('inf')
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]

    return min_val


def maximum(arr: list[int]) -> int:
    """
    Find maximum integer in list
    :param arr:
    :return: maximum integer in arr
    """

    max_val = float('-inf')
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]

    return max_val


def selection(arr: list[int]) -> list[int]:
    """
    Performs a selection sort on an input list. Takes the smallest/largest integer
    from the unsorted portion of the list and moves it to the sorted portion of the
    list.
    :param arr:
    :return: sorted list
    """
    for i in range(len(arr)):
        arr_min = minimum(arr[i + 1::])
        if arr[i] > arr_min:
            j = arr[i + 1::].index(arr_min) + i + 1
            arr[i], arr[j] = arr[j], arr[i]

    return arr


def bubble(arr: list[int]) -> list[int]:
    """
    Performs a bubble sort on an input list. Repeatedly swaps adjacent elements
    if they are in the wrong order.
    :param arr:
    :return: sorted list
    """
    n = len(arr)
    for j in range(n):
        for i in range(n - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


def bubble_optimized(arr: list[int]) -> list[int]:
    """
    Performs a bubble sort on an input list. Stops if inner loop
    swap does not occur.
    :param arr:
    :return: sorted list
    """
    n = len(arr)
    for j in range(n):
        swap = False
        for i in range(n - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        if not swap:
            break

    return arr


def merge_sort(arr: list[int]):
    """
    Performs a merge sort on an input list. Split array into two arrays recursively
    until there's only basic units left in split arrays. Then combines arrays back
    recursively in sorted order.
    :param arr:
    :return: sorted list
    """
    if len(arr) > 1:
        m = len(arr)//2
        l_arr = arr[:m]
        r_arr = arr[m:]
        merge_sort(l_arr)
        merge_sort(r_arr)

        i = j = k = 0

        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] <= r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1

        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1
