class ExceptionDemo:
    def divide(self):
        try:
            a = int(input("Enter numerator: "))
            b = int(input("Enter denominator: "))
            result = a / b
            print("Result: ", result)
        except ZeroDivisionError:
            print("Error: Division by zero error occurs")
        except ValueError:
            print("Error: Input must be an integer")

    def accesslist(self):
        try:
            l = []
            n = int(input("Enter number of elements in list: "))
            for i in range(n):
                num = int(input(f"Enter element {i+1}: "))
                l.append(num)  # Corrected indentation
            index = int(input("Enter index to find element: "))
            print("Element at index:", index, "is", l[index])
        except IndexError:
            print("Error: Index is out of range")
        except ValueError:
            print("Error: Invalid input type")

    def accessdict(self):
        try:
            d = {}
            n = int(input("Enter number of key-value pairs: "))
            for i in range(n):
                key = input("Enter key: ")
                value = input("Enter value: ")
                d[key] = value
            search = input("Enter key to find value: ")
            print("Value: ", d[search])
        except KeyError:  # Corrected case from keyError to KeyError
            print("Error: Key not in dictionary")
        except ValueError:
            print("Error: Invalid input type")

obj = ExceptionDemo()
print("--- Division ---")
obj.divide()
print("\n--- List Access ---")
obj.accesslist()
print("\n--- Dictionary Access ---")
obj.accessdict()
