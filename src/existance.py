import os
def exists(fullfilename):
    file_exists = os.path.isfile(fullfilename)
    file_exists2 = str(file_exists)
    file_existance2 = file_exists2.upper()
    return file_existance2

def direxists(dirpath):
    location1 = os.path.exists(dirpath)
    location2 = str(location1)
    location3 = location2.upper()
    return location3

def lenghtinfile(filename):
    with open(filename, "r") as file:
        info = file.read().rstrip("\n")
        info2 = str(info)
        info3 = len(info2)
        info4 = int(info3)
        return info4

def readfile(filename):
    with open(filename, "r") as file:
        info = file.read().rstrip("\n")
        info2 = str(info)
        return info2