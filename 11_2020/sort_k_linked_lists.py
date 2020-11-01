"""
Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

Merge pairs until everything is sorted.
"""

class LinkedList:
    class Node:
        value = None
        Next = None

    def __init__(self):
        self.start = None

    def insert(self, val):
        if self.start == None:
            self.start = self.Node()
            self.start.value = val
        else:
            new_node = self.Node()
            new_node.value = val
            new_node.next = self.start
            self.start = new_node
        
    def insert_odered(self, val):
        pointer = self.start

        if pointer is None:
            self.insert(val)

        while pointer is not None:
            if pointer.value > val:
                new_node = self.Node()
                new_node.value = pointer.value
                new_node.next = pointer.next
                pointer.value = val

            if pointer.next is None:
                new_node = self.Node()
                new_node.value = val

            pointer.next = new_node



    def merge(self, LL):
        n = LL.start
        while n is not None:
            self.insert_odered(n)





def merge_linked_lists(lst):

    sol = LinkedList()

    for l in lst:
        sol.merge(l)

    return sol
