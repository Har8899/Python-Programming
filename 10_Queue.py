import queue

q= queue.PriorityQueue()

q.put(1)
q.put(20)
q.put(21)
q.put(2)
q.put(30)

print(q.get())
