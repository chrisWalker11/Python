#!/usr/bin/python3
import random
pool = ["rock", "paper", "scissors"]
tie = "it's a tie"
lost = "You lost"
won = "You won"
outcomes = [[tie, lost, won],
            [won, tie, lost],
            [lost , won, tie]]
win = 0
comp_win = 0
while True:
    #win = 0
    #comp_win = 0
    ui = None
    try:
        ui = input("pick 1 for rock, 2 for paper, or 3 for scissors\n>")
        uc = int(ui)
    except ValueError:
        print("Error you put ", ui, "Enter 1-3 only")
        continue
    try:
        print("You chose", pool[uc - 1])
    except IndexError:
        print("enter only 1, 2, or 3")
        continue

    comp = random.randint(1, 3)
    print("Computer chose", pool[comp -1])

    outcome = outcomes[uc -1][comp -1]
    print(outcome)

    if outcome == won:
        win += 1
    elif outcome == lost:
        comp_win += 1
    print(f"you have {win} wins\nthe computer has {comp_win} wins")
    if win >= 2 or comp_win >= 2:
        break
print("Goodbye!")


