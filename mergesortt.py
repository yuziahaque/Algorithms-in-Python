def merge_sort(arr):
    # Base case: If the array has only one element or is empty, it's already sorted.
    if len(arr) <= 1:
        return arr
    
    # Split the input array into two halves.
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]
    
    # Recursively sort each half.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves back together.
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    # Compare elements from both halves and merge them in sorted order.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Append any remaining elements from both halves (if any).
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# test case:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)


