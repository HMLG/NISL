from config import THE_ANTENNA_NUM,antenna_list

import cmath
import math
import numpy as np

#the const number
DEG2RAD = np.pi/180
RAD2DEG = 180/np.pi

#the frequence
FRE=924.375*pow(10,6)
C=3*(10**8)
Lamuda=C/FRE

#the basic axes,pixels
XGRIDSIZE=200
XX=XGRIDSIZE-1
YGRIDSIZE=200
PIXEL=np.zeros((XGRIDSIZE,YGRIDSIZE))
XGRID2TRUE=1.60/XGRIDSIZE
YGRID2TRUE=1.60/YGRIDSIZE

# the antennae array coordiantion
#COUNT = THE_ANTENNA_NUM
X = [1.60,1.60,1.60,1.60]
Y = np.linspace(0.8,1.12,THE_ANTENNA_NUM).tolist()#y is a metric [the_antenna,1]  to optional to a list
#np.zeros((THE_ANTENNA_NUM,1)).tolist()

#the new signal   S=Am'.*exp(1i*ph');


#the basic signal ,is the signal as the model ,theorically
#we use the real data to match them and we can get the most match
def basic_signal_construct(am,ph):
    s = []
    for i in range(THE_ANTENNA_NUM):
        s.append(am[i] * cmath.exp(ph[i]*1j))
    return s

#use the algorithem to calculate the array
def familiar_match(s):
    pm = []
    for i in range(1,XGRIDSIZE+1):
        for n in range(1,YGRIDSIZE+1):
            for k in range(1,THE_ANTENNA_NUM+1):
                par0 = s[k-1]
                par1 = float(X[k-1])
                par2 = float(Y[k-1])
                c = 1j*2*math.pi*2*math.sqrt((i*XGRID2TRUE-par1)**2+(n*YGRID2TRUE-par2)**2)/Lamuda
                pm.append(par0*cmath.exp(c))
            PIXEL[i-1][n-1] = abs(sum(pm))
            pm.clear()
    print(np.where(PIXEL==np.max(PIXEL)))
    return  PIXEL


