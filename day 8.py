# import sys 
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     # add node
#     def addNode(self,value):
#         node = Node(value)
#         if self.head == None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node

#     def displayNode(self):
#         while self.head is not None:
#             print("|",self.head.data,"|","|",self.head.next,"->", end = " ") 
#             self.head = self.head.next
#             print()
#             print('--------------------------------------------')


# if __name__ == "__main__":
#     object = LinkedList()
    
#     while True:
#         print("1. add node in linkedlist")
#         print("2. add node in beginning")
#         print("3. add node in between")
#         print("4. add node in end")
#         print("5. display linkedlist")
#         print("6. exit")
#         choice = int(input("enter your choice : "))
#         if choice == 1:
#             value = int(input("enter value for node :"))
#             object.addNode(value)
#             print("Node added successfully")
#         elif choice == 2:
#             value = int(input("enter value for node :"))
#             object.addNodeInBeginning(value)
#             print("Node added successfully")
#         elif choice == 3:
#             value = int(input("enter value for node :"))
#             pos = int(input("enter position for node :"))
#             object.addNodeInBetween(value,pos)
#             print("Node added successfully")
#         elif choice == 4:
#             value = int(input("enter value for node :"))
#             object.addNodeInEnd(value)
#             print("Node added successfully")
#         elif choice == 5:
#             object.displayNode()
#         elif choice == 6:
#             break
#         else:
#             print("Invalid choice")

#-------------------------------------------------------------------------------------------------------------------------


# import sys
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def addNode(self,value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node

#     def addNodeBeggining(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             node.next = self.head
#             self.head = node

#     def addNodeinBetween(self,index, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         elif index == 0:
#             node.next = self.head
#             self.head - node
#         else:
#             temp = self.head
#             for _ in range(index - 1):
#                 temp = temp.next
#             node.next = temp.next
#             temp.next = node


#     def addNodeatEnd(self,value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node

#     def displayNode(self):
#         print("------------------------")
#         while self.head is not None:
#           print("|",self.head.data,"|","===>",end=" ")
#           self.head=self.head.next
#         print("------------------------")

    

# #link list add,del,
# if __name__ =='__main__':
#     object = Linkedlist()

#     while True:
#         print("1. Add node linkedlist:")
#         print("2. Add node in begining:")
#         print("3. Add node in between:")
#         print("4. Add node in end:")
#         print("5. Display linkedlist:")
#         print("6.exit")

#         ch = int(input("Enter your choice:"))
#         if ch == 1:
#             value = int(input("enter value for node:"))
#             object.addNode(value)
#             print("node added successfully insingle linkedlist")

#         elif ch == 2:
#             value = int(input("enter value for node:"))
#             object.addNodeBeggining(value)
#             print("node added successfully insingle linkedlist")

#         elif ch == 3:
#             value = int(input("enter value for node:"))
#             index = int(input("enter position after that you have to insert"))
#             object.addNodeinBetween(index,value)
#             print("node added successfully insingle linkedlist")


#         elif ch == 4:
#             value = int(input("enter value for node:"))
#             object.addNodeatEnd(value)
#             print("node added successfully insingle linkedlist")



#         elif ch == 5:
#             object.displayNode()

#         elif ch == 6:
#             sys.exit()

#         else:
#             print("Invalid choice")


#-------------------------------------------------------------------------------------------------------------------------


#WAP to remove only leading zeros from a list of integers using for loop
# s = [0,0,1,2,0,3,0,0,4]
# result = []
# started = False

# for num in s:
#     if num != 0:
#         started = True
#     if started:
#         result.append(num)

# print(s)
# print(result)

#-------------------------------------------------------------------------------------------------------------------------

