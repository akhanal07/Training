def first_non_repeating_character(s):
    # Dictionary to store the count of each character
    char_count = {}

    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char

    return None  # Return None if no non-repeating character is found

# Example usage
s = "swwiss"
result = first_non_repeating_character(s)
if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("No non-repeating character found.")
