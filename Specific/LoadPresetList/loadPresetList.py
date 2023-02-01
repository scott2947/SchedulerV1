import colorama, sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

def LoadPresetList():
    taskLists = ConvertFileList("./Data/PresetLists/listNames.txt")

    print(colorama.Fore.WHITE + "Please select a preset list to load\n")

    for i in range(len(taskLists)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + taskLists[i])

    choice = int(input(colorama.Fore.CYAN + "Your choice => "))

    ""+colorama.Style.RESET_ALL

    fileName = "./Data/PresetLists/Lists/" + taskLists[choice - 1] + ".txt"

    ""+colorama.Style.RESET_ALL

    tasks = ConvertFileList(fileName)

    return tasks