#!/usr/bin/python3
import random
pool = ["rock", "paper", "scissors"]
while True:
    win = 0
    #if win == 'yes'
        #break
    #if win > 0
        #break
    user = int(input("pick 1 for rock, 2 for paper, or 3 for scissors\n>"))
    if user == 1:
        c = 'rock'
    if user == 2:
        c = 'paper'
    if user == 3:
        c = 'scissors'

    comp = random.choice(pool)
    if c == comp:
        print(f"you picked {c}\ncomputer picked {comp}\ntie")
    elif c == 'rock' and comp == 'paper':
        print(f"you picked {c}\ncomputer picked {comp}\nyou lose")
    elif c == 'rock' and comp == 'scissors':
        print(f"you picked {c}\ncomputer picked {comp}\nyou win")
        #idk how to break out loop
        #win =='yes'
        win += 1
    elif c == 'paper' and comp == 'rock':
        print(f"you picked {c}\ncomputer picked {comp}\nyou win")
        #win == 'yes'
        win += 1
    elif c == 'paper' and comp == 'scissors':
        print(f"you picked {c}\ncomputer picked {comp}\nyou loose")
    elif c == 'scissors' and comp == 'rock':
        print(f"you picked {c}\ncomputer picked {comp}\nyou loose")
    elif c == 'scissors' and comp == 'paper':
        print(f"you picked {c}\ncomputer picked {comp}\nyou win")
        win += 1
    if win > 0:
        break
