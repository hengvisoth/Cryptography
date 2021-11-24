import string
import numpy as np

# Step1 : Generation of Key Matrix
# Taking the input dimensions - no.rows and col of key matrix
row_keymatrix = int(input("Enter the number of rows of the key matrix : "))
column_keymatrix = int(input("Enter the number of column of the key matrix : "))

key = []

# populate the key matrix
print("Enter the elements of the key matrix row wise = ")

# user input and create the key matrix
for i in range(row_keymatrix):
    a = []
    for j in range(column_keymatrix):
        a.append(int(input()))
    key.append(a)

print("The key matrix is : ")
key_matrix = np.array(key)
print(key_matrix)

# Step 2 : Accepting the plain text , add filler characters to match the D(Key_matrix)
plain_text = input("Enter the plain text : ")
plain_text = plain_text.replace(" ", "")

print()
print(plain_text)
# add filler characters to match the D(key_matrix)
while (len(plain_text) % row_keymatrix != 0):
    plain_text += 'x'

print("The Plain text after adding fillers : " + plain_text)
# Split the plain text
print("The lsit of plain text characters : ")
plain = list(plain_text)
print()
print(plain)
# cover lists of pt characters to numbers
plain_text_index = []
for char in plain:
    plain_text_index.append(ord(char) - ord('a'))

print(plain_text_index)
# creating the plain text matrix = numerical of characters
# rememmber that no. col of the plain text matrix = no. rows of key matrix
plain_text_matrix = np.array(plain_text_index)
rp = int(len(plain_text_matrix) / row_keymatrix)  # length of the plain text = 12 / 3 = 4
cp = row_keymatrix
plain_text_matrix.resize(rp, cp)
print("The Plain text matrix is", plain_text_matrix)

# Encryption : PT Matrix key (3x3) = matrix mul of matrices (P.K)
# O/ P = Cipher Text
encryption_matrix = np.matmul(plain_text_matrix, key_matrix)
print("Matrix before performing Mod 26 : ", encryption_matrix)

# Never ever forget mod 26 in hill ciphe

encryption_matrix = np.mod(encryption_matrix, 26)
print("Cipher Matrix afater Mod 26 : ",encryption_matrix)

#Dimension of Cipher Text = no.rows(PT Matrix) X no.col (Key_Matrix)
cipher_text_matrix = []
for i in range(rp):
    a=[]
    for j in range(column_keymatrix):
        a.append(chr(int(encryption_matrix[i][j]) + ord('a')))
    cipher_text_matrix.append(a)

print("The Cipher Text character matrix is : ",cipher_text_matrix)

cipher_text_matrix = np.array(cipher_text_matrix)
print(cipher_text_matrix)

print('List of plain text characters : ')
print(plain)
