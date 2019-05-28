def similar_element(list1,list2):
	i=0
	while i<len(list1):
		j=0
		while j<len(list2):
			if list1[i]==list2[j]:
				print "yes"
			j=j+1
		i=i+1
list1=[2,6,8]
list2=[3,2,9]
similar_element(list1,list2)

		
	


