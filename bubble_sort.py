def bubble_sort(arr):
    """
    Sorts a list of numbers using the Bubble Sort algorithm.

    Args:
        arr: The list of numbers to be sorted.

    Returns:
        The sorted list.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        # We optimize by checking if any swaps occurred in a pass.
        # If no swaps, the array is sorted.
        swapped = False
        # Traverse the array from 0 to n-i-1
        # Compare adjacent elements and swap them if they are in the wrong order
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

# Example usage:
if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original list: {my_list}")

    sorted_list = bubble_sort(my_list)
    print(f"Sorted list: {sorted_list}")

    my_list_2 = [5, 1, 4, 2, 8]
    print(f"Original list: {my_list_2}")
    sorted_list_2 = bubble_sort(my_list_2)
    print(f"Sorted list: {sorted_list_2}")

    my_list_3 = []
    print(f"Original list: {my_list_3}")
    sorted_list_3 = bubble_sort(my_list_3)
    print(f"Sorted list: {sorted_list_3}")

    my_list_4 = [7]
    print(f"Original list: {my_list_4}")
    sorted_list_4 = bubble_sort(my_list_4)
    print(f"Sorted list: {sorted_list_4}")