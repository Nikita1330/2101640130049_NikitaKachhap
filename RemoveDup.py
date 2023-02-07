string="geeksforgeeks"
stack=[]
for ele in string:
	if ele not in stack:
		stack.append(ele)
for i in range(0,len(stack)):
	print(stack[i],end="")