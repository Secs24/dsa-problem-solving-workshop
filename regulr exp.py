# import re  # re module for performing all the regular expression based operation  
# count=0    # to count the number of matching found  
# pattern = re.compile("python")# string converts into bytecode  
# # print(pattern)  
# matcher = pattern.finditer("A function in python is defined by a def statement. python The general syntax looks like this: def function name(Parameter list): statements, i.e. the function body. The parameter python list consists of none or more parameters. ")  
# #print(matcher)  
# for i in matcher:   
#     count+=1   
#     print(i.start(),"...",i.end(),"...",i.group())  
# print("The number of occurrences: ",count)


#------------------------------------------------------------------------------------------------------------------------------------------

# import re    
# count=0   
# matcher=re.finditer("Hi","HiHiHiHi")  
# # print(matcher)  
# for i in matcher:# loop 4 times execute  
#     count+=1   
#     print(i.start(),"...",i.end(),"...",i.group())  
# print("The number of occurrences: ",count) 

#---------------------------------------------------------------------------------------------------------------------------------------------

# import re  
# obj = input("enter any charecter")  
# objmatch=re.finditer(obj,"a7b @k9z")  
# #print(objmatch)  
# for match in objmatch:  
#     print(match.start(),"...",match.end(),"...",match.group())

#--------------------------------------------------------------------------------------------------------------------------------------------

# import re 
# a= input("enter string to perform match operation:")
# mtch= re.match(a,"python is very important language")
# print(mtch)
# if mtch!=None:
#     print("match found at begining level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("there is no matching at begining level")

#-------------------------------------------------------------------------------------------------------------------------------------------
# import re 
# a = input("Enter the string to perform match operation:")
# match = re.fullmatch(a, "pythonisvery")
# print(match)
# if match!=None:
#     print("match found")
#     print(match.start()," ",match.end())
# else:
#     print("There is no matching at beginning level")


#-------------------------------------------------------------------------------------------------------------------------------------------

# # searh() function 
# -if the match found anywhere in the string then it return object else it will returnNone.

# import re
# a = input("Enter a string to perform search operation:")
# mtch = re.search(a, "python is very important language")
# print(mtch)
# if mtch != None:
#     print(mtch.start(), " ", mtch.end(), " ", mtch.group())
# else:
#     print("There is no matching")

#-------------------------------------------------------------------------------------------------------------------------------

# import re
# a=input("Enter the string:")
# f=open("myabc.txt","r")
# c=f.read()
# mtch= re.search(a,c)
# print(mtch)
# if mtch!=None:
#     print("match found at the beginning level")
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("there is no matching at beginning level")


#-------------------------------------------------------------------------------------------------------------------------------

# import re
# mtch = re.findall('[0-9]',"abch3hdh5bk7ZQ$&")
# print(mtch)


#-----------------------------------------------------------------------------------------------------------------------------------

# import re 
# obj = re.sub('[a-zA-Z]','X','2345 ABCD Fabc deff')
# print(obj)

#-----------------------------------------------------------------------------------------------------------------------------------
# import re
# mo = input("Enter the number:")
# obj=re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print("valid number")
# else:
#     print("invalid number")


#-----------------------------------------------------------------------------------------------------------------------------------


# import re
# s = input("Enter email id: ")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
# if m != None:
#     print("valid email id")
# else:
#     print("invalid email id")


#-----------------------------------------------------------------------------------------------------------------------------------


# import os,sys
# fname=input("Enter the file name:")
# if os.path.isfile(fname):
#     print("File exists:",fname)
#     f=open(fname,"r")
# else:
#     print(fname,"is not a file")
#     sys.exit(0)
# print("The content of the file is:")
# data=f.read()
# print(data)