#!/usr/bin/env python
"""Heap in Python"""

import heapq

lis = [100, 2, 33, 40, 4, 5]

# convert list into heap using heapify
heapq.heapify(lis)

print("the converted list", lis)

# adding elements to the heap
print("adding 500")
heapq.heappush(lis, 500)

# printing modified heap
print("\nThe modified heap after push is : ", end="")
print(list(lis))

# using heappop() to pop smallest element
print("\nThe popped and smallest element is : ", end="")
print(heapq.heappop(lis))
print("the new heap is", list(lis))

# using heappushpop
print("\nThe popped item using heappushpop(lis, 20) is: ", end="")
print(heapq.heappushpop(lis, 20))
print("the new heap is", list(lis))

# Find Largest and Smallest elements

# using nlargest to print 3 largest numbers
print("\nThe 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, lis))

# using nsmallest to print 3 smallest numbers
print("\nThe 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, lis))
