import subprocess
import os
import shutil
import time
def activeReader():
    """
    THIS FUNC IS USED TO ACTIVITE THE READER AS THE DATA SOURCE
    """
    path = r'E:/WORK/CODE/NISL/ReadTags_wx1/ReadTags4BF/bin/Debug/'
    cmd = r'920.625.exe'
    EXIT = subprocess.Popen(path+cmd)
    #print(EXIT)
    return EXIT

def stroeData(EXIT):
    """
    THIS FUNC MV THE READER DATA TO THE NEW DIRECTOY 
    AND IF THE PATH EXISTS, WILL STOP THE READER 
    """
    dir = 'E:/'
    TIME =time.localtime(time.time())
    filename = str(TIME.tm_year)+'-'+str(TIME.tm_mon)+'-'+str(TIME.tm_mday)+'-'+str(TIME.tm_hour)+'-'+str(TIME.tm_min)
    print(filename)
    if os.path.exists(dir+filename):
        print("The file has been exits!")
        EXIT.terminate()
    else:
        os.mkdir(dir+filename)
        shutil.move(dir+'Fre920.625.txt',dir+filename)

if __name__=="__main__":
    stroeData(None)
