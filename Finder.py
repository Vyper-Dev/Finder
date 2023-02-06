import os
global FileType
FileType = "###"

def Find(Target):
    global File
    global Files
    Files = os.listdir()
    print(Files)
    for i in range(len(Files)):
        if Target in Files[i]:
            File = Files[i]
            print(File)
            return File
def FindFile():
    global Files
    global FileList
    FileList = []
    Files = os.listdir()
    for i in range(len(Files)):
        if Files[i].find("###") != -1:
            if Files[i].find(FileType) != -1:
                FileList.append(Files[i])
    print(FileList)
    return FileList

JobNumber = str(input("Enter the job number(ex. '###'): "))
os.chdir("###")
if Find(JobNumber):
    os.startfile(f"###{File}")
    os.chdir(f"###{File}")
    FindFile()
    try:
        os.startfile(f"{FileList[-1]}")
    except:
        print("None found for this job.")
os.chdir(f"###")
if Find(JobNumber):
    os.startfile(f"###{File}")
    os.chdir(f"###{File}")
    FindFile()
    try:
        os.startfile(f"{FileList[-2]}")
    except:
        os.startfile(f"{FileList[-1]}")
os.chdir("###")
if Find(JobNumber):
    FindFile()
    for x in range(len(FileList)):
        if FileList[x].find(JobNumber) != -1:
            if FileList[x].find("###") == -1:
                if FileList[x].find("###") == -1:
                    os.startfile(f"{FileList[x]}")
os.chdir("###")
if Find(JobNumber):
    FileType = "###"
    FindFile()
    for x in range(len(FileList)):
        if FileList[x].find(JobNumber) != -1:
            if FileList[x].find("###") == -1:
                if FileList[x].find("###") == -1:
                    os.startfile(f"{FileList[x]}")