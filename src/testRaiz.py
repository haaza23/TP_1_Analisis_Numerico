import numpy as np

A = 200000

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
    xkMasUno = xk - (((P/xk)*(((1+xk)**n)-1))-A)/(((((-1)*P)/(xk**2))*(((1+xk)**n)-1))+((P/xk)*n*((1+xk)**n-1)))
    return xkMasUno

def main():
    NP = np.float32(100849)
    P = np.float32(NP / 700)
    n = 360
    k = np.float32(0)
    xk = np.float32(1e-16)
    xkSiguiente = algoritmo5(xk, P, n)
    error = abs((xkSiguiente - xk) / xkSiguiente)
    print('{:^10}{:^10}{:^10}{:^10}'.format('k', 'xk', 'xk+1', 'error'))
    while (error >= 1e-5):
        xkSiguiente = algoritmo5(xk, P, n)
        error = abs((xkSiguiente - xk) / xkSiguiente)
        print('{:^10}{:^10.5f}{:^10.5f}{:^10.5f}'.format(k, float(xk), float(xkSiguiente), float(error)))
        xk = xkSiguiente
        k += 1
    print("La raiz es: ", xk)
main()
