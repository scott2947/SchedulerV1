import colorama, sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

sys.path.insert(0, "./General/ConvertListFile")
from convertListFile import ConvertListFile

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

sys.path.insert(0, "./Specific/PreloadTasks")
from preloadTasks import PreloadTasks

sys.path.insert(0, "./Specific/LoadPresetList")
from loadPresetList import LoadPresetList

sys.path.insert(0, "./Specific/LoadPresetTasks")
from loadPresetTasks import LoadPresetTasks

sys.path.insert(0, "./General/AddTask")
from addTask import AddTask

sys.path.insert(0, "./General/EditTask")
from editTask import EditTask

sys.path.insert(0, "./General/ReorderTasks")
from reorderTasks import ReorderTasks

sys.path.insert(0, "./General/DeleteTask")
from deleteTask import DeleteTask

def InputTasks(blockLength):
    tasks = []

    carryOn = True
    while carryOn:
        PrintBlock(blockLength)
        print()

        for line in tasks:
            print(colorama.Fore.WHITE + line)

        print("\n" + colorama.Fore.WHITE + "Please select an option\n")

        print(colorama.Fore.CYAN + "1) " + colorama.Fore.WHITE + "Preload tasks")

        print(colorama.Fore.CYAN + "2) " + colorama.Fore.WHITE + "Select list of preset tasks")

        print(colorama.Fore.CYAN + "3) " + colorama.Fore.WHITE + "Select tasks from a preset list")

        print(colorama.Fore.CYAN + "4) " + colorama.Fore.WHITE + "Add task")

        print(colorama.Fore.CYAN + "5) " + colorama.Fore.WHITE + "Edit task")

        print(colorama.Fore.CYAN + "6) " + colorama.Fore.WHITE + "Reorder tasks")

        print(colorama.Fore.CYAN + "7) " + colorama.Fore.WHITE + "Delete task")

        print(colorama.Fore.CYAN + "8) " + colorama.Fore.WHITE + "Exit to next stage")

        choice = int(input(colorama.Fore.CYAN + "Your choice => "))

        ""+colorama.Style.RESET_ALL

        if choice == 1:
            tasks = PreloadTasks()
            print()

        elif choice == 2:
            print()
            tasks = LoadPresetList()
            print()

        elif choice == 3:
            print()
            tasks = LoadPresetTasks(tasks, blockLength)
            print()

        elif choice == 4:
            print()
            tasks = AddTask(tasks)
            print()

        elif choice == 5:
            print()
            tasks = EditTask(tasks)
            print()

        elif choice == 6:
            print()
            tasks = ReorderTasks(tasks)
            print()

        elif choice == 7:
            print()
            tasks = DeleteTask(tasks)
            print()

        elif choice == 8:
            carryOn = False

    ConvertListFile("./Data/PreloadList/preloadList.txt", tasks)

    return tasks

if __name__ == "__main__":
    InputTasks(30) # This is just for testing purposes