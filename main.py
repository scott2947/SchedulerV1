import colorama, random

def WelcomeMessage():
    print(colorama.Fore.WHITE + colorama.Style.DIM + "Created in 2023 by " + colorama.Fore.CYAN + "Callum Scott")
    print(colorama.Fore.WHITE + "For the benefit of all who show a desire to learn" + "\n")

    inspirationQuotes = []
    with open("./WelcomeMessage/quotes.txt") as fileObj:
        fileDump = fileObj.readlines()
        fileDump = [line.replace("\n", "") for line in fileDump]
        for line in fileDump:
            inspirationQuotes.append(line)
    inspirationQuote = random.choice(inspirationQuotes)
    
    print(colorama.Fore.YELLOW + colorama.Style.NORMAL + inspirationQuote + "\n")

    print(colorama.Fore.WHITE + "Welcome to Python Project Scheduler" + "\n")

    repeatedString = "█" * len(inspirationQuote)

    print(colorama.Fore.WHITE + colorama.Style.DIM + repeatedString + colorama.Style.RESET_ALL)

    input()

    return len(inspirationQuote)

def RootMenu(blockLength):
    carryOn = True

    while carryOn:
        print("Please select an option\n")

        print(colorama.Fore.CYAN + "1) " + colorama.Fore.WHITE + "Return to previous state")

        print(colorama.Fore.CYAN + "2) " + colorama.Fore.WHITE + "Manage preset lists")

        print(colorama.Fore.CYAN + "3) " + colorama.Fore.WHITE + "Use Scheduler")

        print(colorama.Fore.CYAN + "4) " + colorama.Fore.WHITE + "Exit Code")

        choice = int(input(colorama.Fore.CYAN + "Your choice => "))

        repeatedString = "█" * blockLength

        print("\n" + colorama.Fore.WHITE + colorama.Style.DIM + repeatedString + colorama.Style.RESET_ALL + "\n")

        if choice == 1:
            pass

        elif choice == 2:
            ManagePresetLists(blockLength)

        elif choice == 3:
            pass

        elif choice == 4:
            carryOn = False

def ReturnToPreviousState(blockLength):
    pass # Will be written when necessary infrastructure is implemented

def ManagePresetLists(blockLength):
    carryOn = True

    while carryOn:
        print("Please select an option\n")

        print(colorama.Fore.CYAN + "1) " + colorama.Fore.WHITE + "View all preset lists")

        print(colorama.Fore.CYAN + "2) " + colorama.Fore.WHITE + "Add preset lists")

        print(colorama.Fore.CYAN + "3) " + colorama.Fore.WHITE + "Edit preset lists")

        print(colorama.Fore.CYAN + "4) " + colorama.Fore.WHITE + "Reorder preset lists")

        print(colorama.Fore.CYAN + "5) " + colorama.Fore.WHITE + "Delete preset list")

        print(colorama.Fore.CYAN + "6) " + colorama.Fore.WHITE + "Exit to root menu")

        choice = int(input(colorama.Fore.CYAN + "Your choice => "))

        repeatedString = "█" * blockLength

        print("\n" + colorama.Fore.WHITE + colorama.Style.DIM + repeatedString + colorama.Style.RESET_ALL + "\n")

        if choice == 1:
            ViewPresetLists(blockLength)

        elif choice == 2:
            AddPresetList(blockLength)

        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            carryOn = False

def ViewPresetLists(blockLength):
    lists = []
    with open("./PresetLists/lists.txt") as fileObj:
        fileDump = fileObj.readlines()
        fileDump = [line.replace("\n", "") for line in fileDump]
        for line in fileDump:
            lists.append(line)

    print("Please select an option\n")

    for i in range(len(lists)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + lists[i])
    
    choice = int(input(colorama.Fore.CYAN + "Your choice => "))

    fileName = "./PresetLists/Lists/" + lists[choice - 1] + ".txt"

    tasks = []
    with open(fileName) as fileObj:
        fileDump = fileObj.readlines()
        fileDump = [line.replace("\n", "") for line in fileDump]
        for line in fileDump:
            tasks.append(line)
    
    print()
    for task in tasks:
        print(colorama.Style.RESET_ALL + task)
    print()

    repeatedString = "█" * blockLength

    print(colorama.Fore.WHITE + colorama.Style.DIM + repeatedString + colorama.Style.RESET_ALL + "\n")

