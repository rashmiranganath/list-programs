list=[1,6,7,2,1,6,1,2,1]
i=0
j=0
count=0
while i<len(list):
    while j<len(list):
        if list[i]==list[j]:
            count=count+1
            list.remove(list[i])
        j=j+1
    i=i+1
print count


list=[6,1,1,2,3,3,5,5,6]
i=0
count=0
while i<len(list):
    j=i+1
    while j<len(list):
        if list[i]==list[j]:
            count=count+1
            list.remove(list[j])
        j=j+1
    i=i+1
print count

    
    
        
    
    
        
