import collections
stack = collections.deque()
print(stack)

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print(stack)

stack.pop()
stack.pop()
stack.pop()
stack.pop()

print(not stack)
stack.append(10)
stack.append(20)

print(stack[-1])

 # not gonna show output
import queue
s1 = queue.LifoQueue(3)


s1.put(10)
s1.put(40)
s1.put(30)
s1.put(20)
print(s1[-1])

s1.get()
print(s1[-1])
s1.get()
s1.get()
print(s1[-1])
