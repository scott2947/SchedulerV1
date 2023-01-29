def ConvertFileList(filePath):
    with open(filePath) as fileObj:
        fileDump = fileObj.readlines()
        fileDump = [line.replace("\n", "") for line in fileDump]
        return fileDump
    
if __name__ == '__main__':
    ConvertFileList()