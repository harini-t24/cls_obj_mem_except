class Employee:
    def __init__(self,name,age,designation,basic_pay):
        self.name=name
        self.age=age
        self.designation=designation
        self.basic_pay=basic_pay
    def salary(self):
        da=0.1*self.basic_pay
        hra=0.2*self.basic_pay
        gross=da+hra+self.basic_pay
        return gross
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Designation:",self.designation)
        print("Salary:",self.salary())
name=input("Enter your name:")
age=int(input("Enter your age:"))
designation=input("Enter your designation:")
basic_pay=int(input("Enter your basic pay:"))
e=Employee(name,age,designation,basic_pay)
e.salary()
e.display()
