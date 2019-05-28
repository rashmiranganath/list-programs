string = "rashmi ranganath"
i=0
space =" "
word=" "
while i<len(string):
    j=i
    if string[i]==space+str(j):
        letter = space +j
        word=word+letter
        j=j+1
    i=i+1
print word  


    
