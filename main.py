"""
- dial *
- get options
---
1- deposit money
2- airtime / bundles
3- withdraw cash
----
1.deposit
- ask the user to enter amount of money to deposit.
- add that money to their balance
2.airtime and bundles
- daily bundles
- weekly bundles
- monthly bundles
3.Withdraw money
- Enter the amount to withdraw
- Substract from current if current balance is not 
"""

dial=input("Dial number: ")

print(
    """ 
    1- deposit money
    2- airtime / bundles
    3- withdraw cash
    4- Check balance
    """)

account_balance = 0

option=int(input(">>> "))

if option == 1:
    deposit = int(input("Enter amount to deposit: "))

    account_balance+=deposit
    #  account_balance =account_balance + withdraw


elif option == 2:
    print("""
        - daily bundles
        - weekly bundles
        - monthly bundles
    """)

elif option ==3:
    withdraw=int(input("Enter amount you want to deposit: "))

    if withdraw >=account_balance:
        print("Insufficient funds.")

    account_balance -= withdraw

    # account_balance =account_balance - withdraw

elif option == 4:
    print(f"Account balance: {account_balance}")

else:
    print("Invalid option")







