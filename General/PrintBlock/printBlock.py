import colorama

def PrintBlock(blockLength):
    repeatedString = "█" * blockLength
    print(colorama.Fore.WHITE + colorama.Style.DIM + repeatedString + colorama.Style.RESET_ALL)

if __name__ == '__main__':
    PrintBlock()