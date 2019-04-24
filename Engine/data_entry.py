from config import THE_TIME_INTERVAL,antenna_list,THE_ANTENNA_NUM
import time
import preventFromStrangeValue as pfsv
#the data entry is the input of the data ,and the data from the reader
#we need RSSI and PHASE ,in the txt is the first and the second colume
#the antenna can be entend so we used the list to control the number of the metric


#the function is used to process the data and extra the data from the data source,
# use the regular expression to seperate the PHASE and the RSSI
#this edition use one data sourece(txt) to extra eight data stream
#the data interval is 0.288 sec

                 
def extra_PHASE_AND_RSSI():
    
    for antnum in range(THE_ANTENNA_NUM):
     ant_num = antnum
     #dir = r'E:/3-29/1/Antenna'+str(antnum+1)+'.txt'
     dir = r'E:\4-23\1\seq\Antenna'+str(antnum+1)+'.txt'
     #dir = r'F:\experience\13\Antennatest'+str(antnum+1)+'.txt'
     with open(dir,'r')as file:
         for count in file:
            temp = (count.split('\t'))
            antenna_list[ant_num][0].append(float(temp[0]))
            antenna_list[ant_num][1].append(float(1))


if __name__=='__main__':
    extra_PHASE_AND_RSSI()
    #for i in range(THE_ANTENNA_NUM):
    # print(antenna_list[i])
