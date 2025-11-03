'''
Problem: First Non-Repeating Character

APPROACH
1. Use a dictionary to count occurrences of each character.
2. Loop through the string again to find the first character
   whose count is 1.
3. Return that character, or an empty string if none found.

COMPLEXITY
Time Complexity: O(n)
Space Complexity: O(1) — since ASCII characters are finite (max 128).
'''

def first_non_repeating_char(s1: str) -> str:

    if not s1:
        return ""
    
    # First pass: count each character
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    
    # Second pass: find the first non-repeating character
    for ch in s1:
        if count[ch] == 1:
            return ch
    
    # If no unique character exists
    return ""


# Test cases
assert first_non_repeating_char("swiss") == "w"        # Expected: 'w'
assert first_non_repeating_char("") == ""              # Expected: ''
assert first_non_repeating_char("aabbcc") == ""        # Expected: ''
assert first_non_repeating_char("a") == "a"            # Expected: 'a'
assert first_non_repeating_char("aA") == "a"           # Expected: 'a' (case-sensitive)
assert first_non_repeating_char("success") == "u"      # Expected: 'u'
