def ConvertListFile(filePath, taskList):
    with open(filePath, "w") as fileObj:
        for line in taskList:
            fileObj.write(line + "\n")