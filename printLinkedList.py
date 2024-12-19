import math
import os
import random
import re
import sys

class SLLNode:
    def __init__(self, nodeData):
        self.data = nodeData
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self, nodeData):
        nodeData = SLLNode(nodeData)

        if not self.head:
            self.head = nodeData
        else:
            self.tail.next = nodeData
        
        self.tail = nodeData

def printLinkedList(head):
    current = head
    while(current):
        print(current.data)
        current = current.next

if __name__ == '__main__':
    llist_count = int(input())

    llist = SLL()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.addNode(llist_item)

    printLinkedList(llist.head)
