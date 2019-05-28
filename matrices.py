def matrices(a,b):

	i=0
	while i<len(list1):
		j=0
		while j<len(list1):
			if list1[i]==list2[i]:
				result="matrices are identical"
			else:
				result="matrices are not identical"
			j=j+1
		i=i+1
	print result

list1=[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
list2=[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]

matrices(list1,list2)
	
