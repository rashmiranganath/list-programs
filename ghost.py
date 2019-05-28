list=[[2,0,9],[0,6,0],[1,2,2]]
i=0
count=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if i==0:
            if list[i+1][j]!=0:
                count=count+list[i][j]
        elif i==1 :
            if list[i+1][j]!=0 and list[i-1][j]!=0:
                count=count+list[i][j]
        elif i==2:
            if list[i-1][j]!=0:
                count=count+list[i][j]        
        j=j+1
    i=i+1
print count



def ghost(list):
    i=0
    count=0
    while i<len(list):
        j=0
        while j<len(list[i]):
            if i==0:
                if list[i+1][j]!=0:
                    count=count+list[i][j]
            elif i==1 :
                if list[i+1][j]!=0 and list[i-1][j]!=0:
                    count=count+list[i][j]
            elif i==2:
                if list[i-1][j]!=0:
                    count=count+list[i][j]        
            j=j+1
        i=i+1
    print count
a=[[2,0,9],[0,6,0],[1,2,2]]
ghost(a)

        
            
























1































1
