import colorama, sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

sys.path.insert(0, "./General/ConvertListFile")
from convertListFile import ConvertListFile

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

def InputTasks(blockLength):
    file = open("./Data/ActiveList/activeList.txt", "w")
    file.close()

    carryOn = True
    while carryOn:
        PrintBlock(blockLength)
        print()

        tasks = ConvertFileList("./Data/ActiveList/activeList.txt")
        for line in tasks:
            print(colorama.Fore.WHITE + line)

        print("\n" + colorama.Fore.WHITE + "Please select an option\n")

        print(colorama.Fore.CYAN + "1) " + colorama.Fore.WHITE + "Preload tasks")

        print(colorama.Fore.CYAN + "2) " + colorama.Fore.WHITE + "Select list of preset tasks")

        print(colorama.Fore.CYAN + "3) " + colorama.Fore.WHITE + "Select tasks from a preset list")

        print(colorama.Fore.CYAN + "4) " + colorama.Fore.WHITE + "Input new tasks")

        print(colorama.Fore.CYAN + "5) " + colorama.Fore.WHITE + "Reorder tasks")

        print(colorama.Fore.CYAN + "6) " + colorama.Fore.WHITE + "Delete task")

        print(colorama.Fore.CYAN + "7) " + colorama.Fore.WHITE + "Exit to next stage")

        choice = int(input(colorama.Fore.CYAN + "Your choice => "))

        ""+colorama.Style.RESET_ALL

        if choice == 1:
            pass

        elif choice == 2:
            pass

        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            pass

        elif choice == 7:
            carryOn = False

        ConvertListFile("./Data/ActiveList/activeList.txt", tasks)

    ConvertListFile("./Data/PreloadList/preloadList.txt", tasks)

    print()
    PrintBlock(blockLength)
    print()

if __name__ == "__main__":
    InputTasks(30) # This is just for testing purposes