import string
english_alphabets =string.ascii_lowercase
english_alphabets = english_alphabets.replace("j",".")

# capture the keyword
keyword = input("Enter the keyword : ")

# Creating the key_matrix 5x5 list

key_matrix = [""for k in range(5)]
print(f"Key Matrix is {key_matrix}")

# Populate the 5x5 key matrix with values

row = 0 # 0 <= row < 5
column = 0 # 0 <= column <= 5

for char in keyword:
    if char in english_alphabets:
        key_matrix[row] += char
        english_alphabets = english_alphabets.replace(char, '.')
        column += 1

        if column > 4:
            row = row + 1
            column = 0

for char in english_alphabets:
    if char != "." :
        key_matrix[row] += char
        column+=1

        if column > 4 :
            row += 1
            column = 0

for i in range(0,5):
    for j in range(0,5):
        print(key_matrix[i][j]+" ",end="")
    print("\n")

# Step 1 Creating digrams out of the plain text
plain_text = input("Enter the plain text : ")

# remove spaces from the plain text

plain_text = plain_text.replace(" ", "")

# replae j's wiht i's

plain_text = plain_text.replace("j","i")


# Create / Split the modified plain_text to digrams - Rule (a) - no identical characters in a diagram
# rule (b) : end character if alon should be accompanied by a filler x
plaintext_diagrams = [] # list to whicih we will append the digrams
i = 0

while i < len(plain_text) :
    char1 = plain_text[i] # char 1 represent first character of the diagram
    char2 = '' #char 2 represents second character of the diagram

    if (i+1) == len(plain_text) :
        char2 = "x"
    else :
        char2 = plain_text[i+1]
    if char1 != char2 :
        plaintext_diagrams.append(char1+char2)
        i=i+2
    else : # both character in the diagram are same so spli and add filler to char 1
        plaintext_diagrams.append(char1+"x")

        i = i + 1

print("Plain Text Diagrams",plaintext_diagrams)

# Rule 1 : If both letters of the digram fall in the same row of the key matrix
# replace each with letter to right ( wrapping back to start from end )
ciphertextpairs = []
for pair in plaintext_diagrams:
    applied_rule = False
    for row in key_matrix :
        if pair[0] in row and pair[1] in row: # if both characters in the digram are in the same row
            j0 = row.find(pair[0])
            j1 = row.find(pair[1])
            # we just captured the column numbers of both characters in the plain text diagram
            ct_pair= row[(j0 + 1)%5]  + row[(j1+1)%5]
            ciphertextpairs.append(ct_pair)
            applied_rule = True
    if applied_rule :
        continue

# Rule No 2: If both the characters in a digram belongs to the same column replace each
# with the character below ( wrap if necessary. Logic : xy -x and y belongs to the same coumn j and
    for j in range(5) :
        col = "".join([key_matrix[i][j] for i in range(5)])
        if pair[0] in col and pair[1] in col :
            i0 = col.find(pair[0])
            i1 = col.find(pair[1])

            ct_pair = col[(i0 + 1) % 5 ] + col[(i1 + 1 ) % 5 ]
            ciphertextpairs.append(ct_pair)
            applied_rule = True

        if applied_rule :
            continue

# Rule N.O 3
    # Row and Column of first character in the diagram
    i0 = 0
    j0 = 0
    # Row and column of 2nd character in the diagram
    i1 = 0
    j1 = 0
    for i in range(5) :
        row = key_matrix[i]
        if pair[0] in row :
            i0 = i
            j0 = row.find(pair[0])
        if pair[1] in row :
            i1 = i
            j1 = row.find(pair[1])
    ct_pair = key_matrix[i0][j1] + key_matrix[i1][j0]
    ciphertextpairs.append(ct_pair)


res = "".join(ciphertextpairs)


print("Cipher Text : "+str(ciphertextpairs))
print(res)
