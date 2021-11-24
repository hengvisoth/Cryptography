import string

english_alphabets = string.ascii_lowercase
english_alphabets = english_alphabets.replace('j', '.')
print(english_alphabets)

# capture keyword

keyword = input("Enter keyword:")

# create the key matrix 5x5 - list
key_matrix = ['' for k in range(5)]

# populate the 5x5 key matrix with value
row = 0  # row variable 0<=row<5
column = 0  # column variable 0<=column<5

# Traverse teh keyword and if the char is not present in key matrix add it to the key matrix

for char in keyword:
    if char in english_alphabets:
        key_matrix[row] += char
        english_alphabets = english_alphabets.replace(char, '.')
        print(english_alphabets)
        column += 1

        if column > 4:
            row += 1
            column = 0

for char in english_alphabets:
    if char != '.':
        key_matrix[row] += char
        column += 1

        if column > 4:
            row += 1
            column = 0

print("The Key matrix:", str(key_matrix))

# inputting cipher text
cipher_text = str(input("Enter the cipher text : "))

# replace j with i
# plain_text = plain_text.replace("j", "i")

# Rule No.1 create / split the string modified plain text to diagram - Rule (a)-no identical
# rule(b): end character if alone should be accompanied by filler

plaintext_diagram = []  # list in which we will append the diagaram
ciphertext_diagram = []

i = 0

while i < len(cipher_text):
    char1 = cipher_text[i]  # char1 = first char of the diagram
    char2 = cipher_text[i+1]              # char2 = 2nd character of the diagram

    ciphertext_diagram.append(char1 + char2)
    i+=2


# print the diagram
print()
print("Cipher text Diagram ", str(ciphertext_diagram))

# rule no.2 if both the letter are from the same row of the key matrix
# replace each with letter to the right (wrapping back to start from end)

plaintextpair = []  # empty list

for pair in ciphertext_diagram:
    applied_rule = False

    for row in key_matrix:
        if pair[0] in row and pair[1] in row:  # both character in diagram are in the same row
            j0 = row.find(pair[0])
            j1 = row.find(pair[1])

            # we just captured the column number of both the character in the plain text diagram
            pt_pair = row[(j0 + 4) % 5] + row[(j1 + 4) % 5]
            plaintextpair.append(pt_pair)
            applied_rule = True

    if applied_rule:
        continue

# Rule No.3 : if both the character in the diagram belongs to the same column,
# replace the character below (wrap if necessary, Logic : xy - x and y belong to the same column J and row i1)
#  y - col J but row i2 [j denoted column]

    for j in range(5):
        col = "".join([key_matrix[i][j] for i in range(5)])
        if pair[0] in col and pair[1] in col:
            i0 = col.find(pair[0])
            i1 = col.find(pair[1])

            pt_pair = col[(i0 + 4) % 5] + col[(i1 + 4) % 5]
            plaintextpair.append(pt_pair)
            applied_rule = True

    if applied_rule:
        continue

    # ciphertextPairs.append(" ")

# rule No.4 if the letters are not on teh same row or column, replace them
# with letter on the same row respectively but at the other pair of corner
# of the rectangle defined by the original pair

#  the order is importance - the first letter of the encrypted
# pair is the one that ies on the same row as the first letter of the plain text

#  row and column of the first character in the diagram
    i0 = 0
    j0 = 0
#  row and column of the second character in the diagram
    i1 = 0
    j1 = 0
    for i in range(5):
        row = key_matrix[i]

        if pair[0] in row:
            i0 = i
            j0 = row.find(pair[0])

        if pair[1] in row:
            i1 = i
            j1 = row.find(pair[1])
    pt_pair = key_matrix[i0][j1] + key_matrix[i1][j0]

    plaintextpair.append(pt_pair)

print()
print("plain text diagram", plaintextpair)
print()
print("plain Text :" + "".join(plaintextpair))
