def rotate_character(char, rot):
    letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if char.isalpha() is True:
        new_char = char.lower()
        rot_letter_position = alphabet_position(new_char) + rot

        if rot_letter_position > 25:
            while rot_letter_position > 25:
                rot_letter_position = rot_letter_position - 26
        rot_char =  letter_list[(rot_letter_position)]
        if char == new_char:
            return rot_char
        if char != new_char:
            rot_char = rot_char.upper()
            return rot_char
    else:
        return char

def alphabet_position(letter):
    letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter = letter.lower()
    letter_position = (letter_list.index((letter)))
    return letter_position

def encrypt(text, rot):
    encrypt_text = ("")
    text_list = list(text)
    for i in (text_list):
        rot_item = rotate_character(i,rot)
        encrypt_text = encrypt_text + rot_item
    return(encrypt_text)
