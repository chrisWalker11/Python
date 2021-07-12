#!/usr/bi1n/python3
import random
pool = ["rock", "paper", "scissors"]
while True:
    win = 0
    #if win == 'yes'
        #break
    #if win > 0
        #break
    user = input("pick rock, paper, or scissors\n>").lower()
    comp = random.choice(pool)
    if user == comp:
        print(f"you picked {user}\ncomputer picked {comp}\ntie")
    elif user == 'rock' and comp == 'paper':
        print(f"you picked {user}\ncomputer picked {comp}\nyou lose")
    elif user == 'rock' and comp == 'scissors':
        print(f"you picked {user}\ncomputer picked {comp}\nyou win")
        #idk how to break out loop
        #win =='yes'
        win += 1
    elif user == 'paper' and comp == 'rock':
        print(f"you picked {user}\ncomputer picked {comp}\nyou win")
        #win == 'yes'
        win += 1
    elif user == 'paper' and comp == 'scissors':
        print(f"you picked {user}\ncomputer picked {comp}\nyou loose")
    elif user == 'scissors' and comp == 'rock':
        print(f"you picked {user}\ncomputer picked {comp}\nyou loose")
    elif user == 'scissors' and comp == 'paper':
        print(f"you picked {user}\ncomputer picked {comp}\nyou win")
    if win > 0:
        break
