import random


class Student:
    def __init__(self,xeploai):
        self.list_student = []
        self.xeploai = xeploai

    def enter_info(self):
        so_luong = int(input("nhap so luong can them: "))
        for i in range(so_luong):
            name = input("nhap ten:")
            age = int(input("nhap tuoi: "))
            point = float(input("point student: "))
            xeploai = self.xep_loai(point)
            danh_sach = [name,age,point,xeploai]
            self.list_student.append(danh_sach)
        self.list_student = sorted(self.list_student,key=lambda x: x[2],reverse=True)


    def xep_loai(self,diem):
        if 8 < diem <= 10:
            return "gioi"
        elif 5 <= diem < 8:
            return  "trung binh"
        elif 0<= diem > 5:
            return "truot"
    def delet(self):
        list_studen = self.list_student
        name_need_detele = input("nhập thông tin để xoas sinh viên: ")
        for i in list_studen:
            if name_need_detele in i:
                list_studen.remove(i)
                print("da xoa sinh vien!")
                break

    def show_info(self):
        for i in self.list_student:
            print(f"ten: {i[0]}, tuoi: {i[1]}, mssv:{i[2]}, xep loai: {i[3]}")

    def random_info_student(self):
        self.list_student = random.choice(self.list_student)
        print("in thông tin sinh viên ngẫu nhiên: ")
        print(f"ten: {self.list_student[0]}, tuoi: {self.list_student[1]}, mssv:{self.list_student[2]}, xep loai: {self.list_student[3]}")


    def find_student(self):
        tim_ten_trong_danh_sach = input("nhap ten can tim: ")
        for i in self.list_student:
            if i[0] == tim_ten_trong_danh_sach:
                print(f"ten: {i[0]}, tuoi: {i[1]}, mssv:{i[2]}, xep loai: {i[3]}")

    def enter(self):
        while True:
            print("1. inter infor student")
            print("2. delete info student")
            print("3. print info studen random")
            print("4. print all student")
            print("5. Find info student")
            print("6. exit progame")
            chon = int(input("chọn chương trình: "))
            if chon == 1:
                self.enter_info()
            elif chon == 2:
                self.delet()
            elif chon == 3:
                self.random_info_student()
            elif chon == 4:
                self.show_info()
            elif chon == 5:
                self.find_student()
            elif chon == 6:
                break
            else:
                print("nhap lai!")

student = Student("")
student.enter()