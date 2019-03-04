from config import THE_TIME_INTERVAL,antenna_list,THE_ANTENNA_NUM
import time

#the data entry is the input of the data ,and the data from the reader
#we need RSSI and PHASE ,in the txt is the first and the second colume
#the antenna can be entend so we used the list to control the number of the metric


#the function is used to process the data and extra the data from the data source,
# use the regular expression to seperate the PHASE and the RSSI
#this edition use one data sourece(txt) to extra eight data stream
#the data interval is 0.288 sec

#def extra_PHASE_AND_RSSI():
#    timestamp = 0
#    ant_num = 0
#    dir = r'F:experience\3.txt'
#    with open(dir,'r')as file:
#        for count in file:
#            temp = (count.split(','))
#            time_now = int(temp[2])
#            if timestamp == 0 :
#                timestamp = time_now + THE_TIME_INTERVAL
#            if time_now <= timestamp:
#                antenna_list[ant_num][0].append(float(temp[0]))
#                antenna_list[ant_num][1].append(float(temp[1]))
#            else :
#                timestamp += THE_TIME_INTERVAL
#                ant_num += 1
#                if ant_num > 7 :
#                    print(antenna_list)
#   
                 
def extra_PHASE_AND_RSSI():
    
    for antnum in range(THE_ANTENNA_NUM):
     ant_num = antnum
     dir = r'F:/experience/13/Antenna'+str(antnum+1)+'.txt'
     with open(dir,'r')as file:
         for count in file:
            temp = (count.split('\t'))
            antenna_list[ant_num][0].append(float(temp[0]))
            antenna_list[ant_num][1].append(float(temp[1]))


#this func used to trim the origin data ,extra the ph,am,timestamp and
# store to the prefix trim_ origin name
def the_data_extra():
    dir = r'E:/1/Antenna12.txt'
    dir_trim = r'E:/1/trim_Antenna12.txt'
    trim = open(dir_trim, 'w')
    # the range is the sources data
    with open(dir, 'r')as file:
        for count in file:
            temp = (count.split('\t'))
            if temp[4] == '6246':
                contents = temp[0] + ',' + temp[1] + ',' + temp[6]
                trim.writelines(contents)
    trim.close()

if __name__=='__main__':
    extra_PHASE_AND_RSSI()
    print(antenna_list)
    #for i in range(THE_ANTENNA_NUM):
    #    z = i
    #    print('the length of '+str(z)+'is : ',len(antenna_list[i][0]),len(antenna_list[i][1]))