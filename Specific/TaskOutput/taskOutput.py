import colorama, datetime, sys

sys.path.insert(0, "./General/PrintBlock")
from printBlock import PrintBlock

def TaskOutput(schedule, completedTasks, startTime, blockLength):
    PrintBlock(blockLength)
    print()

    if len(completedTasks) == 0:
        print(colorama.Fore.GREEN + colorama.Style.DIM + "----" + colorama.Style.RESET_ALL)
    for task in completedTasks:
        print(colorama.Fore.GREEN + colorama.Style.DIM + task + colorama.Style.RESET_ALL)

    print()

    currentTime = datetime.datetime.now().time()
    currentTimeDelta = datetime.timedelta(hours = currentTime.hour, minutes = currentTime.minute)

    currentPointer = int(currentTimeDelta.total_seconds() // 60 - startTime.total_seconds() // 60)

    currentTask = schedule[currentPointer]

    duration = 0
    for task in range(0, len(schedule)):
        if schedule[task] == None:
            continue
        
        if task < len(schedule) - 1 and schedule[task] == schedule[task + 1]:
            duration += 1
            continue
        beginTime = str(datetime.timedelta(minutes = startTime.total_seconds() // 60 + task - duration))[:5]
        endTime = str(datetime.timedelta(minutes = startTime.total_seconds() // 60 + task))[:5]

        if schedule[task] == currentTask:
            print(colorama.Fore.YELLOW + schedule[task] + " " + colorama.Fore.WHITE + beginTime + " - " + endTime)

        elif task < currentPointer:
            print(colorama.Fore.RED + schedule[task] + " " + colorama.Fore.WHITE + beginTime + " - " + endTime)

        elif task > currentPointer:
            print(colorama.Fore.GREEN + schedule[task] + " " + colorama.Fore.WHITE + beginTime + " - " + endTime)

        duration = 0

    print()

    ""+colorama.Style.RESET_ALL

if __name__ == "__main__":
    pass # Tested from main code