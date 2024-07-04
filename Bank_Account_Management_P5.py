def get_balance(account_number: str) -> float:
    with open('accounts.txt', 'r') as file:
        for line in file:
            acc_num, balance = line.strip().split(',') #Split account number and balance
            if acc_num == account_number:
                return float(balance)
    print("Invalid Account Number")
    return 0.0

def deposit(account_number: str, amount: float):
    found = False
    lines = []
    with open('accounts.txt', 'r') as file:
        for line in file:
            acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                balance = str(float(balance) + amount)
                found = True
            lines.append(f"{acc_num},{balance}\n")
    if not found:
        print("Invalid Account Number")
    else:
        with open('accounts.txt', 'w') as file:
            file.writelines(lines)

def withdraw(account_number: str, amount: float):
    found = False
    lines = []
    with open('accounts.txt', 'r') as file:
        for line in file:
            acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                if float(balance) >= amount:
                    balance = str(float(balance) - amount)
                    found = True
                else:
                    print("Insufficient balance for withdrawals")
                    found = True
            lines.append(f"{acc_num},{balance}\n")
    if not found:
        print("Invalid Account Number")
    else:
        with open('accounts.txt', 'w') as file:
            file.writelines(lines)

def update_account(account_number: str, balance: float):
    found = False
    lines = []
    with open('accounts.txt', 'r') as file:
        for line in file:
            acc_num, bal = line.strip().split(',')
            if acc_num == account_number:
                bal = str(balance)
                found = True
            lines.append(f"{acc_num},{bal}\n")
    if not found:
        print("Invalid Account Number")
    else:
        with open('accounts.txt', 'w') as file:
            file.writelines(lines)

# Optional
with open('accounts.txt', 'w') as f:
    f.write("12435,1000.0\n") # first shows the account number then account balance

print(get_balance("12435"))
deposit("12435", 200.0)
print(get_balance("12435"))
withdraw("12435", 10000.0)
print(get_balance("12435"))
update_account("12435", 800.0)
print(get_balance("12435"))
deposit("14436", 200.0)
