#multiprocess
import time
from pylab import *
import threading
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
print('All packages have been loaded')
#the axes set
plt.ion()
xside = np.linspace(0,2,200)
yside = np.linspace(0,2,200)
X,Y = np.meshgrid(xside,yside)
#the antenna coordination
antX = [1,5,9,13]
antY = [200,200,200,200]
# Sample data

def display(Z,i):
    """
    actually we can't display the graph ,the engine is the backend.
    we just prepare the source picture for the UI.
    """
    plt.clf()

    # plt.imshow(Z)
    # plt.colorbar(shrink=.55)
    # plt.scatter(antX, antY, color='red')
    # plt.savefig('./pic/test'+str(i)+'.png')#save the pic as the source to the UI 
    
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
    display(the_show_data,count)
    #time.sleep(0.2)
    return position

#class just for the data entry
class Threads(threading.Thread):
    def run(self):
        d_e.extra_PHASE_AND_RSSI()
        print('over')


def sys_entry():
    """
    The func works as the system entry
    It is an api to
    """
    data_entry = Threads()
    data_entry.start()
    time.sleep(1)
    ph = d_p_e.ph_process()
    am = d_p_e.am_process()
    position = []
    ca.basic_signal_construct(am,ph)
    for i in range(10) :
        print('the routune : '+str(i))
        position.append(the_route_volk(i))
    plt.ioff()
    plt.close()
    return position

if __name__ =='__main__':
    # data_entry = Threads()
    # data_entry.start()
    # ph = d_p_e.ph_process()
    # am = d_p_e.am_process()
    # time.sleep(1)
    # ca.basic_signal_construct(am,ph)
    # for i in range(5) :
    #     print('the routune')
    #     the_route_volk(i)
    # plt.ioff()
    sys_entry()
