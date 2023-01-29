import colorama, sys

sys.path.insert(0, "./General/PresetListInteractor")
from presetListInteractor import PresetListInteractor

def AddPresetList(blockLength):
    fileName = input(colorama.Fore.CYAN + "Please enter the name of the list => ")
    print()

    file = open("./Data/PresetLists/Lists/" + fileName + ".txt", "w")
    file.close()

    with open("./Data/PresetLists/listNames.txt", "a") as fileObj:
        fileObj.write(fileName + "\n")

    ""+colorama.Style.RESET_ALL

    PresetListInteractor("./Data/PresetLists/Lists/" + fileName + ".txt", blockLength)

if __name__ == "__main__":
    AddPresetList(30) # This is just for testing purposes