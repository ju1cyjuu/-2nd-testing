def binary_search(target_list, target_value):
    low = 0
    high = len(target_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if target_list[mid] == target_value:
            return mid  

        elif target_list[mid] > target_value:
            high = mid - 1
            
        else:
            low = mid + 1
            
    return -1 

arr = [10, 20, 30, 40, 50]
user_input = int(input("Enter the number that you want to search: "))

result = binary_search(arr, user_input)


if result != -1:
    print(f"Element found at position: {result+1}")
else:
    print("Element not found in the list.")

#Bubble sort
class BubbleSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(n- 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements

arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)
BubbleSort.sort(arr)
print("Sorted array:", arr)