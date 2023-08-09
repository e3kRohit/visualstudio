import random

MAX_LINES=3
MIN_BET=1
MAX_BET=100

ROWS=3
COLS=3

symbol_count= {
    "A": 8,
    "B": 1,
    "C": 1,
    "D": 1
}

symbol_value= {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for p in range(lines):
        symbol= columns[0][p]
        for q in columns:
            symbol_to_check = q[p]
            if symbol != symbol_to_check:
                break
        else:
            winnings = values[symbol]*bet
            winning_lines.append(p+1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for i, j in symbols.items():
        for k in range(j):
            all_symbols.append(i)
  
    columns=[]
    for column in range (cols) :
        column=[]
        for row in range(rows):
            current_symbols = all_symbols[:]
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return(columns)

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")


def deposit():
    while True:
         amount = input("What would you like to deposit $")
         if amount.isdigit():
               amount=int(amount)
               if amount > 0:
                   break
               else: 
                   print("amount must be greater than zero")
         else:
            print("please enter a number")
    
    return amount

def get_number_of_lines():
    while True:
         lines = input("how many lines would you like to bet on (1-  "+str(MAX_LINES)+")? ")
         if lines.isdigit():
               lines=int(lines)
               if 1 <= lines <= MAX_LINES:
                   break
               else: 
                   print("Enter the valid number of lines")
         else:
            print("please enter a number")
    
    return lines

def get_bet():
    while True:
         amount = input("What amount would you like to bet on $")
         if amount.isdigit():
               amount=int(amount)
               if MIN_BET< amount < 100:
                   break
               else: 
                   print("amount must be in range 0-100")
         else:
            print("please enter a number")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet= bet*lines
        if total_bet > balance:
            print(f"you do not have enough to bet on, your current balance is ${balance}")
        else:
            break
    print(f"you are betting ${total_bet} on {lines} lines")

    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_value)
    print(f"You have won $", winnings)
    print("You have won on lines ", *winning_lines)
    return winnings - total_bet



def main():
    balance = deposit()
    while True:
         print(f" your current balance is ${balance}")
         result = input("Press enter to play (press q to quit)")
         if result == "q":
             break
         else:
            balance += spin(balance)
    print(f"you are left with ${balance} ")
    
main()
