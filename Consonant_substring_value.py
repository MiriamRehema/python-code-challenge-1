def solve(s):
    # Function to calculate the value of a substring
    def calculate_value(substring):
        value = 0
        for char in substring:
            value += ord(char) - ord('a') + 1
        return value
    
    vowels = "aeiou"
    max_value = 0
    current_substring = ""
    
    for char in s:
        if char not in vowels:
            current_substring += char
        else:
            if current_substring:
                current_value = calculate_value(current_substring)
                max_value = max(max_value, current_value)
                current_substring = ""
    
    # Check if the last substring is a consonant substring
    if current_substring:
        current_value = calculate_value(current_substring)
        max_value = max(max_value, current_value)
    
    return max_value

