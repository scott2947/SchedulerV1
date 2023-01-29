import colorama

def DeleteTask(taskList):
    for i in range(len(taskList)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + taskList[i])

    print()

    choice = int(input(colorama.Fore.CYAN + "Please select the task you want to delete => "))

    taskList.pop(choice - 1)

    ""+colorama.Style.RESET_ALL

    return taskList