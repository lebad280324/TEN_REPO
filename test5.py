class Student:
    def __init__(self):
        self.list_student = []

    def information_info(self):
        numbers = int(input("nhap so luong sinh vien can them: "))
        for i in range(numbers):
            ten = input("ten: ")
            age = int(input("tuoi: "))
            self.list_student.append((ten,age))

    def delete_f(self):
        can_xoa = input("nhap ten can xoa")
        for i in self.list_student:
            if can_xoa == i:
                self.list_student.remove(self.list_student[0])


    def show_info(self):
        for i in self.list_student:
            print(f"ten: {i[0]}, tuoi: {i[1]}")


    def enter_c(self):
        while True:
            print("1. add")
            print("2. view")
            i = int(input("enter:"))
            if i == 1:
                self.information_info()
            elif i == 2:
                self.delete_f()
            elif i == 3:
                self.show_info()
            else:
                print("nhap lai.")

students = Student()
students.enter_c()