def find_key_with_max_value(my_dict):
  """Finds the key with the maximum value in a dictionary.

  Args:
    my_dict: The input dictionary.

  Returns:
    The key with the maximum value.
  """

  if not my_dict:
    return None  # Handle empty dictionary

  max_key = max(my_dict, key=my_dict.get)
  return max_key

# Example usage:
my_dict = {'a': 3, 'b': 5, 'c': 1}
key_with_max_value = find_key_with_max_value(my_dict)
print(key_with_max_value)  # Output: b
