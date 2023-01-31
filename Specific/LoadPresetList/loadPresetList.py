import colorama, sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

def LoadPresetLists():
    taskLists = ConvertFileList("./Data/PresetLists/presetLists.txt")

    print(colorama.Fore.WHITE + "Please select a preset list to load\n")

    for i in range(len(taskLists)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + taskLists[i])

    choice = int(input(colorama.Fore.CYAN + "Your choice => "))

    ""+colorama.Style.RESET_ALL

    fileName = "./Data/PresetLists/Lists/" + taskLists[choice - 1] + ".txt"

    tasks = ConvertFileList(fileName)

    return tasks