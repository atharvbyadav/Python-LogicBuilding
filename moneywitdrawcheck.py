#Check for sufficient balance in Account

balance = 1000
withdraw = float(input("Enter amount to withdraw: "))

if withdraw > balance:
    print("Insufficient balance")
else:
    print("Withdrawal successful")
    