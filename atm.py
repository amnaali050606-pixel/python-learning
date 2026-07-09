def main():
    print("ATM")

def display_menu():
    print("1. Check Balance ")
    print("2. Deposit Money")
    print("3. Withdraw Money ")
    print ("4. Exit ")

def check_balance():
    print(f"corrent balance is: {current_balance}")

def deposit_money():
    try:
        money = int(input(" Enter amount to deposit "))
    except ValueError:

def 