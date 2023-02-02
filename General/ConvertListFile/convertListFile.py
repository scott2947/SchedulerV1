def ConvertListFile(filePath, taskList):
    with open(filePath, "w") as fileObj:
        for line in taskList:
            fileObj.write(line + "\n")

if __name__ == '__main__':
    ConvertListFile() # Tested from main code