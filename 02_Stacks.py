# First in Last out or last in first out


# push for adding elements --> append
stack =[]
stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)


print(stack)


# pop for removing the element--> pop
stack.pop()
stack.pop()
stack.pop()
print(stack)

print(len(stack)==0)
print(not stack)
stack.pop()
print(not stack)
#peek or top to represent the element at the top
stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)

print(stack[-1])

# isempty whether stack is empty or not
