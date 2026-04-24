class bill:
    def __init__(self,units):
        self.units=units
    def billamount(self):
        if self.units<=100 and self.units>=0:
            return 0
        elif self.units<=200 and self.units>=100:
            return 1.5*self.units
        elif self.units<=300 and self.units>=200:
            return ((self.units-200)*2.5)+(1.5*100)
        elif self.units<=400 and self.units>=300:
            return ((self.units-300)*4)+(1.5*100)+(2.5*100)
        elif self.units>400:
            return ((self.units-400)*5)+(1.5*100)+(2.5*100)+(4*100)
    def display(self):
        electricbill=self.billamount()
        print("Electicity bill:",electricbill)
units=int(input("Enter units:"))
u=bill(units)
u.display()
