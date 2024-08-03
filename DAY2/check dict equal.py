from collections import deque

def dicts_are_equal(dict1, dict2):
    if len(dict1) != len(dict2):
        return False

    queue1 = deque(dict1.items())
    queue2 = deque(dict2.items())

    while queue1 and queue2:
        key1, value1 = queue1.popleft()
        key2, value2 = queue2.popleft()

        if key1 != key2 or value1 != value2:
            return False

    return len(queue1) == len(queue2)

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'b': 2, 'a': 1}
dict3 = {'a': 1, 'b': 2, 'c': 3}

print(dicts_are_equal(dict1, dict2))  # Output: True
print(dicts_are_equal(dict1, dict3))  # Output: False
