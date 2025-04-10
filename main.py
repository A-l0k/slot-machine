import random

MAX_LINES =3
MAX_BET =100
MIN_BET=1

ROWS = 3
COLS = 3


symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, Lines, bet,values):
    winnings = 0
    winning_lines = []
    for line in range(Lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]* bet
            winning_lines.append(line + 1)

    return winnings,winning_lines




def getSlotMachineSpin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end='')
        print()


def deposit():
    while True:    
        amount = input('Enter the amount you want to deposit:$')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")

    return amount

def get_number_of_lines():
     while True:    
        lines = input(f'Enter the number of lines you want to bet on 1 to {MAX_LINES} ? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter valid no. of lines")
     return lines     

def get_bet():
     while True:    
        amount = input('Enter the amount you want to bet on:$')
        if amount.isdigit():
            amount = int(amount)
            if  MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between {MIN_BET} and {MAX_BET}")
     return amount
      

def main():
    balance =deposit()
    lines = get_number_of_lines()
    while True:

        bet = get_bet()
        total_bet = bet * lines
        if total_bet >  balance:
            print(f"you do enough balance for the bet, your current balance is {balance}")
        else:
            break
    print(f"you are betting $ {bet} on {lines} lines. total bet is equal to:${total_bet}")
    slots = getSlotMachineSpin(ROWS,COLS,symbol_count)
    printSlotMachine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"you won{winnings}")
    print(f"you won on lines:",*winning_lines)


main()    
