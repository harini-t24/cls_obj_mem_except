class BillingSystem:

    def __init__(self):
        self.items = []
        self.sub_tot = []
        self.total = 0

    def get_items(self, n):
        for i in range(n):
            name = input("Enter name: ")
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter price: "))
            self.items.append((name,quantity,price))
    def calculate_subtotal(self):
        for item in self.items:
            sub=item[1]*item[2]
            self.sub_tot.append(sub)
    def calculate_total(self):
        self.total = sum(self.sub_tot)
    def apply_discount(self):
        if self.total > 3000:
            discount = self.total * 10 / 100
        else:
            discount = 0
        self.total -= discount
        print("Total after discount:", self.total)

    def apply_gst(self):
        gst = self.total * 5 / 100
        self.total += gst
        print("Total after GST:", self.total)
        print("GST:", gst)

    def display(self):
        print("Items:", self.items)
        print("Sub totals:", self.sub_tot)


n = int(input("Enter number of elements: "))

obj = BillingSystem()

obj.get_items(n)
obj.calculate_subtotal()
obj.display()

obj.calculate_total()
print("Total before discount:", obj.total)

obj.apply_discount()
obj.apply_gst()
