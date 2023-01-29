import sys, os

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

sys.path.insert(0, "./General/ConvertListFile")
from convertListFile import ConvertListFile

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

sys.path.insert(0, "./General/DeleteTask")
from deleteTask import DeleteTask

def DeletePresetList(blockLength):
    presetLists = ConvertFileList("./Data/PresetLists/listNames.txt")

    presetLists = DeleteTask(presetLists)

    ConvertListFile("./Data/PresetLists/listNames.txt", presetLists)

    files = os.listdir("./Data/PresetLists/Lists/")
    files = [file.replace(".txt", "") for file in files]

    for file in files:
        if file not in presetLists:
            os.remove("./Data/PresetLists/Lists/" + file + ".txt")

    print()
    PrintBlock(blockLength)
    print()

if __name__ == "__main__":
    DeletePresetList(30) # This is just for testing purposes