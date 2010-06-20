from math import *

def gaussienne(x,mu,sigma):
        return (1/(sigma*sqrt(2*pi))) * exp( -0.5 * ( pow((x - mu) / (sigma),2 ) ))     
def gaussEqual(x, error): # equal error
        return gaussienne(x,0,0.166666667*error) 
def gaussLT(x, error): # less than error
        return gaussienne(x, -0.5*error,0.166666667*error)
def gaussMT(x, error): #more than error
        return gaussienne(x, 0.5*error,0.166666667*error)

