import colorama

def AddTask(taskList):
    task = input(colorama.Fore.CYAN + "Please enter the task => ")
    duration = input(colorama.Fore.CYAN + "Please enter the duration of the task (in minutes) => ")
    "" + colorama.Style.RESET_ALL
    taskList.append(task + " ({0})".format(duration))
    return taskList

if __name__ == '__main__':
    AddTask()