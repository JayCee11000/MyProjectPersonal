def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
data_set = [64, 34, 25, 12, 22, 11, 90, 2, 40, 51, 74, 18, 32, 61, 59, 82, 5, 36, 47, 45, 3, 1, 67, 21, 88, 54, 29, 65, 50, 70]

bubble_sort(data_set)
print("Sorted array is:", data_set)
