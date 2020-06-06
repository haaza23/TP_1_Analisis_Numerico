import numpy as np

A = 200000
B = 1000000

def algoritmo1(xk, P, n):
    xkMasUno = xk - P/xk * (((1 + xk)**n) - 1) - A
    return xkMasUno

def algoritmo2(xk, P, n):
    xkMasUno = (((A * (xk / P)) + 1) ** (1/n)) - 1
    return xkMasUno

def algoritmo3(xk, P, n):
    xkMasUno = (P/A)*(((1 + xk)**n) - 1)
    return xkMasUno

def algoritmo4(xk, P, n):
    xkMasUno = ((((A*(xk/P))+1)/((1+xk)**(n/2)))**(2/n))-1
    return xkMasUno

def algoritmo5(xk, P, n):
    xkMasUno = xk - (((P/xk)*(((1+xk)**n)-1))-A)/(((((-1)*P)/(xk**2))*(((1+xk)**n)-1))+((P/xk)*n*((1+xk)**(n-1))))
    return xkMasUno


def calcularDoblePres():
    NP = float(100849)
    P = float(NP / 700)
    n = 360
    k = float(0)
    xk = float(0.001)
    print(float(xk))
    xkSiguiente = algoritmo5(xk, P, n)
    error = abs((xkSiguiente - xk) / xkSiguiente)
    print('{:^10}{:^10}{:^10}{:^10}'.format('k', 'xk', 'xk+1', 'error'))
    while (error >= 1e-10):
        xkSiguiente = algoritmo5(xk,P, n)
        error = abs((xkSiguiente - xk) / xkSiguiente)
        print('{:^10} {:^10.14f} {:^10.14f} {:^10.14f}'.format(k, float(xk), float(xkSiguiente), float(error)))
        xk = xkSiguiente
        k += 1
    print("La raiz es: ", xk)
    print()

def calcularSimplePres():
    NP =  np.float32(100849)
    P = np.float32(NP / 700)
    n = 360
    k =  np.float32(0)
    xk = np.float32(0.001)
    print(float(xk))
    xkSiguiente = algoritmo5(xk, P, n)
    error = abs((xkSiguiente - xk) / xkSiguiente)
    print('{:^10}{:^10}{:^10}{:^10}'.format('k', 'xk', 'xk+1', 'error'))
    while (error >= 1e-5):
        xkSiguiente = algoritmo5(xk, P, n)
        error = abs((xkSiguiente - xk) / xkSiguiente)
        print('{:^10} {:^10.9f} {:^10.9f} {:^10.9f}'.format(k, float(xk), float(xkSiguiente), float(error)))
        xk = xkSiguiente
        k += 1
    print("La raiz es: ", xk)
    print()
def calcularA():
    i = float(0.0063738101905 )
    p = float(100849/700)
    n = 360
    a = (p/i)*(((1+i)**n)-1)
    print(a)

def calcularAMaxI(a, i):
    i = float(0.00637371)
    i = i + i*0.3
    p = float(100849/700)
    n = 360
    a = (p/i)*(((1+i)**n)-1)
    return a, i


def calcularAMinI(a, i):
    i = float(0.00637371)
    i = i - (i*0.3)
    p = float(100849/700)
    n = 360
    a = (p/i)*(((1+i)**n)-1)
    return a, i


def calcularAMaxP(a, p):
    i = float(0.00637371)
    p = float(100849/700)
    p = p + (p*0.1)
    n = 360
    a = (p/i)*(((1+i)**n)-1)
    return a, p


def calcularAMinP(a, p):
    i = float(0.00637371)
    p = float(100849/700)
    p = p - (p*0.1)
    n = 360
    a = (p/i)*(((1+i)**n)-1)
    return a, p

#calcularDoblePres();
print(0.00000039467101*0.00637381018990)

errorI= float(0.00637371)*0.3
errorP= float(100849/700)*0.1

iMAX=0
imin=0

pMAX=0
pmin=0


aiMAX=0
aimin=0

apMAX=0
apmin=0

apMAX, pMAX = calcularAMaxP(apMAX, pMAX)
apmin, pmin = calcularAMinP(apmin, pmin)

aiMAX, iMAX = calcularAMaxI(aiMAX, iMAX)
aimin, imin = calcularAMinI(aimin, imin)

print("I MAX I", iMAX)
print("I min I", imin)
deltaI = iMAX-imin
print("Delta I", deltaI)

print("A MAX I", aiMAX)
print("A min I", aimin)
deltaAi = aiMAX-aimin
print("Delta Ai", deltaAi)

deltaAI = deltaAi/deltaI
print("Delta A/Delta I: ", deltaAI)

print("P MAX P", pMAX)
print("P min P", pmin)
deltaP = pMAX-pmin
print("Delta P", deltaP)

print("A MAX P", apMAX)
print("A min P", apmin)
deltaAp = apMAX-apmin
print("Delta Ap", deltaAp)

deltaAP= deltaAp/deltaP
print("Delta A/Delta P: ", deltaAp/deltaP)


print("Error de i", errorI)
print("Error de p", errorP)
print("Total: ", deltaAI*errorI + deltaAP*errorP)

calcularDoblePres()
calcularSimplePres()