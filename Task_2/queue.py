from collections import deque

shuttle_queue= deque()

# implementing the enqueue
shuttle_queue.append('A')
shuttle_queue.append('B')
shuttle_queue.append('C')

print(shuttle_queue)

# implementing the dequeue
shuttle_queue.popleft()
print(shuttle_queue)

# implementing the front operation
x=shuttle_queue[0]
print(x)

# implementing the is_empty operation
if len(shuttle_queue)==0:
    print('queue is empty')
else:
    print('queue is not empty')

