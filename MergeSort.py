class MergeSort:
    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            MergeSort.merge_sort(left_half)
            MergeSort.merge_sort(right_half)
            MergeSort.merge(arr, left_half, right_half)

    @staticmethod
    def merge(arr, left_half, right_half):
        i = j = k = 0

        # Compare elements from both halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1  # Increments every time a choice is made

        # Catch any remaining elements in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Catch any remaining elements in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Main execution (completely unindented)
arr = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted array:", arr)
MergeSort.merge_sort(arr)
print("Sorted array:  ", arr)