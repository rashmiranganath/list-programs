list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

i=0
new=[]
while i<len(list1):
	j=0
	k=j+1
	new1=0
	while j<len(list1)-1:
		if list2[i]<list2[k]:
			new.append(list1[i])
			list1.remove(list1[j])
			new.sort
			
		k=k+1
		j=j+1
	i=i+1
print new
	

