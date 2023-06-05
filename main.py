import random


def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comparisons, swaps


def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            swaps += 1
            arr[j + 1] = arr[j]
            j -= 1
        comparisons += 1
        arr[j + 1] = key
    return comparisons, swaps


def insertion_sort_sentinel(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    arr.append(float('inf'))  # Sentinel value
    i = 1
    while i < n:
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            comparisons += 1
            swaps += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        i += 1
    arr.pop()  # Remove the sentinel value
    return comparisons, swaps


def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        swaps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons, swaps


def quick_sort(arr, low, high):
    comparisons = 0
    swaps = 0
    if low < high:
        pivot_idx, comp, sw = partition(arr, low, high)
        comparisons += comp
        swaps += sw
        lc, ls = quick_sort(arr, low, pivot_idx)
        rc, rs = quick_sort(arr, pivot_idx + 1, high)
        comparisons += lc + rc
        swaps += ls + rs
    return comparisons, swaps


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    comparisons = 0
    swaps = 0
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            comparisons += 1
            left += 1
        while arr[right] >= pivot and right >= left:
            comparisons += 1
            right -= 1
        if right < left:
            done = True
        else:
            swaps += 1
            arr[left], arr[right] = arr[right], arr[left]
    swaps += 1
    arr[low], arr[right] = arr[right], arr[low]
    return right, comparisons, swaps


def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()


def main():
    #arr = random.sample(range(1000), 20)
    #arr = [115, 174, 184, 269, 284, 291, 328, 351, 447, 641, 642, 674, 679, 680, 682, 713, 792, 797, 904, 989]
    #arr = [989, 904, 797, 792, 713, 682, 680, 679, 674, 642, 641, 447, 351, 328, 291, 284, 269, 184, 174, 115]

    print("Przed sortowaniem:")
    print("Tablica przed sortowaniem:", end=" ")
    print_array(arr)

    print("\nSortowanie metoda bąbelkową:")
    bubble_arr = arr.copy()
    bubble_comparisons, bubble_swaps = bubble_sort(bubble_arr)
    print("Tablica po sortowaniu:", end="   ")
    print_array(bubble_arr)
    print("Liczba porównań:", bubble_comparisons)
    print("Liczba zamian:", bubble_swaps)

    print("\nSortowanie metoda przez proste wstawianie:")
    insertion_arr = arr.copy()
    insertion_comparisons, insertion_swaps = insertion_sort(insertion_arr)
    print("Tablica po sortowaniu:", end="   ")
    print_array(insertion_arr)
    print("Liczba porównań:", insertion_comparisons)
    print("Liczba zamian:", insertion_swaps)

    print("\nSortowanie metoda przez proste wstawianie ze strażnikiem:")
    sentinel_arr = arr.copy()
    sentinel_comparisons, sentinel_swaps = insertion_sort_sentinel(sentinel_arr)
    print("Tablica po sortowaniu:", end="   ")
    print_array(sentinel_arr)
    print("Liczba porównań:", sentinel_comparisons)
    print("Liczba zamian:", sentinel_swaps)

    print("\nSortowanie metoda przez proste wybieranie:")
    selection_arr = arr.copy()
    selection_comparisons, selection_swaps = selection_sort(selection_arr)
    print("Tablica po sortowaniu:", end="   ")
    print_array(selection_arr)
    print("Liczba porównań:", selection_comparisons)
    print("Liczba zamian:", selection_swaps)

    print("\nSortowanie metoda quick sort:")
    quick_arr = arr.copy()
    quick_comparisons, quick_swaps = quick_sort(quick_arr, 0, len(quick_arr) - 1)
    print("Tablica po sortowaniu:", end="   ")
    print_array(quick_arr)
    print("Liczba porównań:", quick_comparisons)
    print("Liczba zamian:", quick_swaps)


if __name__ == "__main__":
    main()
