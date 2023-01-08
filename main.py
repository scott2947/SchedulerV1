import colorama, random

def WelcomeMessage():
    print(colorama.Fore.WHITE + colorama.Style.DIM + "Created in 2023 by " + colorama.Fore.GREEN + "Callum Scott")
    print(colorama.Fore.WHITE + "For the benefit of all who show a desire to learn" + "\n")

    inspirationQuotes = []
    with open("./WelcomeMessage/quotes.txt") as fileObj:
        fileDump = fileObj.readlines()
        fileDump = [line.replace("\n", "") for line in fileDump]
        for line in fileDump:
            inspirationQuotes.append(line)
    inspirationQuote = random.choice(inspirationQuotes)
    
    print(colorama.Fore.YELLOW + colorama.Style.NORMAL + inspirationQuote + "\n")

    print(colorama.Fore.CYAN + "Welcome to Python Project Scheduler" + "\n")

    repeatedString = "█" * len(inspirationQuote)

    print(colorama.Fore.WHITE + colorama.Style.DIM + repeatedString + colorama.Style.RESET_ALL + "\n")

def RootMenu():
    options = ["Return to previous state", "Manage preset lists", "Use Scheduler", "Exit"]

    print(colorama.Fore.RED + "Select an option from the root menu below:" + "\n")

    for i in range(len(options)):
        print(colorama.Fore.GREEN + str(i + 1) + " " + colorama.Fore.CYAN + options[i])

    print()

    choice = int(input(colorama.Fore.RED + "Enter your choice >> " + colorama.Style.RESET_ALL))

    if choice == 1:
        ReturnToPreviousState()

    elif choice == 2:
        ManagePresetLists()

    elif choice == 3:
        UseScheduler()

    elif choice == 4:
        Exit()

def ReturnToPreviousState():
    pass

def ManagePresetLists():
    pass

def ViewPresetLists():
    pass

def AddPresetList():
    pass

def EditPresetList():
    pass

def AddTasks():
    pass

def EditTasks():
    pass

def ReorderTasks():
    pass

def DeleteTasks():
    pass

def ReorderPresetLists():
    pass

def DeletePresetList():
    pass

def RerunScheduler():
    pass

def UseScheduler():
    pass

def InputTasks():
    pass

def PreloadTasks():
    pass

def SelectPresetList():
    pass

def SelectPresetTasks():
    pass

def InputStartTime():
    pass

def InputProhibitedWindows():
    pass

def CalculateTaskList():
    pass

def OutputTaskList():
    pass

def MarkCompletedTask():
    pass

def Exit():
    pass