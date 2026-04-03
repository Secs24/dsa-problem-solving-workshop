# mylist = ["prashant", "ashish", "komal", "ankush", "ashish", "sandip" ,60.52 ,"prashant"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# mylist [2] = "Akshay"
# print(mylist) 


# if "ankush" in mylist:
#     print("yes ankush is available")
# else:
#     print('not available')    


# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)

# mylist.insert(1, "Nana")
# print(mylist)

# mylist.remove("Nana")
# print(mylist)


# newlist = mylist.copy()
# print(newlist)

#---------------------------------------------------------

# mylist = [['prashant','jha'],['85,56'],[440022,"yyy"]]
# print("example of multidimensional list")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

#---------------------------------------------------------------

# list1=["prashant", "jha"]
# print(list1*2)

# list2 = [50,25.50]
# print(list1+list2)

#----------------------------------------

# list2 =[50,25.50,'prashant']
# del list2[2]
# print(list2)

# list2 =[50,25.50,'prashant']
# list2.clear()
# print(list2)


# name="prashant"
# print(name)
# myname=list(name)
# print(myname)


# mylist = [40,30,20,10]
# mylist.reverse()
# print(mylist)

# mylist=[44,22,77,0,9,88]
# mylist.sort()
# print(mylist)


# mylist=[44,22,77,0,9,88]
# mylist.sort(reverse=True)
# print(mylist)


# mylist=[44,22,77,0,9,88]
# newlist= mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0]="prashant"
# print(mylist)
# print(newlist)


# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14 ,15]]
# for i in range(0,4):
#     print(arr[i].pop())



# arr = [1 ,2 ,3 ,4 ,5 ,6 ]
# for i in range(1,6):
#     arr[i-1] = arr[i]
# for i in range(0,6):
#     print(arr[i], end = "")



# a=[1,2,3,4,5,6,7,8,9]
# a[::2] =10,20,30,40,50 
# print(a)


# a=[1,2,3,4,5]
# print(a[3:0:-1])

mytuple = ("prashant" , "ashish" , "rahul" , "sandip" , "komal" , "ankush" , "rajesh" ,23,3.15,77,"sandip")

# print(mytuple)
# print(type(mytuple))

# mytuple[2]="sunil"
# print(mytuple)

# init_tuple = ()
# print(init_tuple.__len__())

# init_tuple_a = 'a','b'
# init_tuple_b = ('a','b')
# print (init_tuple_a == init_tuple_b)

# init_tuple = ('python',) * 3
# print(type(init_tuple))


# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple)

# init_tuple = ((1,2),)*7
# print(len(init_tuple[3:8]))


# names=[4,2,5,6,8,2]
# for i in names:
#     print(i)

#----------------------------------------------------------------

# A = [4,0,2,5,0,1]
# for i in A:
#     if i == 0:
#         A.remove(i)
#         A.append(i)
# print(A)


#---------------------------------------------------------------------------


# A = [1,2,2,3,4,4,5]
# newlist=[]
# for i in A:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)


#----------------------------------------------------------------------------


# A = [1,2,3]
# B =[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)


#---------------------------------------------------------------------------

# n = int(input("enter the size of the array"))
# arr=[]
# for i in range(n):
#     val=int(input("Enter the value of array:"))
#     arr.append(val)
# sum=0
# print(arr)
# for i in range(n):
#     if i+1 in range(n):
#         sum =abs(arr[i] - arr[i+1])
# print(sum)
    
#---------------------------------------------------------------------------

# for i in range(1,5):
#     if i==3:
#         continue
#     print(i)


#---------------------------------------------------------------------------


# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)


#---------------------------------------------------------------------------

#Wap to move *
# name = 'prashant*is*a*good*programmer'
# newname=''
# val=''
# for i in name:
#     if i !='*':
#         newname += i
#     else:
#         val+=i
# print(newname)
# print(str(val+newname))        

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)


#--------------------------------------------------------------------------

# x=['A',"B","C"]
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-

# 6
#--------------------------------------------------------------------------

a="this is sentence"
count = 1
for i in a:
    if i == " ":
        count += 1
print(count)


#--------------------------------------------------------------------------


