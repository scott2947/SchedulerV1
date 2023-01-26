import colorama, random

def WelcomeMessage():
    print(colorama.Fore.WHITE + colorama.Style.DIM + "Created in 2023 by " + colorama.Fore.GREEN + "Callum Scott")
    print(colorama.Fore.WHITE + "For the benefit of all who show a desire to learn" + "\n")

    inspirationQuotes = []
    with open("./WelcomeMessage/quotes.txt") as fileObj:
        fileDump = fileObj.readlines()
        fileDump = [line.replace("\n", "") for line in fileDump]
        for line in fileDump:
            inspirationQuotes.append(line)
    inspirationQuote = random.choice(inspirationQuotes)
    
    print(colorama.Fore.YELLOW + colorama.Style.NORMAL + inspirationQuote + "\n")

    print(colorama.Fore.WHITE + "Welcome to Python Project Scheduler" + "\n")

    repeatedString = "█" * len(inspirationQuote)

    print(colorama.Fore.WHITE + colorama.Style.DIM + repeatedString + colorama.Style.RESET_ALL + "\n")

def RootMenu():
    print("Please select an option\n")

    print(colorama.Fore.GREEN + "1) " + colorama.Fore.WHITE + "Return to previous state")

    print(colorama.Fore.GREEN + "2) " + colorama.Fore.WHITE + "Manage preset lists")

    print(colorama.Fore.GREEN + "3) " + colorama.Fore.WHITE + "Use Scheduler")

    print(colorama.Fore.GREEN + "4) " + colorama.Fore.GREEN + "Exit Code")

    choice = int(input(colorama.Fore.GREEN + colorama.Style.DIM + "Your choice => "))

    print() # Break bar

RootMenu()
