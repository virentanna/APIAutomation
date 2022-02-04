# Program to implement Singly Linked List with following functionality
# Insert Node at Beginning, Append, Delete First/Last node, Print all nodes

class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        node = Node(value)
        self.head = node

    def insertFirst(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        print(value, ' Inserted at the Beginning...')

    def deleteFirst(self):
        self.head = self.head.next
        print('First node deleted...')

    def deleteLast(self):
        itr = self.head

        while itr.next:
            xNode = itr.next
            if xNode.next == None:
                break
            itr = itr.next

        itr.next = None
        print('Last node deleted...')

    def appendList(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node
        print(value, ' Appended...')

    def printList(self):
        itr = self.head
        llStr=''
        while (itr):
            llStr += str(itr.value) + '--->'
            itr = itr.next
        print(llStr)

if __name__ == '__main__':
    LL = LinkedList(10)
    LL.printList()
    LL.appendList(20)
    LL.printList()
    LL.appendList(30)
    LL.printList()
    LL.insertFirst(5)
    LL.printList()
    LL.deleteLast()
    LL.printList()
    LL.deleteFirst()
    LL.printList()
