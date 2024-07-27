def find_key_with_max_value(my_dict):
    
  if not my_dict:
    return None 

  max_key = max(my_dict, key=my_dict.get)
  return max_key


my_dict = {'a': 3, 'b': 5, 'c': 1}
key_with_max_value = find_key_with_max_value(my_dict)
print(key_with_max_value)
