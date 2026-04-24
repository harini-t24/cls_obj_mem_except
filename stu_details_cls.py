class Student:
    def __init__(self,name,roll_no,m1,m2,m3,m4,m5):
        self.name=name
        self.roll_no=roll_no
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def total(self,m1,m2,m3,m4,m5):
        total=m1+m2+m3+m4+m5
        return total
    def average(self,total):
        average=total/5
        return average
    def grade(self,average):
        if average>=90 and average<=100:
            return "O"
        elif average>=80:
            return "A+"
        elif average>=70:
            return "A"
        elif average>=60:
            return "B+"
        elif average>=50:
            return "B"
        else:
            return "F"
    def display_grade(self):
        total=self.total(self.m1,self.m2,self.m3,self.m4,self.m5)
        average=self.average(total)
        print("Name:",self.name)
        print("Roll no:",self.roll_no)
        print("Average:",average)
        print("Grade:",self.grade(average))
        print()
name=(input("Enter name:"))
roll_no=int(input("Enter roll no:"))
m1=int(input("Enter m1:"))
m2=int(input("Enter m2:"))
m3=int(input("Enter m3:"))
m4=int(input("Enter m4:"))
m5=int(input("Enter m5:"))
s=Student(name,roll_no,m1,m2,m3,m4,m5)
s.total(m1,m2,m3,m4,m5)
s.display_grade()
