# Bubble Sort is the simplest sorting algorithm
# that works by repeatedly swapping the adjacent elements if they are in wrong order.
# The function always runs O(n^2) time even if the array is sorted
def bubble_sort(arr):
    length = len(arr)

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


my_list = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(my_list))
