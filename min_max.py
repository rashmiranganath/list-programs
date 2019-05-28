def min(a):

	i=0
	min=list[i]
	while i<len(list):
		if list[i]<min:
			min=list[i]
		i=i+1
	print min
	j=0
	max=list[j]
	while j<len(list):
		if list[j]>max:
			max=list[j]
		j=j+1
	print max
	
	
list=[2,5,8,1,20,0]
min(list)
