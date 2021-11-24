user_input = input("Enter the message : ")
user_input1= ""

string = "abcdefghijklmnopqrstuvwxyz"
shift = int(input("Shift : "))
res =""
for i in user_input:
    if i == " ":
        res += " "
        continue
    index = string.find(i)


    a = (index + shift)%26

    res +=string[a]

print("Result : ",res)
