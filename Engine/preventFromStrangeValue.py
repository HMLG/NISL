#-*- coding:utf-8 -*-
from config import THE_ANTENNA_NUM,antenna_list

for antnum in range(THE_ANTENNA_NUM):
    """
    this func will be used to eliminate the strange value in the ph 
    in the select sentences.
    use the last value in the list and the abs of the (last value - current value )
    is the boundy of the strange value.
    it's tough.
    """
    ant_num = antnum
    dir = r'F:/experience/13/Antenna'+str(antnum+1)+'.txt'
    with open(dir,'r')as file:
        for count in file:
            temp = (count.split('\t'))
            if (len(antenna_list[ant_num][0])==0):
                antenna_list[ant_num][0].append(float(temp[0]))
            else:
                 err = antenna_list[ant_num][0][-1]
                 if abs(err-float(temp[0])) > 0.1*(err):
                     antenna_list[ant_num][0].append(float(err))
            
                 else:  
                     antenna_list[ant_num][0].append(float(temp[0]))
            
            antenna_list[ant_num][1].append(float(temp[1]))
print(antenna_list)