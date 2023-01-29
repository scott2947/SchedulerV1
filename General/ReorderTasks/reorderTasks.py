import colorama

def ReorderTasks(taskList):
    for i in range(len(taskList)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + taskList[i])

    choice = input(colorama.Fore.CYAN + "Please provide a comma-separated string with the entries in the desired order => ")

    returnList = []

    for i in choice.split(","):
        returnList.append(taskList[int(i) - 1])

    ""+colorama.Style.RESET_ALL

    return returnList