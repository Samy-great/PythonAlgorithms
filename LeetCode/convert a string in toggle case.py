#wap to convert a string  in toggle case
a=input("enter a string = ")
b=""
for i in a :
    if i.islower():
        b+=i.upper()
    elif i.isupper():
         b+=i.lower()
    else:
        b+=i
print(b)
