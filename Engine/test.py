# coding=utf-8
import matlab
import matlab.engine
import time
#the music.m called by python
path = r"E:/matlab/"
if __name__ == '__main__':
    
    eng = matlab.engine.start_matlab('MATLAB_R2017b')
    #fun  = eng.Music()
    a = time.asctime(time.localtime())
    fun_opt = eng.DOA_Freespace(path)
    b = time.asctime(time.localtime())
    #fun_opt = eng.DOA_Freespace_Calibration()
    #print('the coordination is below :')
    #print(fun)
    #print(fun_opt)
    print(fun_opt)
    eng.quit()
    print(b-a)