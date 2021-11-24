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

# inputting plain text
plain_text = str(input("enter string:"))

# remove space from plain text
plain_text = plain_text.replace(" ", "")

# replace j with i
plain_text = plain_text.replace("j", "i")

# Rule No.1 create / split the string modified plain text to diagram - Rule (a)-no identical
# rule(b): end character if alone should be accompanied by filler

plaintext_diagram = []  # list in which we will append the diagaram
ciphertext_diagram = []

i = 0

while i < len(plain_text):
    char1 = plain_text[i]  # char1 = first char of the diagram
    char2 = ''              # char2 = 2nd character of the diagram

    if (i + 1) == len(plain_text):
        char2 = 'x'

    else:
        char2 = plain_text[i + 1]

    if char1 != char2:
        plaintext_diagram.append(char1 + char2)
        i = i + 2
    else:  # mean both character in the diagram are the same and add teh filler to char 1
        plaintext_diagram.append(char1 + 'x')

        i += 1


# print the diagram
print()
print("plain text converted to diagram:", str(plaintext_diagram))

# rule no.2 if both the letter are from the same row of the key matrix
# replace each with letter to the right (wrapping back to start from end)

ciphertextPairs = []  # empty list

for pair in plaintext_diagram:
    applied_rule = False

    for row in key_matrix:
        if pair[0] in row and pair[1] in row:  # both character in diagram are in the same row
            j0 = row.find(pair[0])
            j1 = row.find(pair[1])

            # we just captured the column number of both the character in the plain text diagram
            ct_pair = row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
            ciphertextPairs.append(ct_pair)
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

            ct_pair = col[(i0 + 1) % 5] + col[(i1 + 1) % 5]
            ciphertextPairs.append(ct_pair)
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
    ct_pair = key_matrix[i1][j0] + key_matrix[i0][j1]

    ciphertextPairs.append(ct_pair)

print()
print("cipher text diagram", ciphertextPairs)
print()
print("plain text:", plain_text)
print("Cipher Text :" + "".join(ciphertextPairs))
