class Nodes:
    def __init__(self,data=None):
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

    def printList(self):
        cur = self.head
        arr = []
        while cur: 
            if cur.data != None:
                arr.append(cur.data)
                #print(cur.data)
            cur = cur.next
        print(arr)

    def length(self):
        cur = self.head
        n=0
        while cur.next != None:
            n+=1
            cur = cur.next
        print("length is: ",n)

    def lookfor(self,key):
        cur = self.head
        i=0
        cur = cur.next
        while cur:          
            if cur.data == key:     
                #print("the index of ",key,"is ", i)
                cur=cur.next
                return i
            else:   
                cur=cur.next
            i+=1

    def remove(self,gone):
        cur = self.head
        goneIdx = self.lookfor(gone)
        #print("-------",gone,"will be gone -----")
        curIdx = 0
        while cur: 
            prev = cur
            cur = cur.next
            if goneIdx == curIdx:
                prev.next = cur.next
            curIdx+=1

    def findDupe(self):
        cur = self.head
        dupe = []
        print("*********** remove dupe ************")
        while cur.next != None:
            nextOne = cur.next 
            while nextOne:
                if cur.data == nextOne.data:
                    dupe.append(nextOne.data)
                    self.remove(nextOne.data)
                nextOne = nextOne.next
            cur = cur.next
        #print("dupes:", dupe)

    def reverseIterative(self): 
        print("  <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        cur = self.head
        prev = None
        cur = cur.next
        while cur:
            nextAddress = cur.next
            cur.next = prev             
            prev = cur       
            cur = nextAddress
        self.head=prev


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
list.length()
list.reverseIterative()
list.printList()
list.findDupe()
list.printList()
#list.remove(55)



'''
n = int(input("how long? \n"))
print("What are nodes?")
for i in range(0,n):  
    nodes = str(input()) 
    list.insertFront(nodes) 
'''
'''
def remove(self,gone):
        while cur:              #does NOT work with ODD index
            prev = cur
            cur = cur.next
            if cur.data == gone:
                prev.next=cur.next
            cur = cur.next
''' 