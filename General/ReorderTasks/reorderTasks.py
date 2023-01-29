import colorama

def ReorderTasks(taskList):
    for i in range(len(taskList)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + taskList[i])
    
    print()

    choice = input(colorama.Fore.CYAN + "Please provide a string with the tasks in the desired order => ")

    returnList = []

    for i in choice:
        returnList.append(taskList[int(i) - 1])

    ""+colorama.Style.RESET_ALL

    return returnList