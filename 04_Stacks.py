# we are creating stack list that will take input from user

def push():
    if len(stack) == e:
        print('stack is full')
    else:
        element = input("enter element :")
        stack.append(element)
        print(stack)

def pop():
    if not stack:
        print('stack is empty')
    else:
        p = stack.pop()
        print('element you pop:',p)
        print(stack)

stack = []
e = int(input('enter no. of elements you want to add :'))

while True:
    user = int(input('enter your choice -> 1= add element, 2 = delete element, 3 = quit program :'))
    if user == 1:
        push()
    elif user == 2:
        pop()
    elif user == 3:
        print('quitting program')
        break
    else:
        print('wrong information given')
