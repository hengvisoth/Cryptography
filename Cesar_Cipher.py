import string
special_character = "!@#$%^&*():;,.'/][{}<>"

# define the encrypt function
def encrypt(text,s):
    result = ""
    for char in text :
        # ENCRYPT UPPER CASE
        if char.isupper():
            result+=chr(((ord(char) + s -65) % 26 ) + 65 )
        elif char.islower():
            result += chr(((ord(char) + s -97) % 26 ) + 97 )
        elif char.isspace():
            result+=char
        elif char.isdigit():
            x = str((int(char)+s)%10)
            result+=x
        elif char in special_character :
            result += special_character[(special_character.index(char)+s)%22]


    return result

def decrypt(text,s):
    result = ""
    for char in text :
        if char.isupper() :
            result += chr(((ord(char) - s -65)%26)+65)
        elif char.islower():
            result += chr(((ord(char) - s - 97) % 26) +97)
        elif char.isspace():
            result+= char
        elif char.isdigit():
            x = 0
            x = str((10 - s + int(char)) % 10 )
            result+=x
        else :
            result+=special_character[(special_character.index(char)-s)%22]
    return result
# Capture the plain text
text = str(input("Enter the plain text : "))
# number of shift
s = int(input("Shift : "))

cipher_text = encrypt(text,s)
print("Cipher Text : ",cipher_text)
cip = input("Enter ")
de_res = decrypt(cip,s)
print("Decrypt Text : ",de_res)
