#wap to find frequency of given character in a string
a=input("enter string : ")
c=input("enter search character : ")
b=0
for i in a :
    if i == c :
        b+=1
print("total character found = ",b)
