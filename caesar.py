# helper module defining a few functions
# aka refactoring shared code

def alphabet_position(letter):
    if ord(letter)>=97 and ord(letter)<=122:
         return ord(letter)-97
    elif ord(letter)>=65 and ord(letter)<=90:
        return ord(letter)-65


def rotate_character(char, rot):
    if 97<=ord(char)<=122:
        return chr((alphabet_position(char) + rot) % 26 + 97)
    elif 65<=ord(char)<=90:
        return chr((alphabet_position(char) + rot) % 26 + 65)
    else:
        return char

def encrypt(text, rot):
    super_secret_message=""
    for letter in text:
        super_secret_message+=rotate_character(letter, rot)
    return super_secret_message
  
