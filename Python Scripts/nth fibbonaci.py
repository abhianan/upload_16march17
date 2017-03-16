input_num=input()
temp=0
temp1=0
temp2 =1
if input_num == 1:
    print "The Number is 0"
if input_num == 2:
    print " The Number is 1"
else:
    traversal = 2
    while traversal < input_num:
        temp= temp1 + temp2
        temp1 = temp2
        temp2 = temp
        traversal = traversal + 1
    print temp