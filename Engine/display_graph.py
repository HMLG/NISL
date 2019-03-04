#multiprocess
import time
import threading
#the data process
import matplotlib.pyplot as plt
#import pylab as plt
import numpy as np
#the function
import data_entry as d_e

import data_pre_trim as d_p_e
import core_algorithm as ca
#the axes set
plt.ion()
xside = np.linspace(0,2,200)
yside = np.linspace(0,2,200)
X,Y = np.meshgrid(xside,yside)
#the antenna coordination
antX = [1,5,9,13]
antY = [200,200,200,200]
# Sample data

def display(Z):
    plt.clf()
    plt.imshow(Z)
    plt.colorbar(shrink=.55)
    plt.scatter(antX, antY, color='red')
    plt.pause(1)

# Plot the density map using nearest-neighbor interpolation
def the_route_volk():
    ph = d_p_e.ph_pricess()
    am = d_p_e.am_process()
    s = ca.basic_signal_construct(am, ph)
    print(s)
    the_show_data = ca.familiar_match(s)
    display(the_show_data)
    time.sleep(1)

#class just for the data entry
class Threads(threading.Thread):
    def run(self):
        d_e.extra_PHASE_AND_RSSI()
        print('over')

if __name__ =='__main__':
    data_entry = Threads()
    data_entry.start()
    ph = d_p_e.ph_pricess()
    am = d_p_e.am_process()
    ca.basic_signal_construct(am,ph)
    for i in range(5) :
        print('the routune')
        the_route_volk()
    plt.ioff()
