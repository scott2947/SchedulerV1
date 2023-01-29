import colorama, random, sys

sys.path.insert(0, "./General/ConvertFileList")
from convertFileList import ConvertFileList

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

def WelcomeMessage():
    print(colorama.Fore.WHITE + colorama.Style.DIM + "Created in 2023 by " + colorama.Fore.CYAN + "Callum Scott")
    print(colorama.Fore.WHITE + "For the benefit of all who show a desire to learn" + "\n")

    inspirationQuotes = ConvertFileList("./Data/Quotes/quotes.txt")
    inspirationQuote = random.choice(inspirationQuotes)
    
    print(colorama.Fore.YELLOW + colorama.Style.NORMAL + inspirationQuote + "\n")

    print(colorama.Fore.WHITE + "Welcome to Python Project Scheduler" + "\n" + colorama.Style.RESET_ALL)

    PrintBlock(len(inspirationQuote))

    input()

    return len(inspirationQuote)

if __name__ == "__main__":
    WelcomeMessage()