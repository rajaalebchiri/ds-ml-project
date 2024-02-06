#!/usr/bin/env python
"""Linked Lists"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_end(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        current_node = self.head
        while current_node:
            if current_node.data == target_node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        current_node = self.head
        while current_node:
            if current_node.next.data == target_node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        prev = self.head
        while prev:
            if prev.next.data == target_node_data:
                prev_next = prev.next
                prev.next = prev_next.next
                return
            prev = prev.next
        raise Exception("Node with data '%s' not found" % target_node_data)


if __name__ == "__main__":
    llist = LinkedList(["a", "b", "e"])
    print(llist)
    llist.add_first(Node("k"))
    print(llist)
    llist.add_end(Node("Kk"))
    print(llist)
    llist.add_after("b", Node("ui"))
    print(llist)
    llist.add_before("e", Node("hello"))
    print(llist)
    llist.remove_node("e")
    print(llist)
