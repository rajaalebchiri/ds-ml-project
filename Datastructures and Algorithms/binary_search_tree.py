#!/usr/bin/env python
""" Binary Search Tree """
import random


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        """insert a node"""
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if self.val > val:
            if self.left is None:
                self.left = BSTNode(val=val)
                return
            self.left.insert(val=val)
            return
        if self.val < val:
            if self.right is None:
                self.right = BSTNode(val=val)
                return
            self.right.insert(val=val)
            return

    def get_min(self):
        """return min value"""
        if self.left is None:
            return self.val
        return self.left.get_min()

    def get_max(self):
        """return the maximum value"""
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        """delete a node from the tree"""
        if self is None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        """check if the value exists"""
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

    def inorder(self, vals):
        """return the three values in order"""
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals


if __name__ == '__main__':
    tree = BSTNode(13)
    for _ in range(6):
        number = random.randint(1, 23)
        print("inserting", number)
        tree.insert(number)
    minimum = tree.get_min()
    print("Min:", minimum)
    maximum = tree.get_max()
    print("Max:", maximum)
    print("2 Exists:", tree.exists(2))
    print(tree.inorder([]))
