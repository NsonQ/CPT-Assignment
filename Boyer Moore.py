def bad_character_table(pattern):
    """
    This function generates a table mapping each character to its last occurrence in the pattern.
    It take the pattern as input and returns a dictionary with the character as the key and the index as the value.
    """
    table = {}      # Initialize an empty dictionary

    # Iterates over the pattern, i is the index and char is the character at that index
    # The dictionary is updated with the character as the key and the index as the value
    for i, char in enumerate(pattern):
        table[char] = i
    return table

def good_suffix_table(pattern):
    """
    This function generates the good suffix table, which is used to determine the shift when a mismatch occurs.
    It takes the pattern as input and returns a list of shift values for each position in the pattern.
    """
    length = len(pattern)       # Length of the pattern
    table = [0] * length        # Initialize the table with zeros, used for storing the shift values when a mismatch occurs
    border = [0] * (length + 1) # Initialize the border with zeros, will be used in calculation of good suffix table
    
    # Part 1: Analyze the pattern
    i = length          # Initialize i with the length of the pattern
    j = length + 1      # Initialize j with the length of the pattern plus one
    border[i] = j       # Update the border value for the last position in the pattern

    while i > 0:
        # Continue if the character at i-1 and j-1 does not match
        while j <= length and pattern[i-1] != pattern[j-1]:
            # Update the table for the first occurrence of the mismatched character
            if table[j-1] == 0:
                table[j-1] = j - i
            # Move to next border position
            j = border[j]
        # Move to previous character in the pattern
        i -= 1
        j -= 1
        # Update the border positon for the current character
        border[i] = j
    
    # Part 2: Analyze the prefixes
    # Initialize j with the first border value
    j = border[0]

    # Iterate through each position in the table
    for i in range(length):

        # If the current position in the table is 0, update it with the value of j
        if table[i] == 0:
            table[i] = j

         # If the current index matches j, update j to the next border value
        if i == j:
            j = border[j]
    
    return table

def boyer_moore_search(text, pattern):
    """
    Searches for occurrences of `pattern` within `text` using the Boyer-Moore algorithm.
    """
    # Generate bad character table from the pattern
    bad_char = bad_character_table(pattern)
    # Generate good suffix table from the pattern
    good_suffix = good_suffix_table(pattern)

    i = 0
    # Loop through the text until a potential match is found or end of text is reached
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        # Compare the pattern with a substring of text starting from the end of the pattern
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            print(f"Pattern occurs at index {i}")

             # Shift the index based on the good suffix table or move by one if at the end of text
            i += good_suffix[0] if i + len(pattern) < len(text) else 1

        else:
            # Calculate shift based on the bad character rule
            char_shift = j - bad_char.get(text[i + j], -1)
            # Calculate shift based on the good suffix rule
            good_shift = good_suffix[j] if j < len(pattern) - 1 else 1
            # Choose the maximum shift between the bad character and good suffix shifts
            i += max(char_shift, good_shift)

# Example usage
text = "ABAAABCDABC"
pattern = "ABC"
boyer_moore_search(text, pattern)
