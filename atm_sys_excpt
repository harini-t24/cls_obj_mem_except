class InvalidPINError(Exception): pass
class AccountBlockedError(Exception): pass

class ATM:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.attempts = 0

    def verifyPin(self, enteredpin):
        try:
            if self.attempts >= 3:
                raise AccountBlockedError
            if enteredpin != self.pin:
                self.attempts += 1
                raise InvalidPINError

            print("PIN verified successfully")
            self.attempts = 0 # Reset attempts on success
            return True
        except InvalidPINError:
            print(f"Incorrect PIN. Attempts left: {3 - self.attempts}")
            return False
        except AccountBlockedError:
            print("Account Blocked Error")
            return False

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: {amount}")
            print(f"Remaining Balance: {self.balance}")

# Main Logic
name = input("Enter your name: ")
pin = int(input("Enter your PIN: "))
balance = float(input("Enter your Balance: "))
user = ATM(name, pin, balance)

while user.attempts < 3:
    enteredpin = int(input("Verify PIN to proceed: "))
    if user.verifyPin(enteredpin):
        choice = input("Do you want to withdraw? (yes/no): ")
        if choice.lower() == "yes":
            amount = float(input("Enter amount: "))
            user.withdraw(amount)
        break
else:
    print("Account Blocked: Too many incorrect attempts.")
