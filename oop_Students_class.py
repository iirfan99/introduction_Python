class Student :
    def __init__(self,name,age,grade,gender):
        self.name=name
        self.age=age
        self.gender=gender
        self.grade=grade


    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender


class Course:

   def __init__(self,name,max_students):
       self.name=name
       self.max_students=max_students
       self.students=[]

   def add_student(self,student):
    if len(self.students) < self.max_students:
       self.students.append(student)
       return True
    else :
       print("you exceeded the limit capacity of the lesson !! ")

   def get_average_grade(self):
     value =0
     for student in self.students:
           value +=student.get_grade()

     return value/len(self.students)


a1 = Student("Kamil",26,90,"Male")
a2 = Student("Tim ",23,80,"Male")
a3 = Student("Aslı",21,78,"Female")
print("Student name:",a1.name,",","Student age:",a1.age,",","Student grade:",a1.grade,",","Student gender:",a1.gender)
print("Student name:",a2.name,",","Student age:",a2.age,",","Student grade:",a2.grade,",","Student gender:",a2.gender)
print("Student name:",a3.name,",","Student age:",a3.age,",","Student grade:",a3.grade,",","Student gender:",a3.gender)
course=Course("Linear algebra",3)
course.add_student(a1)
course.add_student(a2)

print(course.get_average_grade())
print(course.add_student(1))

course=Course("Differential equations",2)
course.add_student(a3)
course.add_student(a2)
print(course.get_average_grade())
print(course.add_student(3))

course=Course("Mathematical analysis",1)


