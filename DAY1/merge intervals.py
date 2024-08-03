def merge_intervals(intervals):
    # First, sort the intervals by their start points
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = []
    for interval in intervals:
        # If merged_intervals is empty or if the current interval does not overlap with the previous, append it
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval)
        else:
            # Otherwise, there is overlap, so we merge the current and previous intervals
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
    
    return merged_intervals

# Example usage:
intervals = [[1, 3], [2, 6]]
merged = merge_intervals(intervals)
print("Merged intervals:", merged)
