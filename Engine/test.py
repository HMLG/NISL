# coding=utf-8
import matlab
import matlab.engine
import time
#the music.m called by python
path = r"E:/4-23/13/matlab/"
if __name__ == '__main__':
    print(time.asctime(time.localtime(time.time())))
    eng = matlab.engine.start_matlab('MATLAB_R2017b')
    #fun  = eng.Music()
    fun_opt = eng.DOA_Freespace(path)
    #fun_opt = eng.DOA_Freespace_Calibration()
    #print('the coordination is below :')
    #print(fun)
    #print(fun_opt)
    print(fun_opt)
    eng.quit()
    print(time.asctime(time.localtime(time.time())))