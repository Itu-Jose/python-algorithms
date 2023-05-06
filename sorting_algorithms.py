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
        arr_min = minimum(arr[i+1::])
        if arr[i] > arr_min:
            j = arr[i+1::].index(arr_min) + i + 1
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
        for i in range(n-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

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
        for i in range(n-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        if not swap:
            break

    return arr