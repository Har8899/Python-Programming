#Queue is the linear data structure where the elements is inserted from the one side
# and removed from the other
# Queue is open from both the ends
# thats why insertion and removal is done in different ends
# the end where elements are added are known as back/rear/tail of the queue
# the end where elements are removed is called head/front
# queue follo fifo or lilo methodology
# the process of adding element is called enqueue
# and the process of removing the element is called dequeue
# enqueue, dequeue, isFull, isEmpty


q = []

q.append(10)
q.append(20)
q.append(30)

print(q)

# lets pop first element
q.pop(0)

print(q)

# different way

q1 =[]
q1.insert(0,10)
q1.insert(0,20)
q1.insert(0,30)

print(q1)


