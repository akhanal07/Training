def largest_contiguous_subarray(arr):
    n = len(arr)
    max_len = 0

    for i in range(n):
       
        element_set = set()

       
        min_val = arr[i]
        max_val = arr[i]

        
        for j in range(i, n):
           
            if arr[j] in element_set:
                break

            # Add the current element to the set
            element_set.add(arr[j])

            # Update the minimum and maximum element
            min_val = min(min_val, arr[j])
            max_val = max(max_val, arr[j])

            # Check if the current subarray forms a contiguous subarray
            if max_val - min_val == j - i:
                max_len = max(max_len, j - i + 1)

    return max_len

# Example usage:
arr = [10, 12, 11, 14, 13, 16]
print(f"Largest subarray with contiguous elements is of length: {largest_contiguous_subarray(arr)}")
