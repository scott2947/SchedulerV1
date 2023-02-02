import colorama

def AddTask(taskList):
    task = input(colorama.Fore.CYAN + "Please enter the task => ")
    duration = input(colorama.Fore.CYAN + "Please enter the duration of the task (in minutes) => ")

    taskList.append(task + " ({0})".format(duration))

    "" + colorama.Style.RESET_ALL

    return taskList

if __name__ == '__main__':
    AddTask(["T1"]) # This is just for testing purposes