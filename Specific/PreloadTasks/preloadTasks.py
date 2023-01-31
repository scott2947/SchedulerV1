import sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

def PreloadTasks():
    return ConvertFileList("./Data/PreloadTasks/preloadTasks.txt")