#Version 2020.12.16

import os
import simplejson as json

Clear = lambda: os.system("cls")

version = "2020.12.14"

def Info():
    print("Stios is in very early state\nIf you encounter bugs or random crashes make an issue about them in Stios`s github page (https://github.com/Tresquel/Stios)")
    input("\nPress Enter to continue")
    Menu()

def Menu():
    if (lastMenu == 1):
        Settings()
    while True:
        if (settings['username'] == ""):
            username = "world"
        else:
            username = settings['username']
        Clear()
        print('Hello, ' + username + "!\n")
        print('1. Settings')
        print('0. Exit')
        
        choiceMenu = input('> ')
        if choiceMenu.isdigit() and int(choiceMenu) in {1, 0}:
            choiceMenu = int(choiceMenu)
            break
        else:
            print("Please enter a valid number.")
            input('press Enter to continue')
    
    
    if choiceMenu == 1:
        Settings()
    if choiceMenu == 2:
        quit()


def Settings():
    while True:
        lastMenu = 1
        Clear()
        print('Stios, settings\n')
        print('1. Theme')
        print('2. Change username')
        print('0. Back to menu')
        
        choiceSettings = input('> ')
        if choiceSettings.isdigit() and int(choiceSettings) in {1, 2, 0}:
            choiceSettings = int(choiceSettings)
            break
        else:
            print("Please enter a valid number.")
            input('press Enter to continue')
    
    
    if choiceSettings == 1:
        Theme()
    if choiceSettings == 2:
        ChangeUsername1()
    if choiceSettings == 0:
        Menu()

def Theme():
    while True:
        lastMenu = 1
        Clear()
        print('Stios, settings, theme select\n')
        print('1. Default (dark)')
        print('2. Default (light)')
        print('0. Go back to settings')

        choiceTheme = input('> ')
        if choiceTheme.isdigit() and int(choiceTheme) in {1, 2, 0}:
            choiceTheme = int(choiceTheme)
            break
        else:
            print("Please enter a valid number.")
            input('press Enter to continue')
        
    if choiceTheme == 1:
        os.system('color 07')
        settings['theme'] = "default"
    if choiceTheme == 2:
        os.system('color 70')
        settings['theme'] = 'light'
    if choiceTheme == 0:
        Settings()
    with open('files//Stios.json', 'w') as f:
        f.write(json.dumps(settings, indent=4 * ' '))

def ChangeUsername1():
    while True:
        lastMenu = 1
        Clear()
        print('Stios, Settings, Change username')
        if (settings['username'] == ""):
            print('You dont have a username.\n')
        else:
            print(settings['username'] + ' is your current username\n')
        print('1. Change username')
        print('0. Go back to settings')
        ChangeUsername1 = input('> ')
        if ChangeUsername1.isdigit() and int(ChangeUsername1) in {1, 2, 0}:
            ChangeUsername1 = int(ChangeUsername1)
            break
        else:
            print("Please enter a valid number.")
            input('press Enter to continue')
        
    if ChangeUsername1 == 1:
        ChangeUsername2()
    if ChangeUsername1 == 2:
        Settings()
    with open('files//Stios.json', 'w') as f:
        f.write(json.dumps(settings, indent=4 * ' '))
def ChangeUsername2():
    while True:
        lastMenu = 1
        Clear()
        print('What`s gonna be your new username?')
        newusername = input('> ')
        if (newusername == ""):
            ChangeUsername1()
        else:
            settings['username'] = newusername
            break
    with open('files//Stios.json', 'w') as f:
        f.write(json.dumps(settings, indent=4 * ' '))
def LoadStuff():
    settings['version'] = version
    if (settings['theme'] == "default"):
        os.system('color 07')
    if (settings['theme'] == "light"):
        os.system('color 70')
    with open('files//Stios.json', 'w') as f:
        f.write(json.dumps(settings, indent=4 * ' '))
    Info()  
settings = json.load(open("files//Stios.json", 'r'))
lastMenu = 0
LoadStuff()
while True:
    Menu()
