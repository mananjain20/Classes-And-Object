class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


# Creating objects
student1 = Student("Manan", 101, 98)
student2 = Student("Aarav", 102, 55)

# Using objects
student1.display_details()
print("-----------------")
student2.display_details()
