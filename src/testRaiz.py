import numpy as np

def algoritmo1(x, p, n):
    resultado = x - (((p/x)*(((1+x)**n)-1))-200000)
    return resultado

def algoritmo2(x, p, n):
    resultado = (((200000*(x/p))+1)**(1/n)) - 1
    return resultado

def algoritmo3(x, p, n):
    resultado = (p/200000)*(((1+x)**n)-1)
    return resultado

def algoritmo4(x, p, n):
    resultado = ((((200000*(x/p))+1)/((1+x)**(n/2)))**(2/n))-1
    return resultado

def algoritmo5(x, p, n):
    resultado = x - (((p/x)*(((1+x)**n)-1))-200000)/(((((-1)*p)/(x**2))*(((1+x)**n)-1))+((p/x)*n*((1+x)**n-1)))
    return resultado

def main():
    padron = np.float32(100849)
    k = np.float32(0)
    x = np.float32(0.001)
    n = np.float32(60)
    p = np.float32(padron / 700)
    print("k: ", 0)
    print("a: ", x)
    while k <= 30:
        x = algoritmo2(x, p, n)
        print("k: ", k + 1)
        print("a: ", x)
        k += 1

    print("Resultado: ", x)
main()