import colorama, sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

def LoadPresetTasks(currentTasks, blockLength):
    lists = ConvertFileList("./Data/PresetLists/listNames.txt")

    print("Please select a preset list to add tasks from\n")

    for i in range(len(lists)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + lists[i])
    
    choice = int(input(colorama.Fore.CYAN + "Your choice => "))

    fileName = "./Data/PresetLists/Lists/" + lists[choice - 1] + ".txt"

    tasks = ConvertFileList(fileName)

    print()
    PrintBlock(blockLength)
    print()

    print("Please enter the task numbers you would like to add (comma separated)\n")

    for i in range(len(tasks)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + tasks[i])

    choice = input(colorama.Fore.CYAN + "Your choice => ")

    choice = choice.split(",")

    taskList = [tasks[i - 1] for i in range(len(choice))]

    ""+colorama.Style.RESET_ALL

    return currentTasks + taskList

if __name__ == "__main__":
    LoadPresetTasks(30) # This is just for testing purposes