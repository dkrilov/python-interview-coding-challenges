# Challenge 1: Reverse a String
# Write a Python function that takes a string as input and returns the reverse of the string.
# Example:
# Input: "Hello, World!"
# Output: "!dlroW ,olleH"

# Define a function named 'reverse_string' that takes one parameter called 'string'
def reverse_string(string):
    # Return the reversed string using Python's slice notation
    # [::-1] means: start from end, go to beginning, step backwards by 1
    # This is a concise way to reverse any sequence in Python
    return string[::-1]

# Challenge 2: Check Palindrome
# Write a Python function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward.
# Example:
# Input: "racecar"
# Output: True

# Define a function named 'is_palindrome' that takes one parameter called 'string'
def is_palindrome(string):
    # Compare the original string with its reverse
    # If they are equal, it's a palindrome (returns True)
    # If they're different, it's not a palindrome (returns False)
    return string == string[::-1]

# Challenge 3: Count Character Occurrences
# Write a Python function that takes a string and a character as input and returns the number of occurrences of that character in the string.
# Example:
# Input: "Hello, World!", character = "l"
# Output: 3

# Define a function named 'count_occurrences' that takes two parameters: 'string' and 'character'
def count_occurrences(string, character):
    # Initialize a counter variable to keep track of how many times we find the character
    count = 0
    
    # Loop through each character in the input string one by one
    for char in string:
        # Check if the current character matches the character we're looking for
        if char == character:
            # If it matches, increment our counter by 1
            count += 1
    
    # Return the final count of occurrences
    return count

# Challenge 4: Remove Duplicate Characters
# Write a Python function that takes a string as input and returns a new string with duplicate characters removed. The order of characters should be preserved.
# Example:
# Input: "Hello, World!"
# Output: "Helo, Wrd"

# Define a function named 'remove_duplicates' that takes one parameter called 'string'
def remove_duplicates(string):
    # Create an empty list to store unique characters in the order we find them
    unique_chars = []
    
    # Loop through each character in the input string
    for char in string:
        # Check if this character is not already in our unique_chars list
        if char not in unique_chars:
            # If it's new (not a duplicate), add it to our list
            unique_chars.append(char)
    
    # Join all the unique characters back into a single string
    # The empty string '' means no separator between characters
    return ''.join(unique_chars)

# Challenge 5: Check Anagrams
# Write a Python function that takes two strings as input and checks if they are anagrams. Anagrams are words or phrases formed by rearranging the letters of another word or phrase.
# Example:
# Input: "listen", "silent"
# Output: True

# Define a function named 'are_anagrams' that takes two parameters: 'string1' and 'string2'
def are_anagrams(string1, string2):
    # Sort both strings and compare them
    # sorted() converts the string to a list of characters, sorts them alphabetically
    # If both strings have the same characters (regardless of order), they're anagrams
    # This returns True if they're anagrams, False otherwise
    return sorted(string1) == sorted(string2) 