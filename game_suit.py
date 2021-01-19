# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 05:47:13 2021

@author: ASUS
"""

import random

game_list = ['Batu', 'Kertas', 'Gunting']
computer = c = 0
command = p = 0
print("Nilai: Computer = " + str(c) + " User = " + str(p))
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Batu, Kertas, Gunting atau Keluar: ")
    if command == computer_choice:
        print("Seri")
    elif command == 'Batu':
        if computer_choice == 'Gunting':
            print("User menang!")
            p = p+1
        else:
            print("Computer menang!")
            c = c+1
    elif command == 'Kertas':
        if computer_choice == 'Batu':
            print("User menang!")
            p = p+1
        else:
            print("Computer menang!")
            c = c+1
    elif command == 'Gunting':
        if computer_choice == 'Kertas':
            print("User menang!")
            p = p+1
        else:
            print("Computer menang!")
            c = c+1
    elif command == 'Keluar':
        break
    else:
        print("Wrong command! ")
    print("User: " + command)
    print("Computer: " + computer_choice)
    print("Nilai: Computer = " + str(c) + " User = " + str(p))
    print("")