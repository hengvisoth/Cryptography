#
# plain_text = input("Enter the plain text : ")
# key = "qwertyuiopasdfghjklzxcvbnm"
# encrypt = ""
# for char in plain_text :
#     if char.islower() :
#         index = ord(char) - ord("a")
#         print(f"Index of {char} is {index}")
#         encrypt += key[index]
#     elif char.isupper():
#         index = ord(char) - ord("A")
#         print(f"Index of {char} is {index}")
#         encrypt += key[index].upper()
#     else :
#         encrypt += char
#
# print("Encrypt Text : ",encrypt)

# Encrypt
text = input("Enter the plain text :")
key = "qwertyuiopasdfghjklzxcvbnm"
cipher_text = ""
for char in text :
    if char.islower() :
        ind = ord(char) - 97
        print(f"Index of {char} is {ind}")
        cipher_text += key[ind]
    elif char.isupper() :
        ind = ord(char) - 64
        print(f"Index of {char} is {ind}")
        cipher_text += key[ind]
    else :
        cipher_text += char
print(f"Cipher Text {cipher_text}")


#Decrypt monoalphabetic
text = input("Enter the Cipher Text :")
key = "qwertyuiopasdfghjklzxcvbnm"
cipher_text = ""
for char in text :
    if char.islower() :
        ind = key.find(char)

        #print(f"Index of {char} is {ind}")
        cipher_text += chr(ind+ord("a"))
    elif char.isupper() :
        ind = key.find(char)


        cipher_text += chr(ind+ord("A"))
    else :
        cipher_text += char
print(f"Plain text : {cipher_text}")
