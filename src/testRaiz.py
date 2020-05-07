import numpy as np

a = 200000

def algoritmo1(i, p, n):
    resultado = i - (((p/i)*(((1+i)**n)-1))-a)
    return resultado

def algoritmo2(i, p, n):
    resultado = (((a * (i / p)) + 1) ** (1 / n)) - 1
    return resultado

def algoritmo3(i, p, n):
    resultado = (p/a)*(((1 + i) ** n) - 1)
    return resultado

def algoritmo4(i, p, n):
    resultado = ((((a*(i/p))+1)/((1+i)**(n/2)))**(2/n))-1
    return resultado

def algoritmo5(i, p, n):
    resultado = i - (((p/i)*(((1+i)**n)-1))-a)/(((((-1)*p)/(i**2))*(((1+i)**n)-1))+((p/i)*n*((1+i)**n-1)))
    return resultado

def main():
    padron = np.float32(100849)
    k = np.float32(0)
    i = np.float32(0.001)
    n = np.float32(60)
    p = np.float32(padron / 700)
    print("Iteration: ", 0)
    print("Interest: ", i)
    while k <= 30:
        i = algoritmo2(i, p, n)
        print("Iteration: ", k + 1)
        print("Interest: ", i)
        k += 1

    print("Result: ", i)
main()