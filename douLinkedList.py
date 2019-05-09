class Nodes:
    def __init__(self,data=None):
        self.prev = None
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = Nodes()

    def insertBack(self,data):
        newNode = Nodes(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
        newNode.prev = cur

    def insertFront(self,data):   
        newNode = Nodes(data)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode 
        
    def printList(self):
        cur = self.head
        arr = []
        while cur: 
            if cur.data != None:
                arr.append(cur.data)
            cur = cur.next
        print(arr)

    def remove(self,gone):
        cur = self.head
        print("-------",gone,"will be gone -----")
        while cur:
            if cur.data == gone:
                cur.prev.next = cur.next    
            cur = cur.next

    def reverseOrder(self):
        print("  <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        cur = self.head
        lastOne = None
        nextOne = None
        cur = cur.next
        while cur:
            nextOne = cur.next
            cur.next = lastOne
            lastOne = cur
            cur = nextOne
        self.head = lastOne

list = linkedList()
list.insertBack(1)
list.insertBack(20)
list.insertBack(3)
list.insertBack(400)
list.insertBack(55)
list.insertBack('*')
list.insertBack('*')
list.insertBack(800)
list.printList()
#print("----------------------")
list.insertFront('~Head~')
list.insertFront(10000)
list.printList()
#list.remove(3)
list.reverseOrder()
list.printList()




