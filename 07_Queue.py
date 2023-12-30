queue = []

def enqueue():
    element = input('enter element: ')
    queue.append(element)
    print('element added ', element)


def dequeue():
    if not queue:
        print('queue is empty')
    else:
        e = queue.pop(0)
        print('element removed', e)

def display():
    print(queue)

while True:
    user = int(input('Enter your choice : 1-> addition, 2-> deletion, 3-> show, 4->to quit :'))
    if user ==1:
        enqueue()
    elif user ==2:
        dequeue()
    elif user ==3:
        display()
    elif user ==4:
        print('quitting program')
        break
    else:
        print(' Worng user input')

        
