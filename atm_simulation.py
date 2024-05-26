import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, pin, initial_balance):
        self.pin = pin
        self.balance = initial_balance

    def check_pin(self, input_pin):
        return self.pin == input_pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulation")
        self.account = Account("1234", 1000.00)

        self.create_login_window()

    def create_login_window(self):
        self.clear_window()

        self.labelPin = tk.Label(self.root, text="Enter PIN:")
        self.labelPin.pack()

        self.entryPin = tk.Entry(self.root, show="*")
        self.entryPin.pack()

        self.buttonSubmit = tk.Button(self.root, text="Submit", command=self.submit_pin)
        self.buttonSubmit.pack()

    def create_main_menu(self):
        self.clear_window()

        self.buttonBalance = tk.Button(self.root, text="Balance Inquiry", command=self.balance_inquiry)
        self.buttonBalance.pack()

        self.buttonDeposit = tk.Button(self.root, text="Deposit Funds", command=self.deposit_funds)
        self.buttonDeposit.pack()

        self.buttonWithdraw = tk.Button(self.root, text="Withdraw Funds", command=self.withdraw_funds)
        self.buttonWithdraw.pack()

        self.buttonExit = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.buttonExit.pack()

    def balance_inquiry(self):
        self.clear_window()

        self.labelBalance = tk.Label(self.root, text=f"Current Balance: ${self.account.balance:.2f}")
        self.labelBalance.pack()

        self.buttonBack = tk.Button(self.root, text="Back", command=self.create_main_menu)
        self.buttonBack.pack()

    def deposit_funds(self):
        self.clear_window()

        self.labelDepositAmount = tk.Label(self.root, text="Enter deposit amount:")
        self.labelDepositAmount.pack()

        self.entryDepositAmount = tk.Entry(self.root)
        self.entryDepositAmount.pack()

        self.buttonConfirmDeposit = tk.Button(self.root, text="Confirm", command=self.confirm_deposit)
        self.buttonConfirmDeposit.pack()

        self.buttonBack = tk.Button(self.root, text="Back", command=self.create_main_menu)
        self.buttonBack.pack()

    def withdraw_funds(self):
        self.clear_window()

        self.labelWithdrawAmount = tk.Label(self.root, text="Enter withdrawal amount:")
        self.labelWithdrawAmount.pack()

        self.entryWithdrawAmount = tk.Entry(self.root)
        self.entryWithdrawAmount.pack()

        self.buttonConfirmWithdraw = tk.Button(self.root, text="Confirm", command=self.confirm_withdraw)
        self.buttonConfirmWithdraw.pack()

        self.buttonBack = tk.Button(self.root, text="Back", command=self.create_main_menu)
        self.buttonBack.pack()

    def submit_pin(self):
        input_pin = self.entryPin.get()
        if self.account.check_pin(input_pin):
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN. Please try again.")

    def confirm_deposit(self):
        try:
            amount = float(self.entryDepositAmount.get())
            self.account.deposit(amount)
            messagebox.showinfo("Success", f"Deposit successful. New balance: ${self.account.balance:.2f}")
            self.create_main_menu()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")

    def confirm_withdraw(self):
        try:
            amount = float(self.entryWithdrawAmount.get())
            if self.account.withdraw(amount):
                messagebox.showinfo("Success", f"Withdrawal successful. New balance: ${self.account.balance:.2f}")
            else:
                messagebox.showerror("Error", "Insufficient funds.")
            self.create_main_menu()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
