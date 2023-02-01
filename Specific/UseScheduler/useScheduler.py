import sys, colorama, datetime

sys.path.insert(0, "./Specific/InputTasks")
from inputTasks import InputTasks

sys.path.insert(0, "./Specific/InputProhibitedWindows")
from inputProhibitedWindows import InputProhibitedWindows

sys.path.insert(0, "./Specific/CalculateSchedule")
from calculateSchedule import CalculateSchedule

sys.path.insert(0, "./Specific/TaskOutput")
from taskOutput import TaskOutput

def UseScheduler(blockLength):
    print("Welcome to the Scheduler Program\n")

    tasks = InputTasks(blockLength)

    print()
    prohibitedWindows = InputProhibitedWindows(blockLength)

    input()

    currentTime = datetime.datetime.now().time()
    currentTimeDelta = datetime.timedelta(hours = currentTime.hour, minutes = currentTime.minute)

    completedTasks = []
    carryOn = True
    while carryOn:
        if len(tasks) == 0:
            print(colorama.Fore.GREEN + "All tasks completed")
            carryOn = False
            continue

        schedule = CalculateSchedule(tasks, currentTimeDelta, prohibitedWindows)

        TaskOutput(schedule, completedTasks, currentTimeDelta, blockLength)

        choice = int(input(colorama.Fore.CYAN+ "1 to update, 2 to complete a task, 3 to exit => "))

        if choice == 1:
            continue

        elif choice == 2:
            for task in tasks:
                found = False
                i = len(task) - 1
                while not found and i >= 0:
                    if task[i] == "(":
                        openBracketIndex = i
                        found = True
                    i -= 1
                
                name = task[:openBracketIndex - 1]
                if name == schedule[0]:
                    completedTasks.append(schedule[0])
                    tasks.remove(task)
                    break

            currentTime = datetime.datetime.now().time()
            currentTimeDelta = datetime.timedelta(hours = currentTime.hour, minutes = currentTime.minute)
            continue

        elif choice == 3:
            carryOn = False
    
    ""+colorama.Style.RESET_ALL

if __name__ == "__main__":
    UseScheduler(30) # This is just for testing purposes