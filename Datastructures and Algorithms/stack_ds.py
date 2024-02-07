#!/usr/bin/env python
"""Stack in Python"""
import queue
from collections import deque

# Stack in Python using List

print("Using List")

stack = []

stack.append("a")
stack.append("b")
stack.append("c")

print("Initial Stack")
print(stack)

# extract element in LIFO Order
print(stack.pop())
print("Stack after element popped", stack)

# Stack in Python using collections.deque

print("\nUsing collections.deque")

stack_deque = deque()

stack_deque.append("a")
stack_deque.append("b")
stack_deque.append("c")

print("Initial Stack using deque")
print(stack_deque)

# extract element in LIFO Order
print(stack_deque.pop())
print("Stack after element popped", stack_deque)

# Stack in Python using queue module

print("\nUsing queue module (LifoQueue)")

stack_queue = queue.LifoQueue(maxsize=3)

print("number of items in the stack", stack_queue.qsize())

# add items to the stack

stack_queue.put("a")
stack_queue.put("b")
stack_queue.put("c")

print("Full: ", stack_queue.full())
print("Size: ", stack_queue.qsize())

# pop items from the stack in LIFO Mode
print("remove last item", stack_queue.get())

print("Size: ", stack_queue.qsize())
