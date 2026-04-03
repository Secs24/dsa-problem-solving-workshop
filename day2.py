# indexing

# name = "prashant jha"
# # indexing = 012345678910
# print(name[0]) #p
# print(name[1]) #r
# print(name[-1]) #a
# #print(name[15])Error Error string index out of range
# print(name[0:5]) # end= -1, 5-1=4 prash
# print(name[1:]) #rashant jha
# print(name[:5]) # 5-1=4 prash
# print(name[:]) #prashant jha
# print(name[1:8:2]) # 8-1=7 rsat
# print(name[::-1])

#-------------------------------------------------

# s = "Python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

#-----------------------------------------------------------

# print('Subject Marks:')
# phy = 50
# chem = 60
# math = 70
# print("physics={} chemistry={} math={} ".format(phy,chem,math))
# print("physics={0} chemistry={1} math={2} ".format(phy,chem,math))
# print("physics={x} chemistry={y} math={z} ".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("Total Marks",f"{total} ")
# print("Roll No=","7".zfill(4))

#---------------------------------------------------------------

# for i in range(5): # i=0
#     print(i)

#----------------------
# for i in range(1,11,2): #i=5
#     print(i)

#-----------------------------------------------
# for i in range(1,11):
#     print(i*2) #i=4

#------------------------------

# for i in range(1,11):
#     print(i*2,"\t",i*3,"\t", i*4,"\t", i*5,"\t", i*6,"\t", i*7,"\t",i*8,"\t", i*9,"\t", i*10,"\t",)
# print()
# for i in range(1,11):
#     print(i*11,"\t",i*12,"\t", i*13,"\t", i*14,"\t", i*15,"\t", i*16,"\t",i*17,"\t", i*18,"\t", i*19,"\t", i*20,"\t")

#-------------------------------------------------

# name = "racear"
# for i in name: 
#     print(i)


# wap to remove duplicates

# name = "racear"
# newname = ""
# for i in name:
#     if i not in newname:
#         newname += i
# print(name)
# print(newname)        


#--------------------------------------------------

# for i in range(5,0,-1):
#     print(i)



# for i in range(10,0,-2):
#     print(i)

#-----------------------------------------
# wap a program to reverse the string using for loop

# name = "ganesh"
# newname =""
# n = len(name)
# for i in range(n-1,-1,-1):
#     newname += name[i]
# print(newname)

#-------------------------------------------------

#wap to check a given string is palindrome

# name = "ganesh"
# print(name)
# print(name[::-1])

# if name == name[::-1]:
#     print("palindrome string")
# else:
#     print("Not a Palindrome string")

#-----------------------------------------------------------------------------

