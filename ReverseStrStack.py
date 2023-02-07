def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()


def isEmpty(stack):
    if len(stack) == 0:
        return true


def reverse(string):
	stack=[]
	string= ""
	n = len(string)
    for i in range(0, n):
        stack.append(i)
    for i in range(0, n):
        string += pop(stack)
        
    return string


string = input("enter string: ")
string = reverse(string)
print("Reversed string is " +string)