def AddPresetList(blockLength):
    fileName = input(colorama.Fore.CYAN + "Please enter the name of the list => ")
    print()

    file = open("./PresetLists/Lists/" + fileName + ".txt", "w")
    file.close()

    with open("./PresetLists/lists.txt", "a") as fileObj:
        fileObj.write(fileName + "\n")
    
    carryOn = True
    while carryOn:
        repeatedString = "█" * blockLength
        print(colorama.Fore.WHITE + colorama.Style.DIM + repeatedString + colorama.Style.RESET_ALL + "\n")

        with open("./PresetLists/Lists/" + fileName + ".txt") as fileObj:
            fileDump = fileObj.readlines()
            fileDump = [line.replace("\n", "") for line in fileDump]
            for line in fileDump:
                print(colorama.Fore.WHITE + line)
        
        print("\n" + colorama.Fore.CYAN + "Please select an option\n")

        print(colorama.Fore.CYAN + "1) " + colorama.Fore.WHITE + "Add task")

        print(colorama.Fore.CYAN + "2) " + colorama.Fore.WHITE + "Edit task")

        print(colorama.Fore.CYAN + "3) " + colorama.Fore.WHITE + "Reorder tasks")

        print(colorama.Fore.CYAN + "4) " + colorama.Fore.WHITE + "Delete task")

        print(colorama.Fore.CYAN + "5) " + colorama.Fore.WHITE + "Exit to manage preset tasks")

        choice = int(input(colorama.Fore.CYAN + "Your choice => "))

        "" + colorama.Style.RESET_ALL

        if choice == 1:
            print()
            fileDump = AddTask(fileDump)
            print()

        elif choice == 2:
            print()
            fileDump = EditTask(fileDump)
            print()

        elif choice == 3:
            print()
            fileDump = ReorderTasks(fileDump)
            print()

        elif choice == 4:
            print()
            fileDump = DeleteTask(fileDump)
            print()

        elif choice == 5:
            carryOn = False

        with open("./PresetLists/Lists/" + fileName + ".txt", "w") as fileObj:
            for line in fileDump:
                fileObj.write(line + "\n")

    repeatedString = "█" * blockLength

    print("\n" + colorama.Fore.WHITE + colorama.Style.DIM + repeatedString + colorama.Style.RESET_ALL + "\n")

def AddTask(taskList):
    task = input(colorama.Fore.CYAN + "Please enter the task => ")
    duration = input(colorama.Fore.CYAN + "Please enter the duration of the task (in minutes) => ")
    "" + colorama.Style.RESET_ALL
    taskList.append(task + " ({0})".format(duration))
    return taskList

def EditTask(taskList):
    for i in range(len(taskList)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + taskList[i])

    print()

    choice = int(input(colorama.Fore.CYAN + "Please select the task you want to edit => "))

    print()
    
    task = input(colorama.Fore.CYAN + "Please enter the edited task => ")
    duration = input(colorama.Fore.CYAN + "Please enter the duration of the edited task (in minutes) => ")
    "" + colorama.Style.RESET_ALL

    taskList[choice - 1] = task + " ({0})".format(duration)

    return taskList

def ReorderTasks(taskList):
    for i in range(len(taskList)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + taskList[i])
    
    print()

    choice = input(colorama.Fore.CYAN + "Please provide a string with the tasks in the desired order => ")

    returnList = []

    for i in choice:
        returnList.append(taskList[int(i) - 1])

    return returnList

def DeleteTask(taskList):
    for i in range(len(taskList)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + taskList[i])

    print()

    choice = int(input(colorama.Fore.CYAN + "Please select the task you want to delete => "))

    taskList.pop(choice - 1)

    return taskList

blockLength = WelcomeMessage()
RootMenu(blockLength)
