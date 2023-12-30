stack = []

def push():
    element = input("Enter the element :")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print('stack is empty')

    else:
        e = stack.pop()
        print('stack element removed :', e)
        print(stack)

while True:
    print(" select the operation 1=push, 2=pop, 3=quit")
    choice = int(input("operation :"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice ==3:
        print("quitting operation")
        break
    else:
        print('choose correct operation')
