# Linked Lists Second Version

# Singly Linked Lists
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

# Display Linked List - O(n)


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

# Search for node value - O(n)


def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False

# Doubly Linked Lists


class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


def display_doubly(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))

# insert at beginning Doubly linked lists- O(1)


def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

# Insert at end - O(1)


def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node


if __name__ == "__main__":
    Head = SinglyNode(1)
    A = SinglyNode(3)
    B = SinglyNode(4)
    C = SinglyNode(7)

    Head.next = A
    A.next = B
    B.next = C

    print(Head)

    # Traverse the list - O(n)
    current = Head

    while current:
        print(current)
        current = current.next

    # Display Linked List - O(n)
    display(Head)

    # Search for 2
    val = search(Head, 2)
    print(val)

    # Doubly Linked Lists
    Head = DoublyNode(9, next=None, prev=None)
    AA = DoublyNode(6, next=None, prev=None)
    BB = DoublyNode(8, next=None, prev=None)
    CC = DoublyNode(2, next=None, prev=None)

    Head.next = AA
    AA.prev = Head
    AA.next = BB
    BB.prev = AA
    BB.next = CC
    CC.prev = BB
    CC.next = None

    display_doubly(Head)

    print("Insert 15 at the beginning")
    head, tail = insert_at_beginning(Head, CC, 15)
    display_doubly(head)

    head = tail = DoublyNode(1)

    print("Insert 3 at the beginning")
    head, tail = insert_at_beginning(head, tail, 3)
    display_doubly(head)
    print("head, tail", head, tail)

    print("Insert 10 at the end")
    head, tail = insert_at_end(head, tail, 10)
    display_doubly(head)
