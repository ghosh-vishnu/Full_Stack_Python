# class Details:
#     a=10
#     b=5
#     c=10+5
# sum=Details()
# print(sum.c)
# print(sum.a)


# class car:
#     color='Red'
#     model='SUV'
# car1=car()
# print(car1.color)
# print(car1.model)

# class car:
#     def start(self):
#         print("Start Car")
# car_start=car()
# car_start.start()


class student:
    def __init__(self,name,age):
        self.name=name
        self.agee=age
        print(f"Hello {name} your age is {age}")

s1=student("Vishnu",18)
print(s1.age)
print(s1.name)
        