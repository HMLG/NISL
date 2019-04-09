import os



def extract(dir):
    """
    This func is used to extract the message from the txt file.
    The MultiReadfer get the signal file.And according this function.The special columes will be select.
    The input is the one big file include many tags in it.
    The output is the tag number file.
    """
    #print(os.listdir(dir))
    txt = os.listdir(dir)
    path = dir+"\\"
    #print(path)
    #print(path+str(files[0]))
    tag =[]
    files ={}
    with open(path+str(txt[0]),'r') as source:
        for line in source:
            # print(line)
            segementation = line.split('\t')
            #print(segementation[:])
            #print('\n')
            if segementation[4]  not in tag:
                print(segementation[4])
                tag.append(segementation[4])
                files[str(segementation[4])]=open(path+str(segementation[4])+'.txt','w')

            rebuild = "".join(segementation[0])+'\n'
            files[segementation[4]].write(rebuild)
            rebuild = ""
        for key,value in files.items():
            print(key,value)
            value.close()

if __name__=="__main__":
    """
    revursive in the dir
    """
    dir = r'E:\4-9'
    dirs = os.listdir(dir)
    print(dir)
    path=[]
    for name in dirs:
        path.append(dir + '\\' + name)
    print(path)
    for i in path:
     extract(i)