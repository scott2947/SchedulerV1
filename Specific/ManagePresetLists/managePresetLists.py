import colorama, sys

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

sys.path.insert(0, "./Specific/ViewPresetLists")
from viewPresetLists import ViewPresetLists

sys.path.insert(0, "./Specific/AddPresetList")
from addPresetList import AddPresetList

sys.path.insert(0, "./Specific/EditPresetList")
from editPresetList import EditPresetList

sys.path.insert(0, "./Specific/ReorderPresetLists")
from reorderPresetLists import ReorderPresetLists

sys.path.insert(0, "./Specific/DeletePresetList")
from deletePresetList import DeletePresetList

def ManagePresetLists(blockLength):
    carryOn = True

    while carryOn:
        print("Please select an option\n")

        print(colorama.Fore.CYAN + "1) " + colorama.Fore.WHITE + "View all preset lists")

        print(colorama.Fore.CYAN + "2) " + colorama.Fore.WHITE + "Add preset lists")

        print(colorama.Fore.CYAN + "3) " + colorama.Fore.WHITE + "Edit preset lists")

        print(colorama.Fore.CYAN + "4) " + colorama.Fore.WHITE + "Reorder preset lists")

        print(colorama.Fore.CYAN + "5) " + colorama.Fore.WHITE + "Delete preset list")

        print(colorama.Fore.CYAN + "6) " + colorama.Fore.WHITE + "Exit to root menu")

        choice = int(input(colorama.Fore.CYAN + "Your choice => "))

        ""+colorama.Style.RESET_ALL

        print()
        PrintBlock(blockLength)
        print()

        if choice == 1:
            ViewPresetLists(blockLength)

        elif choice == 2:
            AddPresetList(blockLength)

        elif choice == 3:
            EditPresetList(blockLength)

        elif choice == 4:
            ReorderPresetLists(blockLength)

        elif choice == 5:
            DeletePresetList(blockLength)

        elif choice == 6:
            carryOn = False

if __name__ == "__main__":
    ManagePresetLists(30) # This is just for testing purposes