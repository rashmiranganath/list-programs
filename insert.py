list= [1,4,5,6,8,10]
i=0
j=1
while i<len(list)-1:
	if list[j]==list[i]+1:
		j=j+1
		i=i+1
	else:
		num=list[i]+1
		list.insert(i+1,num)
		j=j+1
		i=i+1
print list
