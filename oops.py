# # # class Details:
# # #     a=10
# # #     b=5
# # #     c=10+5
# # # sum=Details()
# # # print(sum.c)
# # # print(sum.a)


# # # class car:
# # #     color='Red'
# # #     model='SUV'
# # # car1=car()
# # # print(car1.color)
# # # print(car1.model)

# # # class car:
# # #     def start(self):
# # #         print("Start Car")
# # # car_start=car()
# # # car_start.start()


# # class student:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.agee=age
# #         print(f"Hello {name} your age is {age}")

# # s1=student("Vishnu",18)
# # print(s1.age)
# # print(s1.name)
        
        
        
# # def add(a,b):
# #     return a+b
# # a=add(5,8)
# # b=add(8,78)
# # print(a,b)

# # def name():
# #     print("I am Vishnu")
# # name()

# class Animal():
#     def sound(self,a):
#         if a=='Cow':
#             print("Moo")
#         elif a=="cat":
#             print("Meuw")
#         else:
#             print("Wrong Animal Name")
# z=Animal()
# z.sound("Cow")
# z.sound('cateee')    

# ============================================================

# class Student():  # Blueprint
#     def __init__(a,Name,Grade):  # __init__ Constructor (auto-call hota hai), self/a  Object of refrence      
#         a.name=Name  # Attributes
#         a.grade=Grade #Attributes
#     def get_nameeeee(a):  # Features/Method/Properties
#         print(f"Hello My Name is {a.name} and my Marks is {a.grade}")
# student1=Student("Vishnu",560)   # Object Instances
# student2=Student("Amint",780)   # Object Instances
# student1.get_nameeeee()  # Method Calling
# student2.get_nameeeee()  # Method Calling



# ==============================================Modify Attributes========================
class Student():  # Blueprint
    def __init__(a,Name,Grade,cl):  # __init__ Constructor (auto-call hota hai), self/a  Object of refrence      
        a.name=Name  # Attributes
        a.grade=Grade #Attributes
        a.Class=cl
    def get_nameeeee(a):  # Features/Method/Properties
        print(f"Hello My Name is {a.name} and my Marks is {a.grade}")
student1=Student("Vishnu",560,"MCA")   # Object Instances
student2=Student("Amint",780,"B.Tech")   # Object Instances
student1.grade=700
# student1.name()

student1.get_nameeeee()  # Method Calling
# student2.get_nameeeee()  # Method Calling

#=====================================View Object Data ===================================
print(student1.__dict__)
#===================================Delete Attributes====================================
del student1.Class

student1.get_nameeeee()  # Method Calling
