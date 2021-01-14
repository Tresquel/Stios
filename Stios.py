# Version 0.2.2
try:
    import os
    from random import randint
    import simplejson as json
    import requests
except:
    os.system('pip install simplejson && pip install requests')
    os.system('Stios.py && exit')


def Clear(): return os.system("cls")


version = "0.2.2"


def Info():
    Clear()
    if updateAvailable == True:
        print('Update available ' + versioncheck + "\n")
    else:
        print('You are running Stios version ' + version + "\n\n")
    print("Stios is in an early state\nIf you encounter bugs or random crashes make an issue about them in Stios's github page (https://github.com/Tresquel/Stios)")
    input("\nPress Enter to continue")
    Menu()


def Menu():
    if lastMenu == 1:
        Settings()
    while True:
        if settings['username'] == "":
            username = "world"
        else:
            username = settings['username']
        Clear()
        if updateAvailable == True:
            print("Version " + versioncheck + " is available.\n")
        print('Hello, ' + username + "!\n")
        print('1. Settings')
        print('2. Guess game')
        if updateAvailable == True:
            print('3. Update')
        print('0. Exit')

        choiceMenu = input('> ')
        if choiceMenu.isdigit() and int(choiceMenu) in {1, 2, 3, 0}:
            choiceMenu = int(choiceMenu)
            break

    if choiceMenu == 1:
        Settings()
    if choiceMenu == 2:
        GuessGame()
    if updateAvailable == True:
        if choiceMenu == 3:
            os.system('start https://github.com/Tresquel/Stios/releases')
    if choiceMenu == 0:
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
        if settings["enablecustomtheme"] == 1:
            print('3. ' + settings["customthemename"])
            print('4. Edit custom theme')
        if settings["enablecustomtheme"] == 0:
            print('3. Custom theme setup')
        print('0. Go back to settings')

        choiceTheme = input('> ')
        if choiceTheme.isdigit() and int(choiceTheme) in {1, 2, 3, 4, 0}:
            choiceTheme = int(choiceTheme)
            break

    if choiceTheme == 1:
        os.system('color 07')
        settings['theme'] = "default"
    if choiceTheme == 2:
        os.system('color 70')
        settings['theme'] = 'light'
    if settings["enablecustomtheme"] == 1:
        if choiceTheme == 4:
            CustomThemeSetup()
        if choiceTheme == 3:
            os.system('color ' + settings["customthemecolor"])
            settings['theme'] = 'custom'
    if settings["enablecustomtheme"] == 0:
        if choiceTheme == 3:
            CustomThemeSetup()
    if choiceTheme == 0:
        Settings()
    with open('files//Stios.json', 'w') as f:
        f.write(json.dumps(settings, indent=4 * ' '))


def CustomThemeSetup():
    while True:
        lastMenu = 1
        Clear()
        print('Welcome to the custom theme setup!\n')
        newTheme = input('Enter the name of the theme\n> ')
        settings["customthemename"] = newTheme
        Clear()
        print('0 = Black       8 = Gray\n1 = Blue        9 = Light blue\n2 = Green       A = Light green\n3 = Aqua        B = Light aqua')
        print('4 = Red         C = Light red\n5 = Purple      D = Light Purple\n6 = Yellow      E = Light yellow\n7 = White       F = Bright white\n')
        print('The first value is the color of the background and the second value is responsible for text color')
        print('For example: 01 will create Blue text on a Black background and 30 will create Black text on Aqua background')
        newThemeColor = input('Enter the color of the theme\n> ')
        settings["customthemecolor"] = newThemeColor
        settings["enablecustomtheme"] = 1
        break
    with open('files//Stios.json', 'w') as f:
        f.write(json.dumps(settings, indent=4 * ' '))
    os.system('color ' + settings["customthemecolor"])
    Settings()


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
        print("What's gonna be your new username?")
        newusername = input('> ')
        if (newusername == ""):
            ChangeUsername1()
        else:
            settings['username'] = newusername
            break
    with open('files//Stios.json', 'w') as f:
        f.write(json.dumps(settings, indent=4 * ' '))


def GuessGame():
    Clear()
    GuessCount = 0
    GuessAnswer = randint(0, 32767)
    HS = settings["gghs"]
    print("Welcome to the Guessing Game!")
    if HS != 0:
        print("Your highscore is: " + str(HS))
    while True:
        Guess = input("Try and guess my number!\n> ")
        if Guess.isdigit():
            if int(Guess) << GuessAnswer:
                print("Higher!")
                GuessCount + 1
            if int(Guess) >> GuessAnswer:
                print("Lower!")
                GuessCount + 1
            if int(Guess) == GuessAnswer:
                Won = True
                print("You guessed right!")
                print("It took you " + str(GuessCount) + " guesses!")
                settings["gghs"] = GuessCount
                break
        if Won == True:
            break
    with open('files//Stios.json', 'w') as f:
        f.write(json.dumps(settings, indent=4 * ' '))
    Menu()


def LoadStuff():
    settings['version'] = version
    if settings['theme'] == "default":
        os.system('color 07')
    if settings['theme'] == "light":
        os.system('color 70')
    if settings['theme'] == "custom":
        os.system('color ' + settings["customthemecolor"])
    with open('files//Stios.json', 'w') as f:
        f.write(json.dumps(settings, indent=4 * ' '))
    Info()


versionget = requests.get('https://pastebin.com/raw/u7Gd0wMn')
versioncheck = versionget.text
updateAvailable = False
if versioncheck != version:
    if "debug" in version:
        updateAvailable = True
    else:
        updateAvailable = False
settings = json.load(open("files//Stios.json", 'r'))
lastMenu = 0

LoadStuff()
while True:
    LoadStuff()
