class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curNdx = 0
        tempNode = self.head
        if not self.head:
            return -1
        
        while tempNode.next and curNdx != index:
            tempNode = tempNode.next
            curNdx+=1
       
        return tempNode.val if curNdx == index else -1

        

    def addAtHead(self, val: int) -> None:
        #Create new node
        node = ListNode(val)

        #Maintain ordering of the list
        oldNode = self.head
        self.head = node
        node.next = oldNode
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return
        #Create new node
        node = ListNode(val)

        tempNode = self.head
        while tempNode.next:
            tempNode = tempNode.next
        
        tempNode.next = node
        node.next = None
        self.size+=1
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        node = ListNode(val)
        #stop 1 before
        tempNode = self.head
        curNdx = 0
        while curNdx != (index - 1):
            tempNode = tempNode.next
            curNdx+=1
        
        nextNode = tempNode.next
        tempNode.next = node
        node.next = nextNode
        self.size+=1
        
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        #stop 1 before
        tempNode = self.head
        curNdx = 0
        while curNdx != (index - 1):
            tempNode = tempNode.next
            curNdx+=1
        
        deleteNode = tempNode.next
        tempNode.next = deleteNode.next if deleteNode else None
        self.size-=1
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
