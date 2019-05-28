i=0
while i<5:
    print "*" * i
    i=i+1
j=i-1
while j<0:
    print "*" * j
    j=j-1

i=1
j=1
space1=5
space2=5
while i<5 and j<=5 and space1>0:
    print i * "*",space2*" ",space1 * " ",j * "*"
    space1=space1-1
    space2=space2+1
    j=j+1
    i=i+1


i=1
space=7
while i<5:
    print i*"*",
    print space * " ",
    print i*"*"
    i=i+1
    space=space-2
else:
    print i*"*",i*"*"

list = [2,5,8,6,9,6,3]
list2 = [2,3,8,6]
i=0
j=0
while i<len(list)-1 and j<len(list2)-1:
    if list[i]==list2[j]:
        if list[i+1]==list2[j+1]:
            a= True
        else:
            a= False
        j=j+1
    i=i+1
print a


list = [2,5,8,6,9,6,3]
list2 = [2,5,8]
i=0
j=0
a=False
while i<len(list)-1 and j<len(list2)-1:
    if list[i]==list2[j]:
        if list[i+1]==list2[j+1]:
            a= True
        else:
            a= False
        j=j+1
    i=i+1
print (a)


list = [2,5,8,6,9,6,3]
list2 = [2,8]
i=0
j=0
result=""
while i<len(list)-1 and j<len(list2)-1:
    if list[i]==list2[j]:
        if list[i+1]==list2[j+1]:
            result= True
        else:
            result= False
        j=j+1
    i=i+1
print (result)


string = "my name is rashmi"
i=0
new=[]
a = " "
while i<len(string):
    if string[i]!=" ":
        a=a+string[i]
    else:
        new.append(a)
        a= " "
    i+=1
new.append(a)
print (new)

        

            



            
