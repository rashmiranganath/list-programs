num = [3,5,0,7,2,5,1]
i = 0
var = num[i]
while i < len(num):
	if num[i] < var:
		var = num[i]
	i = i + 1
#num.remove(var)
j=0
var1=num[j]
while j<len(num):
	if num[j]<var1:
		var1=num[j]
	j=j+1
print var1

 