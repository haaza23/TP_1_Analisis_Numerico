import numpy as npy

NP =  npy.float32(100849)
P = npy.float32(NP/700)

def calculoA( p, i,n ):
    a = (p/i)*(((1+i)^n)-1)
    return a


def algo1(p, i, n, xK):
    A = calculoA(p, i, n)
    xKMasUno = xK - ((p/xK)*( ((1+xK)**n) -1 ) -A)
    return xKMasUno

def algo2(p, i, n, xK):
    A = calculoA(p, i, n)
    xKMasUno =  ((A*(xK/p)+1)**(1/n)) -1
    return xKMasUno

def algo3(p, i, n, xK):
    A = calculoA(p, i, n)
    xKMasUno = (p/A)*(((1+xK)**n)-1)
    return xKMasUno

def algo4(p, i, n, xK):
    A = calculoA(p, i, n)
    xKMasUno =  (( (A*(xK/p)+1)/ ((1+xK)**(n/2) ) )**(2/n)) -1
    return xKMasUno

def algo5(p, i, n, xK):
    A = calculoA(p, i, n)
    xKMasUno = xK - ((p/xK)*( ((1+xK)**n) -1 ) -A)
    return xKMasUno