import colorama, sys

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

sys.path.insert(0, "./Specific/ManagePresetLists")
from managePresetLists import ManagePresetLists

sys.path.insert(0, "./Specific/UseScheduler")
from useScheduler import UseScheduler

def RootMenu(blockLength):
    carryOn = True

    while carryOn:
        print("Please select an option\n")

        print(colorama.Fore.CYAN + "1) " + colorama.Fore.WHITE + "Manage preset lists")

        print(colorama.Fore.CYAN + "2) " + colorama.Fore.WHITE + "Use Scheduler")

        print(colorama.Fore.CYAN + "3) " + colorama.Fore.WHITE + "Exit Code")

        choice = int(input(colorama.Fore.CYAN + "Your choice => "))

        ""+colorama.Style.RESET_ALL

        print()
        PrintBlock(blockLength)
        print()

        if choice == 1:
            ManagePresetLists(blockLength)

        elif choice == 2:
            UseScheduler(blockLength)

        elif choice == 3:
            carryOn = False

if __name__ == "__main__":
    RootMenu(30) # This is just for testing purposes