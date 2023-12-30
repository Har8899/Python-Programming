import collections

q = collections.deque()
print(q)

q.appendleft(10)
q.appendleft(20)
q.appendleft(30)

print(q)

q.pop()

print(q)

q1 = collections.deque()
print(q1)

q1.append(10)
q1.append(20)
q1.append(30)

print(q1)

q1.popleft()

print(q1)
