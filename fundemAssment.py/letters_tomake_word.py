def create_strings_from_characters(frequencies, string1, string2):
    # Write your code here.
    can_create1 = can_create_string(frequencies,string1)
    can_create2 = can_create_string(frequencies,string2)

    if (not can_create1) or (not can_create2):
        
        if can_create1 or can_create2:
            return 1

        return 0
    for letter in string1+string2:
        if letter not in frequencies or frequencies[letter] == 0:
            return 1
        frequencies[letter] -=1
    return 2
def can_create_string(frequencies, string):
    for character in string:
        #the zero is the defult value if not present
        if string.count(character) > frequencies.get(character,0):
            return False

    return True