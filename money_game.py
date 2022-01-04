import math
import random

names = input("Enter your names: ")
names = names.split()
personA, personB = names
currency_arr = [2000,2000]
count_arr = [0,0]
n = random.randrange(0, 2)

yearly_earnings_arr = [0,0]

while currency_arr[0] < 10000 and currency_arr[1] < 10000:
    print("Choices: beg, start shop, or rob")
    k = n % 2
    print(f"{names[k]} your turn!")
    currency_arr[k] += yearly_earnings_arr[k]
    print(f"Your currency: {currency_arr[k]} dollars")
    choice = input("What would you like to do? ")
    if choice == "beg":
        currency_arr[k] += random.randrange(0, 200)
    elif choice == "start shop":
        print("cost: 500 dollars")
        if currency_arr[k] < 500:
            print("You don't have enough money")
        elif count_arr[k] == 0:
            currency_arr[k] -= 500
            yearly_earnings_arr[k] = random.randrange(200,400)
            count_arr[k] = 1
            print(f"Congradulations! You will earn {yearly_earnings_arr[k]} dollars every year from your shop!")
        else:
            print("You already have a shop")
            n -= 1
    elif choice == "rob":
        amount = int(input("How much? "))
        if amount > currency_arr[k]:
            print("amount too large, try again")
            n -= 1
        else:    
            l = []
            for _ in range(500):
                l.append(0)
            for _ in range(amount):
                l.append(1)
            random.shuffle(l)
            print(l)
            a = random.randrange(0,len(l))
            if l[a] == 1:
                print("You got caught")
                x = random.randrange(amount,amount+150)
                print(f"fine: {x} dollars")
                print(f"You gave {names[1-k]} {x} dollars")
                currency_arr[k] -= x
                currency_arr[1-k] += x
            else:
                print("That was successful!")
                currency_arr[k] += amount
            

    else:
        print("Wrong input. Please try again")
        n -= 1

    print(f"Your currency: {currency_arr[k]} dollars\n")
    n += 1

if currency_arr[0] >= 10000:
    print(f"{names[0]}, you win!")
else:
    print(f"{names[1]}, you win!")