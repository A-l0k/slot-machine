def deposit():
    while True:    
        amount = input('Enter the amount you want to bet on:$')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")

    return amount
deposit()