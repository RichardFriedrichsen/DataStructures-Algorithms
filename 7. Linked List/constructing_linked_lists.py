class linkedListNode:


    ##### Blue Print for a linked List #### 
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

    ##### Constructing a Linked List manually #####
node1 = linkedListNode(3)
node2 = linkedListNode(4)
node3 = linkedListNode(5)
node4 = linkedListNode(6)

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

currentNode = node1
while True:
    print(f"{currentNode.value} ->")
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode

class linkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node

        else:
            currentNode = self.head
            while True:
                if currentNode.nextNode is None:
                    currentNode.nextNode = node
                    break
                currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.nextNode
        print("None")

myLinkedList = linkedList()
myLinkedList.insert(1)
myLinkedList.insert(2)
myLinkedList.insert(3)

myLinkedList.printLinkedList()

