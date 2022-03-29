# A Python binary search is an algorithm that finds the position of an element in an ordered array. Binary searches
# repeatedly divide a list into two halves. Then, a search compares if a value is higher or lower than the middle
# value in the list.


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
    return "not found"


# Binary search runs in logarithmic time in the worst case, making O(Log n) comparisons,
# where n is the number of elements in the array. Binary search is faster than linear search
# except for small arrays. However, the array must be sorted first to be able to apply binary search. There are
# specialized data structures designed for fast searching, such as hash tables, that can be searched more efficiently
# than binary search. However, binary search can be used to solve a wider range of problems, such as finding the
# next-smallest or next-largest element in the array relative to the target even if it is absent from the array.

my_list = [2, 3, 4, 10, 40, 60, 61, 23]

print(binary_search(my_list, 66))
print(binary_search(my_list, 2))
print(binary_search(my_list, 40))
