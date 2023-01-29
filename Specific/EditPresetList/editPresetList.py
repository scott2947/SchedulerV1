import colorama, sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

sys.path.insert(0, "./General/PresetListInteractor")
from presetListInteractor import PresetListInteractor

def EditPresetList(blockLength):
    lists = ConvertFileList("./Data/PresetLists/listNames.txt")

    print("Please select a preset list to edit\n")

    for i in range(len(lists)):
        print(colorama.Fore.CYAN + str(i + 1) + ") " + colorama.Fore.WHITE + lists[i])
    
    choice = int(input(colorama.Fore.CYAN + "Your choice => "))

    print()

    filePath = "./Data/PresetLists/Lists/" + lists[choice - 1] + ".txt"

    ""+colorama.Style.RESET_ALL

    PresetListInteractor(filePath, blockLength)

if __name__ == "__main__":
    EditPresetList(30) # This is just for testing purposes
