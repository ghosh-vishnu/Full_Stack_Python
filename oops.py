# # # # class Details:
# # # #     a=10
# # # #     b=5
# # # #     c=10+5
# # # # sum=Details()
# # # # print(sum.c)
# # # # print(sum.a)


# # # # class car:
# # # #     color='Red'
# # # #     model='SUV'
# # # # car1=car()
# # # # print(car1.color)
# # # # print(car1.model)

# # # # class car:
# # # #     def start(self):
# # # #         print("Start Car")
# # # # car_start=car()
# # # # car_start.start()


# # # class student:
# # #     def __init__(self,name,age):
# # #         self.name=name
# # #         self.agee=age
# # #         print(f"Hello {name} your age is {age}")

# # # s1=student("Vishnu",18)
# # # print(s1.age)
# # # print(s1.name)
        
        
        
# # # def add(a,b):
# # #     return a+b
# # # a=add(5,8)
# # # b=add(8,78)
# # # print(a,b)

# # # def name():
# # #     print("I am Vishnu")
# # # name()

# # class Animal():
# #     def sound(self,a):
# #         if a=='Cow':
# #             print("Moo")
# #         elif a=="cat":
# #             print("Meuw")
# #         else:
# #             print("Wrong Animal Name")
# # z=Animal()
# # z.sound("Cow")
# # z.sound('cateee')    

# # ============================================================

# # class Student():  # Blueprint
# #     def __init__(a,Name,Grade):  # __init__ Constructor (auto-call hota hai), self/a  Object of refrence      
# #         a.name=Name  # Attributes
# #         a.grade=Grade #Attributes
# #     def get_nameeeee(a):  # Features/Method/Properties
# #         print(f"Hello My Name is {a.name} and my Marks is {a.grade}")
# # student1=Student("Vishnu",560)   # Object Instances
# # student2=Student("Amint",780)   # Object Instances
# # student1.get_nameeeee()  # Method Calling
# # student2.get_nameeeee()  # Method Calling



# # ==============================================Modify Attributes========================
# # class Student():  # Blueprint
# #     def __init__(a,Name,Grade,cl):  # __init__ Constructor (auto-call hota hai), self/a  Object of refrence      
# #         a.name=Name  # Attributes
# #         a.grade=Grade #Attributes
# #         a.Class=cl
# #     def get_nameeeee(a):  # Features/Method/Properties
# #         print(f"Hello My Name is {a.name} and my Marks is {a.grade}")
# # student1=Student("Vishnu",560,"MCA")   # Object Instances
# # student2=Student("Amint",780,"B.Tech")   # Object Instances
# # student1.grade=700
# # # student1.name()

# # student1.get_nameeeee()  # Method Calling
# # # student2.get_nameeeee()  # Method Calling

# # #=====================================View Object Data ===================================
# # print(student1.__dict__)
# # #===================================Delete Attributes====================================
# # del student1.Class

# # student1.get_nameeeee()  # Method Calling
# # # ===================================Delete Object===========================
# # del student1

# # # Pillars of Oops
# # > 1. Abstraction    
# # > 2. Encapsulation
# # > 3. Inheritance
# # > 4.Polymorphism

# # 1.Abstraction
# # User  ko sirf result dikhta hai lofic hide rehta hai

# # class Student():  # Blueprint
# #     def __init__(a,Name,Grade,cl,Percentage):  # __init__ Constructor (auto-call hota hai), self/a  Object of refrence      
# #         a.name=Name  # Attributes
# #         a.grade=Grade #Attributes
# #         a.Class=cl
# #         a.percentage=Percentage
# #     def get_nameeeee(a):  # Features/Method/Properties
# #         print(f"Hello My Name is {a.name} and my Marks is {a.grade} and his marks percentage is {a.percentage+2}%")
# # student1=Student("Vishnu",560,"MCA",95)   # Object Instances
# # student2=Student("Amint",780,"B.Tech",69)   # Object Instances
# # # student1.grade=700
# # # student1.name()

# # student1.get_nameeeee()  # Method Calling
# # student2.get_nameeeee()  # Method Calling

# class Student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     # def __calculate_grade(self):  # Encapsulation//Protected
#     #     if self.marks>=90:
#     #         return "A"
#     #     elif self.marks>=75:
#     #         return 'B'
#     #     else:
#     #         return 'C'
#     # def show_result(self):  # method/features
#     #     grade=self.__calculate_grade()  #abstraction

#     def get_grade(self):
#         grade=self.calculate_grade
#         print(f"Hi {self.name} you got {grade} grade")   
        
# s1=Student("Rahul",78)
# s1.get_grade()




