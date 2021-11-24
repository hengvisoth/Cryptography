# generate matrix
key_word = "kirirominstitute"
new_key_word = ""
text = "abcdefghiklmnopqrstuvwxyz"
ls=[]
k=0
# remove duplicate char in key_word
for chars in key_word.lower():
    if chars not in new_key_word:
        new_key_word+=chars

# remove key-word from text
for char in new_key_word :
    text = text.replace(char,"")


for i in range(0,5):
    element = ""
    for j in range(0,5):
        if j+(5*i) < len(new_key_word):
            element+=new_key_word[j+(5*i)]
        else:
            element+=text[k]
            k+=1
    ls.append(element)
for i in range(0,5):
    for j in range(0,5):
        print(ls[i][j]+" ",end="")
    print("\n")

