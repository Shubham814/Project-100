import time
import sys
import random

class ATM(object):
    def __init__(self,name,account_no, phone_no, balance):
        self.name = name
        self.account_no = account_no
        self.phone_no = phone_no
        self.balance = balance

    # Making functions for functionality


    def accountDetails(self):
        print("\n\n____Account Details____ \n")
        print("Username        :",self.name)
        print("Account Number  :",self.account_no)
        print("Phone Number    : +91 ",self.phone_no)
        print("Account Balance : ₹",self.balance)

    def depositMoney(self):
        print("\n____Deposit Money____ \n")
        amount = int(input("Enter amount you want to deposit: ₹"))
        balance = self.balance + amount
        self.balance =  balance
        print("\nCurrent amount balance: ₹", self.balance)

    def withdrawMoney(self):
        print("\n____Withdraw Money____ \n")
        amount = int(input("Enter amount you want to withdraw: ₹"))
        print("Checking Balance......")
        time.sleep(2)

        # Checking sufficent amount
        if(self.balance > amount):
            balance = self.balance - amount
            self.balance =  balance
            print("\nCurrent amount balance: ₹", self.balance)
        else:
            print("\n!!!Insufficient amount of Money !!! \n")
            print(f"Your current Account Balance is ₹{self.balance}.")
            print(f"You can withdraw money lesser than ₹{self.balance}.")
            print("If you want more money you can deposit cash.")

    def checkBalance(self):
        print(f"\nYour Current Account Balance is: ₹{self.balance}.")

    def changePhoneNumber(self):
        print(f"\nYour Current Phone Number is {self.phone_no}.\n")
        choice = input("Do you want to change your Phone Number? (y/n): ")

        # Checking the choice
        if(choice == "y"):
            time.sleep(1)
            new_number = input("Enter your new Phone Number: +91 ")

            # Checking that the user did not entered the old number
            if(self.phone_no == new_number):
                print("Sorry We can't change the phone number! The number that you entered is the older one.")
            else:
                self.phone_no = new_number
                print("Changing Phone Number......")
                time.sleep(1.5)
                print(f"Phone Number Changed! New Phone Number +91 {self.phone_no}")
        else:
            time.sleep(1)
            print("We will not change your phone number.")
            print(f"Your Current Phone Number is +91{self.phone_no}")

    def transaction(self):
        print("""
        ____Transaction____

        *******************
        1. Account Details
        2. View Balance
        3. Deposit Cash
        4. Withdraw Cash
        5. Change Phone Number
        6. Exit
        *******************        
        """)

        while True:
            try:
                option = int(input("\nEnter 1, 2, 3, 4, 5 or 6 : "))
            except:
                print("!!!!Error!!!! \nEnter 1, 2, 3, 4, 5 or 6 only!\n")
                continue
            else:
                if option == 1:
                    atm.accountDetails()
                elif option == 2:
                    atm.checkBalance()
                elif option == 3:
                    atm.depositMoney()
                elif option == 4:
                    atm.withdrawMoney()
                elif option == 5:
                    atm.changePhoneNumber()
                elif option == 6:
                    print("Generating Receipt......")
                    time.sleep(4)
                    print("Receipt Generated.")
                    choice = input("Do you want to Print Receipt? (y/n)")

                    if (choice == "y"):
                        print("Printing Receipt......")
                        time.sleep(2)

                        print(f"""
******************************************
Transaction Completed.                         
Transaction number     : {random.randint(10000, 1000000)} 
Username               : {self.name}
Account Number         : {self.account_no}
Phone Number           : +91{self.phone_no}
Account Balance        : ₹{self.balance}           
******************************************
                        """)

                        print("""
 -------------------------------------
| Thanks for choosing us as your bank |
| Visit us again!                     |
 -------------------------------------
                        """)
                    else:
                        print("""
-------------------------------------
| Thanks for choosing us as your bank |
| Visit us again!                     |
-------------------------------------
                        """)
                    
                    sys.exit()


print(" ________________________________________________")
print("|------------------------------------------------|")
print("|----------Welcome to the Bank of INDIA----------|")
print("|------------------------------------------------|")
print("|________________________________________________|")

print("\n\n____Account Creation____\n")

name = input("Enter your name: ")
account_no = input("Enter your Account Number: ")
phone_no = int(input("Enter your Phone Number: +91 "))

print("\n____This is your first deposit____")
balance = int(input("Enter amount you want to deposit: ₹"))

atm = ATM(name,account_no,phone_no, balance)
print("****Congratulations Account Created Successfully****")
atm.accountDetails()
print("\n\n\n")

atm.transaction()
