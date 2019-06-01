from ctypes import *
libCalc = CDLL("../library/libfinger.so")
 
#call C function to check connection
libCalc.connect() 
 
#calling randNum() C function
#it returns random number
varRand = libCalc.randNum()
print("Random Number:", varRand)
 
#calling addNum() C function
#it returns addition of two numbers
varAdd = libCalc.addNum(33,30)
print ("Addition : ", varAdd)
