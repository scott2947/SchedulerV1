import sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

sys.path.insert(0, "./General/ConvertListFile")
from convertListFile import ConvertListFile

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

sys.path.insert(0, "./General/ReorderTasks")
from reorderTasks import ReorderTasks

def ReorderPresetLists(blockLength):
    presetLists = ConvertFileList("./Data/PresetLists/listNames.txt")
    presetLists = ReorderTasks(presetLists)
    ConvertListFile("./Data/PresetLists/listNames.txt", presetLists)

    print()
    PrintBlock(blockLength)
    print()

if __name__ == "__main__":
    ReorderPresetLists(30) # This is just for testing purposes