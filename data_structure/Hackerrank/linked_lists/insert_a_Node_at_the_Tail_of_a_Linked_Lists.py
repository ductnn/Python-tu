#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    # if head is None:
    #     head = Node(data)
    #     return head
    # else:
    #     if head.next is None:
    #         head.next = Node(data)
    #     else:
    #         insertNodeAtTail(head.next, data)
    #     return head

    if (head == None):
        head = Node(data)
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = Node(data)
    return head

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n')
    print('\n')

