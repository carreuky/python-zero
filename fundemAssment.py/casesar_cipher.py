

def verison_1_caesar_cipher(string='hello', offset=3):
    # make arr of alphabet
    # find the idex of the given on each letter
    # will subtract by number given
    # add take the index and use with arr to place twe arr
    # use jion to finish it off.
    result =[]
    alphabet =['a','b','c','d','e','f','g','h',
               'i','j','k','l','m','n','o','p',
               'q','r','s','t','u','v','w','x','y','z']
    
    for i in range(len(string)):
        letter = string[i]
        num = alphabet.index(letter)
        
        idx_num = abs(num-offset)%26
        result.append(alphabet[idx_num])
        
    return ''.join(result) 
        
      
        
def caesar_cipher(string, offset):

    alphabet =['a','b','c','d','e','f','g','h',
               'i','j','k','l','m','n','o','p',
               'q','r','s','t','u','v','w','x','y','z']
    encoded_string = ''
    
    for character in string:
        position = alphabet.index(character)
        offset_position = position - offset
        
        # No need to handle negative positions because of negative indexing
        encoded_character = alphabet[offset_position]
        encoded_string += encoded_character

    return encoded_string