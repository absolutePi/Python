# def hello():
#     print("hello")

# x=1  
# print(type(hello))
# string="hello"
# print(string.upper())
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        # print(name)

    # def add_one(self,x):
    #     return x+1

    # def bark(self):
    #     print("bark")
    # def get_name(self):
    #     return self.name
    # def get_age(self):
    #     return self.age
    # def set_age(self,age):
    #     self.age=age
# print(type(d))
# d.bark()
# print(d.add_one(5))
# d=Dog("Tim",34)
# d.set_age(23)
# d2=Dog("Bill",12)
# print(d.get_name())
# print(d2.get_name())
# print(d.get_age())
# print(d2.get_age())
# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade #0-100

#     def get_grade(self):
#         return self.grade

# class Course:
#     def __init__(self,name,max_students):
#         self.name=name
#         self.max_students=max_students
#         self.students=[]
    
#     def add_student(self,student):
#         if len(self.students)<self.max_students:
#             self.students.append(student)
#             return True
#         return False
    
#     def get_average_grade(self):
#         value=0
#         for student in self.students:
#             value+=student.get_grade()

#         return value/len(self.students)
# s1=Student("Tim",19,95)
# s2=Student("Bill",19,75)
# s3=Student("Jill",19,65)

# course=Course("Science",2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.add_student(s3))
# print(course.students[0].name)
# print(course.get_average_grade())
# class Pet:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
#     def speak(self):
#         print("I don't know what I say")
# class Cat(Pet):
#     def __init__(self,name,age,color):
#         super().__init__(name,age)
#         self.color=color
#     # def __init__(self,name,age):
#     #     self.name=name
#     #     self.age=age
#     def speak(self):
#         print("Meow")
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

# class Dog(Pet):
#     # def __init__(self,name,age):
#     #     self.name=name
#     #     self.age=age    
#     def speak(self):
#         print("Bark")

# class Fish(Pet):
#     pass
# p = Pet("Tim",19)
# # p.show()
# p.speak()
# c= Cat("Bill",34,"Brown")
# c.show()
# # c.speak()
# d=Dog("Jill",25)
# d.speak()
# f=Fish("Bubble",10)
# f.speak()
# class Person:
#     number_of_people=0

#     def __init__(self,name):
#         self.name=name
#         # Person.number_of_people+=1
#         Person.add_person()
#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people+=1
# p1 = Person("Tim")
# print(Person.number_of_people)
# p2 = Person("Jill")
# print(Person.number_of_people_())
# Person.number_of_people=8
# p2.number_of_people=8
# print(p1.number_of_people)
# print(Person.number_of_people)
class Math:
    @staticmethod
    def add5(x):
        return x+5
    @staticmethod
    def add10(x):
        return x+10
    @staticmethod
    def pr():
        print("run")
Math.pr()