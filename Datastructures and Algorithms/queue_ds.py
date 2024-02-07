#!/usr/bin/env python
"""Queue in Python"""

import queue
from collections import deque

# Queue in Python using List

print("Using List")

queue_list = []

queue_list.append("a")
queue_list.append("b")
queue_list.append("c")

print("Initial Queue")
print(queue_list)

# extract element in FIFO Order
print("Removing element", queue_list.pop(0))
print("Queue after element popped", queue_list)

# Queue in Python using collections.deque

print("\nUsing collections.deque")

queue_deque = deque()

queue_deque.append("a")
queue_deque.append("b")
queue_deque.append("c")

print("Initial Queue using deque")
print(queue_deque)

# extract element in FIFO Order using popleft()
print("Removing element", queue_deque.popleft())
print("Queue after element popped", queue_deque)

# Queue in Python using queue module

print("\nUsing queue module")

queue_queue = queue.Queue(maxsize=3)

print("number of items in the queue", queue_queue.qsize())

# add items to the Queue

print("Adding items to queue a b c")
queue_queue.put("a")
queue_queue.put("b")
queue_queue.put("c")

print("Full: ", queue_queue.full())
print("Size: ", queue_queue.qsize())

# dequeue item from the queue
print("removing item", queue_queue.get())

print("Size: ", queue_queue.qsize())
