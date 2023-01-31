import colorama, sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

def ViewPresetLists(blockLength):
    lists = ConvertFileList("./Data/PresetLists/listNames.txt")

    print("Please select a preset list to view\n")

    for i in range(len(lists)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + lists[i])
    
    choice = int(input(colorama.Fore.CYAN + "Your choice => "))

    fileName = "./Data/PresetLists/Lists/" + lists[choice - 1] + ".txt"

    tasks = ConvertFileList(fileName)
    
    print()
    for task in tasks:
        print(colorama.Style.RESET_ALL + task)

    print()
    PrintBlock(blockLength)
    input()

if __name__ == "__main__":
    ViewPresetLists(30) # This is just for testing purposes