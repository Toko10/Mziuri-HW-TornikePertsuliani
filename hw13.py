class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        print(self.name, self.surname)
class School:
    def __init__(self, school_name, address):
        self.school_name = school_name
        self.address = address
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        self.students.pop(index)

    def show_students(self):
        for student in self.students:
            student.get_info()
school1 = School("Jasurbek's Public School", "Tbilisi")
student1 = Student("Tornike", "Pertsuliani", 15)
student2 = Student("Giorgi", "Beridze", 14)
student3 = Student("Nika", "Gelashvili", 16)
school1.add_student(student1)
school1.add_student(student2)
school1.add_student(student3)
print("Students list:")
school1.show_students()
school1.remove_student(1)
print("After removal:")
school1.show_students()