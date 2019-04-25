#-*- coding:utf-8 -*-
from config import THE_ANTENNA_NUM,antenna_list,THE_RESTORE_NUM
import os
def dataRestore(position):
    """
    this func will be used to eliminate the strange value in the ph 
    in the select sentences.
    use the last value in the list and the abs of the (last value - current value )
    is the boundy of the strange value.
    it's tough.
    And the file will be restore at the seq(means sequence )
    every 50 lines as a slot.
    postion is the last tell return value
    """
    path = r'E:/4-23/13/'
    cwd = path.split('/')#get the current work directory
    mkdir = '/'.join([cwd[0],cwd[1],cwd[2],'seq'])
    mkdir_matlab = '/'.join([cwd[0],cwd[1],cwd[2],'matlab'])
    cleandata = []
    #print(mkdir) # It is used to check the mkdir path 
    if os.path.exists(mkdir):
        pass # if the dir is exists
    else:
        os.mkdir(mkdir)
        os.mkdir(mkdir_matlab)
    #print(cwd,mkdir) #this is used to test the path
    for antnum in range(THE_ANTENNA_NUM):
        txt_name=['Fre920.625','Antenna2','Antenna3','Antenna4']
        txt_restore=['Antenna1','Antenna2','Antenna3','Antenna4']
        dir = path+txt_name[antnum]+'.txt'
        # print(dir) # this is used to test the file
        count = 0 # every 50 lines as a block
        with open(mkdir+'/'+txt_restore[antnum]+'.txt','w') as file_in:
            with open(mkdir_matlab+'/'+txt_restore[antnum]+'.txt','w') as file_matlab:
                with open(dir,'r')as file_out: # this is the data sources
                    file_out.seek(position[antnum],0)
                    # for line in file_out:
                    while count < THE_RESTORE_NUM:
                        line = file_out.readline()
                        sample = line.split('\t')
                        cleandata.append(float(sample[0]))
                        # file_in.writelines(sample[0]+'\n')
                        # file_matlab.writelines(sample[0]+'\t'+sample[1]+'\n')
                        count = count + 1
                    else :
                        position[antnum]= file_out.tell()

                    cleandata = sorted(cleandata)
                    if abs(cleandata[THE_RESTORE_NUM//2]-cleandata[-1]) < 1:
                        for i in range(THE_RESTORE_NUM):
                            file_in.writelines(str(cleandata[i])+'\n')
                            file_matlab.writelines(str(cleandata[i])+'\t'+'1'+'\n')

                    if abs(cleandata[THE_RESTORE_NUM//2]-cleandata[-1]) > 3:
                        for i in range(THE_RESTORE_NUM//2):
                            file_in.writelines(str(cleandata[i])+'\n')
                            file_matlab.writelines(str(cleandata[i])+'\t'+'1'+'\n')
                    else:
                        for i in range(THE_RESTORE_NUM//2,THE_RESTORE_NUM):
                            file_in.writelines(str(cleandata[i])+'\n')
                            file_matlab.writelines(str(cleandata[i])+'\t'+'1'+'\n')
    return position    



if __name__=="__main__":
    position = dataRestore([0,0,0,0])
    print(position)
    position = dataRestore(position)
    print(position)