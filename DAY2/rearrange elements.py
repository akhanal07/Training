def zig_zag(arr):
    n = len(arr)
    
    # Flag true indicates < relation expected, 
    # else > relation expected.
    flag = True
    
    for i in range(n-1):
        if flag:
            # If we have a situation like a > b, 
            # we swap a and b.
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            # If we have a situation like a < b, 
            # we swap a and b.
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                
        # flip flag for next iteration
        flag = bool(1 - flag)
    
    return arr

# Example usage
arr = [4, 3, 7, 8, 6, 2, 1]
print("Original array:", arr)
zig_zag_arr = zig_zag(arr)
print("Zig-Zag array:", zig_zag_arr)
