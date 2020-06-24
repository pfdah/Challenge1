import random

money = 100
num = random.randint(1,10)
#Write your game of chance functions here
def head_tails(guess,amount):
    res = bool(random.randint(0,1))
    if res:
        print('Heads')
        return amount
    return -amount


def roll_dice(guess,amount):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  if (dice1 + dice2) % 2 == 0 and oddeven = "Even":
    return amount 
  elif (dice1 + dice2) % 2 != 0 and oddeven = "Odd":
    return amount
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
    return amount
  elif ycard == ocard:
    return 0
  return -amount


'''def roulette(guess,amount):
  rouletter = random.randint(0,36)
  if rouletter == 0 and int(guess)  ! = 0:
    return -amount
  if rouletter == 

'''
def betcheck(amount):
    if amount > money:
        return False
    return True

#Call your game of chance functions here
print('Welcome to Game Of Chance')
while(True):
    print('What do you want to play?')
    print('[1]. Coin Flip\n[2]. Cho-Han("Two dice sum")\n[3].Card Pick\n[4].Roulette\n[5]Quit\n>')
    choice = int(input(':\n>'))
    if choice == 1:
        print('You have',str(money)' points')
        print('Place your bet')
        bet = input(str(money))
          if betcheck:
              money += head_tails(bet)
         else:
             print('You bad boy')
             continue
    elif choice == 2:
        print('You have',str(money)' points')
        print('Place your bet')
        bet = input(str(money))
          if betcheck:
              guess = input('Guess Wether the result of Rolls will be (Odd) or (Even)').title()
              money += roll_dice(guess,bet)
         else:
             print('You bad boy')
             continue
    elif choice == 3:
        print('You have',str(money)' points')
        print('Place your bet')
        bet = input(str(money))
          if betcheck:
              money += roll_dice(bet)
         else:
             print('You bad boy')
             continue
    elif choice == 5:
        print('Bye Human')
        exit()
    else:
        print('Enter a valid choice dumbass')
        





















  

