def reverse_words(s):
    # Split the string into words
    words = s.split()
    
    # Reverse each word and store it in a list
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    
    # Join the reversed words back into a string with spaces
    return ' '.join(reversed_words)

# Example usage:
input_string = "Hello World"
reversed_string = reverse_words(input_string)
print(reversed_string)
