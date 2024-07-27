def reverse_dictionary(d):


  reversed_dict = {}
  for key, value in d.items():
    if value in reversed_dict:
      reversed_dict[value].append(key)
    else:
      reversed_dict[value] = [key]
  return reversed_dict

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
reversed_dict = reverse_dictionary(my_dict)
print(reversed_dict)  # Output: {1: ['a'], 2: ['b', 'd'], 3: ['c']}
