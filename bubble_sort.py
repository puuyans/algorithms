# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are
# in wrong order. The function always runs O(n^2) time even if the array is sorted Bubble sort, sometimes referred to
# as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements
# and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The
# algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the
# list.

# This simple algorithm performs poorly in real world use and is used primarily as an educational tool. More
# efficient algorithms such as quicksort, timsort, or merge sort are used by the sorting libraries built into popular
# programming languages such as Python and Java

def bubble_sort(arr):
    length = len(arr)

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


my_list = [1,2,3,4,5]

print(bubble_sort(my_list))
