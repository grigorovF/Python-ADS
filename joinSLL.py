class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insertData (self, data):
        newNode = SLLNode(data)

        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
    
    def toList(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
def mergedSLL(list1, list2):
    mergedList = SLL()

    curr1, curr2 = list1.head, list2.head

    while curr1 or curr2:
        for _ in range(2):
            if curr1:
                mergedList.insertData(curr1.data)
                curr1 = curr1.next

        for _ in range(2):
            if curr2:
                mergedList.insertData(curr2.data)
                curr2 = curr2.next
    
    while curr1:
        mergedList.insertData(curr1.data)
        curr1 = curr1.next

    while curr2:
        mergedList.insertData(curr2.data)
        curr2 = curr2.next

    return mergedList

print("Enter values for the first linked list (space-separated):")
values1 = input().split()
list1 = SLL()
for value in values1:
    list1.insertData(int(value))

print("Enter values for the second linked list (space-separated):")
values2 = input().split()
list2 = SLL()
for value in values2:
    list2.insertData(int(value)) 

merged_list = mergedSLL(list1, list2)

print("Merged list:", merged_list.toList())