import random

money = 100
num = random.randint(1,10)
#Write your game of chance functions here
def head_tails(guess,amount):
    res = bool(random.randint(0,1))
    if res:
        print('The conin flipped Heads')
        if guess == 'Heads':
            print('You won')
            return amount
    print('The coin flipped Tails')
    if guess == 'Tails':
        print('You won')
        return amount 
    print('You lost')
    return -amount

def roll_dice(guess,amount):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if (dice1 + dice2) % 2 == 0 and guess == "Even":
        print('You won Dice Sum was Even')
        return amount 
    elif (dice1 + dice2) % 2 != 0 and guess == "Odd":
        print('You won Dice Sum was Odd')
        return amount
    print('You lost Dice Sum was wrong')
    return -amount


def highroll(amount):
    lst = []  
    ocard = random.randint(1,13)
    lst.append(ocard)
    ycard = random.randint(1,13)
    if ycard in lst:
        ycard = random.randint(1,13)
    if ycard in lst:
        ycard = random.randint(1,13)
    if ycard > ocard:
        print('Your card was higher\nYou won')
        return amount
    elif ycard == ocard:
        print('Your card was same\nTie')
        return 0
    print('Your card was lower\nYou lost')
    return -amount


def betcheck(amount):
    if amount > money:
        return False
    elif amount <= 0:
        print('Bet must be Greater than 0')
        return False
    print('Point is less than the point you Bet.')
    return True

#Call your game of chance functions here
print('Welcome to Game Of Chance')
while(True):
    print('What do you want to play?')
    print('[1]. Coin Flip\n[2]. Cho-Han("Two dice sum")\n[3].Card Pick\n[4]Quit\n>')
    choice = int(input(':\n>'))
    if choice == 1:
        print('You have',str(money),' points')
        print('Place your bet')
        bet = int(input())
        if betcheck(money) :
            Guess = input('Enter your guess (\'Heads\') or (\'Tails\')').title
            money += head_tails(Guess,bet)
        else:
            print('You bad boy')
            continue
    elif choice == 2:
        print('You have',str(money),' points')
        print('Place your bet')
        bet = int(input())
        if betcheck(money):
            guess = input('Guess Wether the result of Rolls will be (Odd) or (Even)').title()
            money += roll_dice(guess,bet)
        else:
            print('You bad boy')
            continue
    elif choice == 3:
        print('You have',str(money),' points')
        print('Place your bet')
        bet = int(input())
        if betcheck(money):
            guess = input('Enter guess \'Even\' or \'Odd\'').title()
            money += highroll(bet)
        else:
            print('You bad boy')
            continue
    elif choice == 4:
        print('Bye Human')
        exit()
    else:
        print('Enter a valid choice dumbass')
        continue
        






















  

