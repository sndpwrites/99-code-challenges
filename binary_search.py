
#iterative approach using while loop
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # to avoid potential overflow
        print(mid)
        # Check if target is present at mid
        if arr[mid] == target:
            return mid  # target found
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target is not present in array
    return -1


#recursive approach
def recursive_binary_search(arr, target, left, right):
    # Base case: if left index exceeds right, target is not present
    if left > right:
        return -1
    
    # Calculate middle index
    mid = left + (right - left) // 2
    
    # Check if the target is at the mid index
    if arr[mid] == target:
        return mid
    # If target is greater, search in the right half
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    # If target is smaller, search in the left half
    else:
        return recursive_binary_search(arr, target, left, mid - 1)


# Example usage
arr = [i for i in range(1, 100)]

target = 10 #replace with any element

result = binary_search(arr, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")