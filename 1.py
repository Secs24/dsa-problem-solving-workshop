# math = 50
# name = "prashant"
# pi = 3.14
# result = True
# print(type(math))
# print(type(name))
# print(type(pi))
# print(type(result))

# math = 50
# name = "prashant"
# pi = 3.14
# result = True
# print(id(math))
# print(id(name))
# print(id(pi))
# print(id(result))

# math = 50
# chem = 50
# phy = 50
# hindi = 40
# print(id(math))
# print(id(chem))
# print(id(phy))
# print(id(hindi))

# print(2+2)
# print("2"+"2")
# val1 = int(input("Enter the value of val1 :"))
# val2 = int(input("Enter the value of val2 :"))
# print(val1 + val2)
# print(int(3.14))
# print(int(True))
# print(int(False))
# print(int("4"))

# print(float(3))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float("4"))


# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex(5))
# print(complex(5.6))
# print(complex("5.6"))
# print(complex(True,False))

# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# print(bool())

# val1 = int(input("Enter the value of val1:"))
# val2 = int(input("Enter the value of val2:"))
# print("Before swapping val1",val1)
# print("Before swapping val2",val2)
# temp = val1
# val1 = val2
# val2 = temp
# print("After swapping val1",val1)
# print("After swapping val2",val2)


# a = int(input("Enter the value of val1:"))
# b = int(input("Enter the value of val2:"))

# print("Before swapping val1",a)
# print("Before swapping val2",b)
# a=a+b
# b=a-b
# a=a-b

# print("After swapping val1",a)
# print("After swapping val2",b)

#calculate %

# p1 = int(input("Enter the marks of p1:"))
# p2 = int(input("Enter the marks of p2:"))
# p3 = int(input("Enter the marks of p3:"))
# total = p1+p2+p3
# percentage = total/3.0
# print("Total =", total)
# print("percentage=",percentage)

# calculate simple int

# p_amount =int(input("Enter principal amount :"))
# roi = int(input("Enter the rate of intrest :"))
# time = int(input("Enter the duration of loan amount :"))

# si = p_amount*roi*time/100
# print("simple intrest=",si)

# wap to enter height in ft and convert it into inch &cm

# height = int(input("Enter the height in feet"))

# inch = height * 12
# cm = inch * 2.54

# print("height in inch:" ,inch)
# print("height in cm:" ,cm)

# reverse the no

# num =123 #321
# a = num %10 #a=3
# num = num // 10 #num = 12
# b= num % 10 #b =2
# num = num // 10 #num = 12
# c= num // 10 #c=1
# rev = a*100+b*10+c*1
# print(rev)

#reverse no

# num =123456 #654321
# a = num %10 #a=3
# num = num // 10 #num = 12
# b= num % 10 #b =2
# num = num // 10 #num = 12
# c= num % 10 #c=1
# num = num // 10 #num = 12
# d= num%10
# num = num // 10 #num = 12
# e=num % 10
# num = num // 10 #num = 12
# f= num %10
# num = num // 10 #num = 12

# rev = a*100000+b*10000+c*1000+d*100+e*10+f*1
# print(rev)


#identity operators

# a = 10
# b = 10
# print(a is b)
# print(a is not b)

# a = 10
# b = 15
# print(a is b)
# print(a is not b)


#membership operator

# name ="help4code"
# print("Z" not in name)
# print("p" in name)


#wap to accept any one no and check pos, neg &zero

# no = int(input("Enter any one no :"))
# if no>0:
#     print("Positive no")
# if no<0:
#     print("Negative no")
# if no ==0:
#     print("no is zero")        


# enter 5 no and find the greatest

#a = int(input("enter no 1:"))
# b = int(input("enter no 2:"))
# c = int(input("enter no 3:"))
# d = int(input("enter no 4:"))
# e = int(input("enter no 5:"))

# if a>b and a>c and a>d and a>e:
#     print(a," is greatest")
# if b>a and b>c and b>d and b>e:
#     print(b," is greatest")
# if c>b and c>a and c>d and c>e:
#     print(c, "is greatest")
# if d>b and d>c and d>a and d>e:
#     print(d, "is greatest")    
# if e>b and e>c and e>d and e>a:
#     print(e, "is greatest")    


#login 

# username = input("Enter username:")
# password = input("Enter password:")
# if username == password:
#     print("Login successful")
# else:
#     print("Invalid Credentials")    


#wap a program to accept phy,chem 7maths sub marks calculate total &percentage and if percentage is greater than or equal to 60 and gender is equal to male so he is elligable for placement else elligable for data entry job


# phy = int(input("enter physics marks:"))
# chem = int(input("enter chemistry marks:")) 
# math = int(input("enter math marks:"))
# gender = input("enter gender:")
# total = phy + chem + math
# per = total/3.0
# if per >= 60 and gender == "male":
#     print("eligible for placement") 
# else:    print("eligible for data entry")


#nested if else: wap to accept value of A,B,C and find max value


# p1 = int(input("enter any no:"))
# p2 = int(input("enter any no:"))
# p3 = int(input("enter any no:"))

# if p1 > p2:
#     if p1 >p3:
#         print(p1,"is greater")
#     else:
#         print(p3,"is greater")
# else:
#     if p2>p3:
#        print(p2,"is greater")
#     else:
#         print(p3, "is greater")




# day = input("enter your day")

# if day == "saturday" or day =="SATURDAY" or day == "sunday" or day=="Sunday":
#     print("Weekend")
# else:
#     print("working day")    


#wap to accept any one character from keyboard and check it is in upper case,lower case digit and special symbol so print message with respect to entered value:


# char = ord(input("enter any char:"))
# if char >=65 and char<=91:
#      print("it is a character is in uppercase")
# elif char>=97 and char<=122:
#      print("it is a character is in lowercase")
# elif char>=48 and char<=57:
#      print("it is a number")
# else:
#     print("it is a special character")



# Amount = int (input("please enter the amount for withdraw:"))
# print(" 100 notes= ",Amount//100)
# print(" 50 notes= ",(Amount%100)//50)
# print(" 50 notes= ",((Amount%100)%50)//20)
# print(" 50 notes= ",(((Amount%100)%50)%20)//10)
# print(" 50 notes= ",((((Amount%100)%50)%20)%10)//5)
