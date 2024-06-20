# In this Boyer Moore program, 
# The bad character table is used to skip the text when a mismatch occurs.

def boyer_moore(pattern, text):
    # Creating the bad character table which is intilized with -1 in a list of size 256
    # The ord() function below will return the ASCII value of the character
    # Then the position of the character in the pattern is stored in the bad_char_table with its ASCII value as the index
    bad_char_table = [-1]*256
    m = len(pattern)
    for i in range(m):
        bad_char_table[ord(pattern[i])] = i

    # The text_pos is the position of the text where the pattern is being compared
    n = len(text)
    text_pos = 0

    # The while loop below compares the pattern with the text
    # While the pattern is within the text
    while(text_pos <= n-m):

        # The pattern_pos is the position of the pattern where the comparison is being made
        # It is m-1 because the index of the pattern starts from 0
        pattern_pos = m-1

        # This inner while loop will compare the pattern with the text from the end of the pattern
        while pattern_pos >= 0 and pattern[pattern_pos] == text[text_pos + pattern_pos]:
            # If the characters at the current position in the pattern and the text match, move to the next character in the pattern
            pattern_pos -= 1

        # If the pattern has been completely compared with the text (pattern_pos < 0), the pattern occurs in the text at the current shift
        if pattern_pos < 0:
            print("Pattern occurs at shift", text_pos)
            # Shift the pattern along the text for the next comparison
            # The shift is calculated based on the bad character heuristic
            text_pos += (m-bad_char_table[ord(text[text_pos+m])] if text_pos+m < n else 1)
        else:
            # If a mismatch occurs, shift the pattern along the text for the next comparison
            # The shift is calculated based on the bad character heuristic
            text_pos += max(1, pattern_pos-bad_char_table[ord(text[text_pos+pattern_pos])])

# Test the function
boyer_moore("ABCD", "ABC ABCD ABC ABCD AACD ABCD")