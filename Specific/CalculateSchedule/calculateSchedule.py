def CalculateSchedule(tasks, startTime, prohibitedWindows):
    taskDict = {}

    for task in tasks:
        found = False
        i = len(task) - 1
        while not found and i >= 0:
            if task[i] == "(":
                openBracketIndex = i
                found = True
            i -= 1
        
        duration = int(task[openBracketIndex + 1:-1])
        name = task[:openBracketIndex - 1]
        taskDict[name] = duration

    prohibitedDict = {}

    for window in prohibitedWindows.keys():
        prohibitedDict[window] = [int(prohibitedWindows[window][0].total_seconds() // 60), int(prohibitedWindows[window][1].total_seconds() // 60)]

    total = 0
    for task in taskDict.values():
        total += task

    for window in prohibitedDict.values():
        total += window[1] - window[0]

    schedule = [None] * total

    offset = int(startTime.total_seconds() // 60)

    for window in prohibitedDict.keys():
        for i in range(prohibitedDict[window][0] - offset, prohibitedDict[window][1] - offset):
            schedule[i] = window
    
    i = 0
    for task in taskDict.keys():
        for duration in range(taskDict[task]):
            while schedule[i] != None:
                i += 1
            schedule[i] = task
    
    return schedule

if __name__ == "__main__":
    pass # Testing done from main code
        