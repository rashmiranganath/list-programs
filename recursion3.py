def factorial(number):
    if number==1:
        return 1
    return number * factorial(number - 1)

i=5
while i>0:
	print factorial(i),
	i=i-1
