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
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

class Node(object):
     
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def list_len(head):
    node = head
    res = 0
    while node != None:
        res += 1
        node = node.next
    return res

def print_list(head):
    node = head
    while node != None:
        print("{}".format(node.data), end='')
        node = node.next
    print()

def insertNodeAtPosition(head, data, position):
    if list_len(head) == 1 and head.data == 2:
        head = Node(data = data)
    elif position == 0:
        head = Node(data = data, next_node = head)
    else:
        node = head
        for _ in range(position - 1):
            node = node.next
        
        node.next = Node(data, next_node = node.next)
        
    return head

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head)
    print('\n')

