import data_entry as d_e
from data_entry import antenna_list
import numpy as np
from config import THE_ANTENNA_NUM,THE_EXTRA_RATE
#the ph will be calculate the aver as the ph array 1*8
#the RSSI will be set as 1(default)

 # the new ph
# the new am ,in the future it may be replace by the rssi

# the block get
def ph_process():
    """
    this func can extract the phase
    """
    ph = []
    for i in range(THE_ANTENNA_NUM):
        block = antenna_list[i][0][0:THE_EXTRA_RATE]
        temp = np.array(block,dtype='float')
        antenna_list[i][0] = antenna_list[i][0][THE_EXTRA_RATE:-1]
        ph.append(complex(temp.mean()))
    #print('ph over')
    return ph

#this func will be alternitive in the future
#in this func the am will be set the default 1
def am_process():
    am = []
    for i in range(THE_ANTENNA_NUM):
        am.append((1))
    #print('am over')
    return am
