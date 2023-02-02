import colorama, sys, datetime

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

def InputProhibitedWindows(blockLength):
    prohibitedWindows = {}

    carryOn = True
    while carryOn:
        PrintBlock(blockLength)
        print()

        for item in prohibitedWindows.keys():
            print("{0}: {1} to {2}".format(item, prohibitedWindows[item][0], prohibitedWindows[item][1]))

        print("\nPlease choose an option\n")

        print(colorama.Fore.CYAN + "1) " + colorama.Fore.WHITE + "Enter a prohibited window")

        print(colorama.Fore.CYAN + "2) " + colorama.Fore.WHITE + "Exit to next stage")

        choice = int(input(colorama.Fore.CYAN + "Your choice => "))

        ""+colorama.Style.RESET_ALL

        if choice == 1:
            print()
            
            name = input(colorama.Fore.CYAN + "Enter a name for this prohibited window => ")

            startTime = input(colorama.Fore.CYAN + "Enter a start time (HH:MM) => ")

            startTime = datetime.timedelta(hours = int(startTime[:2]), minutes = int(startTime[3:]))

            endTime = input(colorama.Fore.CYAN + "Enter an end time (HH:MM) => ")

            endTime = datetime.timedelta(hours = int(endTime[:2]), minutes = int(endTime[3:]))

            print()

            prohibitedWindows[name] = [startTime, endTime]

        elif choice == 2:
            carryOn = False

        ""+colorama.Style.RESET_ALL

    return prohibitedWindows

if __name__ == '__main__':
    print(InputProhibitedWindows(30)) # This is just for testing purposes
