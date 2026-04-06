# class student:

#     roll_no = 101

#     def studentData(self):
#         print("student information")

# obj = student()
# print(obj.roll_no)
# obj.studentData()


#--------------------------------------------------------------------------------------------------------------------
# class Demo:
#     def __init__(self):
#         print("I am constructor")

#     def msg(self):
#         print("Hello class!")

# obj1 = Demo()
# obj2 = Demo()
# obj1.msg()



#------------------------------------------------------------------------------------------

# class Hod:
#     def __init__(self):
#         self.name = "prashant jha"
#         self.age=53
#         self.empid=1001
#     def info(self):
#         print("My name is :", self.name)
#         print("My age is", self.age)
#         print("My empid is", self.empid)
# obj= Hod()
# obj.info()

#-------------------------------------------------------------------------------------------------------------------------

# class Hod:
#     def __init__(self,name,age,rollno):
#         self.name = "prashant jha"
#         self.age=53
#         self.empid=1001
#     def info(self):
#         print("My name is :", self.name)
#         print("My age is", self.age)
#         print("My empid is", self.empid)
# obj= Hod('Arjun',45,101)
# obj.info()


#--------------------------------------------------------------------------------------------------------------------------

# class New:
#     def __init__(self):
#         self.a = 10
    
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a =20
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


#------------------------------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self):
#         self.name ="prashant"
#         self.rollno ="101"

#     def getdata(self):
#         self.s_mb =282828208

# obj = Student()
# obj.getdata()
# del obj.s_mb
# obj.s_branch = "cs"
# print(obj.__dict__)            

#----------------------------------------------------------------------------------------------------------------

# class New:
#     a = 10

# def __init__(self):
#         self.name="prashant"

# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)
# New.a = 50
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)


#------------------------------------------------------------------------------------------------------------------------

# import sys

# class CRUD:
#     def __init__(self):
#         print("Student management system")
#         self.studentId = []
#         self.studentName = []
#         self.studentMarks = []
#         self.studentRollNo = []
#         self.studentMobileNo = []

#     def addStudent(self):
#         self.studentId.append(input("Enter studentId: "))
#         self.studentName.append(input("Enter studentName: "))
#         self.studentMarks.append(input("Enter studentMarks: "))
#         self.studentRollNo.append(input("Enter studentRollNo: "))
#         self.studentMobileNo.append(input("Enter studentMobileNo: "))

# obj = CRUD()
# obj.addStudent()


#---------------------------------------------------------------------------------------------------------------------


# class student:
#     def __init__(self,name,rollno,mob):
#         self.name = name
#         self.rollno = rollno
#         self.mob = mob

#     def display(self):
#         print(self.name," ",self.rollno," ", self.mob)

# stud = student("prashant",1001,646464646)
# stud.display()


#----------------------------------------------------------------------------------------------------------------------


# class student:
#     @staticmethod
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=" ,firstname ,lastname)

#     @staticmethod
#     def contact_detail(mobile_no,rollno):
#         print("your contact detail" ,mobile_no,rollno)
# student.get_personal_detail("prashant","jha")
# student.contact_detail("56545654","1001")


#-------------------------------------------------------------------------------------------------------------------------


# class Principal:
#     def role(self):
#         print('I am managing all activity of college')
# class Dean:
#     def role(self):
#         print('Dean= I am decision taking person')

# class Hod:
#     def role(self):
#         print('Hod= I have responsibilities of Teachers and students')

# class Faculty:
#     def role(self):
#         print('Faculty= I have to complete Syllabus Successfully')

#         # class declaration completee 

# def func(obj):
#     obj.role()
# campus=[Principal(),Dean(),Hod(),Faculty()]
# for obj in campus:
#     func(obj)

#------------------------------------------------------------------------------------------------------------------------


# class Arithmatic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None:
#             print(a+b)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         else:
#             print("Invalid")

# obj = Arithmatic()
# obj.add(10,20)
# obj.add(10,20,30)
# obj.add(10)


#------------------------------------------------------------------------------------------------------------------------
# class Arithmatic:
#     def __init__(self):
#         print("There is no argument")
#     def __init__(self,a):
#         print("Passing one argument")
#     def __init__(self,a,b):
#         print("Passing two arguments")

# # obj = Arithmatic()
# # obj = Arithmatic(10)
# obj = Arithmatic(2,2)


#---------------------------------------------------------------------------------------------------------------------
# class Rbi:
#     def home_loan(self):
#         print("Home Loan = 7.5")
#     def carLoan(self):
#         print("Car Loan 8%")

# class Sbi(Rbi):
#     def home_loan(self):
#         print("sbi provide home loan = 6.5")
#         super().home_loan()

# obj = Sbi()
# obj.home_loan()
# obj.carLoan()


#----------------------------------------------------------------------------------------------------------------------
# class Father:
#     def __init__(self):
#         print("Father:= i am allready at breakfast table")

# class Child:
#     def __init__(self):
#         print("Child:= I will be late for breakfast")

# obj = Child()

