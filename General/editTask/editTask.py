import colorama

def EditTask(taskList):
    for i in range(len(taskList)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + taskList[i])

    choice = int(input(colorama.Fore.CYAN + "Please select the task you want to edit => "))

    print()
    
    task = input(colorama.Fore.CYAN + "Please enter the edited task => ")
    duration = input(colorama.Fore.CYAN + "Please enter the duration of the edited task (in minutes) => ")
    ""+colorama.Style.RESET_ALL

    taskList[choice - 1] = task + " ({0})".format(duration)

    return taskList