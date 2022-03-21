class Student:
    def __init__(self, name,id, department='MNS',courses=[],cgpa=0.00):
        self.name = name
        self.id = id
        self.department = department
        self.courses = courses
        self.cgpa = cgpa
        #
    def print_info(self):
        allow = ['MNS', 'CSE']
        if self.department in allow:
            print(f"Name:{self.name}\n"
                  f"ID:{self.id}\n"
                  f"Department:{self.department}\n"
                  f"Courses:{self.courses}\n"
                  f"CGPA: {self.cgpa}")
class SDS:
    def __init__(self, year):
        self.year = year
        self.cse = {}
        self.mns = {}
        print(f"chool of Data and Sciences {self.year}! Only CSE and MNS department students can be added.")
    def print_info(self):
        cse = len(list(self.cse.keys()))
        mns = len(list(self.mns.keys()))
        print(f"Number of CSE students: {cse}\n"
              f"Number of mns students: {mns}\n"
              f"CSE Students {self.cse}\n"
              f"MNS Students {self.mns}\n")

    def addStudent(self, *infos):
        for info in infos:
            if info.department=='CSE':
                self.cse[info.id] = [info.name, info.cgpa, info.courses]
            elif info.department=='MNS':
                self.mns[info.id] = [info.name, info.cgpa, info.courses]
            else:
                print(f'{info.department} department student cannot be added to SDS')

sds21 = SDS("2021")
print("*********************************************")
sds21.print_info()
print("1.================================")
s1 = Student("Maliha",21101001)
s1.print_info()
print("2.================================")
sds21.addStudent(s1)
sds21.print_info()
print("3.================================")
s2 = Student("Subha",21301001,"CSE", ["ENG091","MAT092"],3.48)
s2.print_info()
print("4.================================")
sds21.addStudent(s2)
sds21.print_info()
print("5.================================")
s3 = Student("Samiul",21305001,"MNS", ["ENG091","MAT092","PHY111"],3.01)
s4 = Student("Mohsina",21305023)
print("6.================================")
s3.print_info()
print("7.================================")
s4.print_info()
print("8.================================")
sds21.addStudent(s3,s4)
print("9.================================")
sds21.print_info()
print("10.================================")
s5 = Student("Nayla", 16101288, "BBS")
sds21.addStudent(s5)
print("11.================================")
sds21.print_info()
