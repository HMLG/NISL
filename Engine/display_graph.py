#multiprocess
import time
from pylab import *
import threading #ahang ???why i use it?
from multiprocessing import Process
import os
#the data process
import matplotlib
import matplotlib.pyplot as plt
#import pylab as plt
import numpy as np
#the function
import data_entry as d_e

import data_pre_trim as d_p_e
import core_algorithm as ca
import preventFromStrangeValue as pfsv

print('All packages have been loaded')
#the axes set
plt.ion()
xside = np.linspace(0,2,200)
yside = np.linspace(0,2,200)
X,Y = np.meshgrid(xside,yside)
#the antenna coordination
antX = [3,7,11,15]
antY = [2,2,2,2]# y axes do not set [0,0,0,0]
# Sample data

def display(Z,pos,i):
    """
    actually we can't display the graph ,the engine is the backend.
    we just prepare the source picture for the UI.
    """
    plt.clf()

    plt.title('Indoor Location System')
    plt.xlabel("X  0.8cm/pixel")
    plt.ylabel("Y  0.8cm/pixel")
    def f(z): 
        """
        This function just set the Z to the Z axes,
        which will be used to make the heat map
        """
        return z

    x_n = 200
    y_n = 200
    x = np.linspace(0,200,x_n)
    y = np.linspace(0,200,y_n)
    X,Y = np.meshgrid(x,y)
    contourf(X, Y, f(Z), 8, alpha=.75, cmap='jet')
    crb = plt.colorbar(shrink=.55)
    crb.set_ticklabels(["5%","20%","30%","40%","50%","60%","70%","95%","99%"])
    # C = contour(X, Y, f(Z), 8, colors='black', linewidth=0.01)
    plt.scatter(antX, antY, color='cyan', marker='^')
    plt.scatter(pos[1],pos[0]-2,color='black',marker='*')
    plt.annotate('Target',xy=(pos[1],pos[0]-4),xytext=(pos[1]-20,pos[0]-22),arrowprops=dict(facecolor='black',headwidth=0.1,width=0.01, shrink=0.01))
    plt.annotate('Antenna Array',xy=(antX[0],antY[0]+2),xytext=(antX[0]+20,antY[0]+22),arrowprops=dict(facecolor='black',headwidth=0.1,width=0.01, shrink=0.01))
    plt.savefig('./pic/test'+str(i)+'.png')#save the pic as the source to the UI 

    #show()
    #plt.pause(1)
    

# Plot the density map using nearest-neighbor interpolation
def the_route_volk(count):
    """
    this founction is used to invole the data-pre-trim as the multithread
    the parameter:
    count the number for the pic the number is 10
    """
    
    ph = d_p_e.ph_process()
    am = d_p_e.am_process()
    s = ca.basic_signal_construct(am, ph)
    #print(s)
    the_show_data, position = ca.familiar_match(s)
    display(the_show_data,position,count)
    #time.sleep(0.2)
    return position

#class just for the data entry
class Threads(threading.Thread):
    def run(self):
        d_e.extra_PHASE_AND_RSSI()
        print('over')


def sys_entry(pos):
    """
    The func works as the system entry
    It is an api to
    """
    pos = pfsv.dataRestore(pos)
    d_e.extra_PHASE_AND_RSSI()
    position = []
    position = (the_route_volk(1))
    plt.ioff()
    plt.close()
    return position,pos

if __name__ =='__main__':
    print(sys_entry([0,0,0,0]))
