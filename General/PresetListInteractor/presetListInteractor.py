import colorama, sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

sys.path.insert(0, "./General/ConvertListFile")
from convertListFile import ConvertListFile

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

sys.path.insert(0, "./General/AddTask")
from addTask import AddTask

sys.path.insert(0, "./General/EditTask")
from editTask import EditTask

sys.path.insert(0, "./General/ReorderTasks")
from reorderTasks import ReorderTasks

sys.path.insert(0, "./General/DeleteTask")
from deleteTask import DeleteTask

def PresetListInteractor(filePath, blockLength):
    carryOn = True
    while carryOn:
        PrintBlock(blockLength)
        print()

        tasks = ConvertFileList(filePath)
        for line in tasks:
            print(colorama.Fore.WHITE + line)
        
        print("\n" + colorama.Fore.CYAN + "Please select an option\n")

        print(colorama.Fore.CYAN + "1) " + colorama.Fore.WHITE + "Add task")

        print(colorama.Fore.CYAN + "2) " + colorama.Fore.WHITE + "Edit task")

        print(colorama.Fore.CYAN + "3) " + colorama.Fore.WHITE + "Reorder tasks")

        print(colorama.Fore.CYAN + "4) " + colorama.Fore.WHITE + "Delete task")

        print(colorama.Fore.CYAN + "5) " + colorama.Fore.WHITE + "Exit to manage preset tasks")

        choice = int(input(colorama.Fore.CYAN + "Your choice => "))

        ""+colorama.Style.RESET_ALL

        if choice == 1:
            print()
            tasks = AddTask(tasks)
            print()

        elif choice == 2:
            print()
            tasks = EditTask(tasks)
            print()

        elif choice == 3:
            print()
            tasks = ReorderTasks(tasks)
            print()

        elif choice == 4:
            print()
            tasks = DeleteTask(tasks)
            print()

        elif choice == 5:
            carryOn = False

        ConvertListFile(filePath, tasks)

    print()
    PrintBlock(blockLength)
    print()

if __name__ == "__main__":
    PresetListInteractor("./Data/PresetLists/Lists/TestList.txt", 30) # This is just for testing purposes