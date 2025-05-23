import time
import random

def generate_random_list(size, min_val, max_val):
    """
    Generates a list of random integers.

    Args:
        size: The number of elements in the list.
        min_val: The minimum possible value for an element.
        max_val: The maximum possible value for an element.

    Returns:
        A list of random integers.
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


def bubble_sort(arr):
    """
    Sorts a list of numbers using the Bubble Sort algorithm and tracks the time taken.

    Args:
        arr: The list of numbers to be sorted.

    Returns:
        The sorted list.
    """
    start_time = time.time() # Record the start time

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

    end_time = time.time() # Record the end time
    elapsed_time = end_time - start_time # Calculate the elapsed time
    print(f"Time taken to sort: {elapsed_time:.6f} seconds") # Print the elapsed time

    return arr


if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original list: {my_list}")
    sorted_list = bubble_sort(my_list)
    print(f"Sorted list: {sorted_list}\n")

    #Test 1
    print("--- Testing with randomly generated lists ---")
    random_list_size = 1000
    random_min_val = 1
    random_max_val = 10000
    random_numbers = generate_random_list(random_list_size, random_min_val, random_max_val)
    print(f"Generated a random list of size {random_list_size}. (Displaying first 10 elements): {random_numbers[:10]}...")

    sorted_random_list = bubble_sort(random_numbers)
    print(f"Sorted random list. (Displaying first 10 elements): {sorted_random_list[:10]}...")

    #Test 2
    random_list_size = 10000
    random_min_val = 1
    random_max_val = 10000
    random_numbers = generate_random_list(random_list_size, random_min_val, random_max_val)
    print(f"Generated a random list of size {random_list_size}. (Displaying first 10 elements): {random_numbers[:10]}...")

    sorted_random_list = bubble_sort(random_numbers)
    print(f"Sorted random list. (Displaying first 10 elements): {sorted_random_list[:10]}...")

    #Test 3
    random_list_size = 100000
    random_min_val = 1
    random_max_val = 10000
    random_numbers = generate_random_list(random_list_size, random_min_val, random_max_val)
    print(f"Generated a random list of size {random_list_size}. (Displaying first 10 elements): {random_numbers[:10]}...")

    sorted_random_list = bubble_sort(random_numbers)
    print(f"Sorted random list. (Displaying first 10 elements): {sorted_random_list[:10]}...")