# coding=utf-8
import matlab.engine
import time
#the music.m called by python

if __name__ == '__main__':
    eng = matlab.engine.start_matlab('MATLAB_R2017b')
    #fun  = eng.Music()
    #fun = eng.DOA_Freespace()
    #fun_opt = eng.DOA_Freespace_Calibration()
    #print('the coordination is below :')
    #print(fun)
    #print(fun_opt)
    print(time.asctime(time.localtime(time.time())))
    eng.quit()