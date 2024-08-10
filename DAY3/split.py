def is_palindrome(s):
    return s == s[::-1]

def split_into_palindromes(s):
    n = len(s)
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            first = s[:i]
            second = s[i:j]
            third = s[j:]
            
            if is_palindrome(first) and is_palindrome(second) and is_palindrome(third):
                return first, second, third
    
    return None

# Test the function
s = "aabaca"
result = split_into_palindromes(s)
if result:
    print(f"The string can be split into three palindromic substrings: {result}")
else:
    print("It's not possible to split the string into three palindromic substrings.")
