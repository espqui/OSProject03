from ctypes import *
import os 
root_path = os.path.dirname(os.path.realpath(__file__))

libFinger = CDLL(root_path + "/../library/libfinger.so")
 
#call C function to check connection
libFinger.connect() 
 
libFinger.set_device()

libFinger.move(1,5)
 
libFinger.pick()

libFinger.drop()
