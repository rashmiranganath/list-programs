list_1 = [1,2]
list_2 = [0,3,9,5]
list_3 = []
i = 0
j = 0
k = 0
while i < len(list_1) and j < len(list_2):





def getFibNumber(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return getFibNumber(number-1) + getFibNumber(number-2)

i=1
while i<10:
    print getFibNumber(i)
    i=i+1
		


