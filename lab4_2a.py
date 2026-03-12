import math

"""
Problema 2.a., laboratorio 4 teoría de probabilidades.
"""
def ganancias(x,y):
    return 0.15*x-0.1*y

def bin(n, p, k):
        return math.comb(n, k) * (p**k) * ((1-p)**(n-k))
valor_max=[]

#Representación de la suma de ganancias esperadas para cada valor de x entre 1 y 10.
for x in range(1,11):
    sumatoria=0
    for k in range(0,x+1):
        sumatoria+=bin(10,1/3,k)*ganancias(k,x)
    valor_max.append(sumatoria)
    print(f"Para x={x}, la ganancia esperada es: {sumatoria}")

print(f"El valor más óptimo de ganancia esperada es {max(valor_max)} en el valor de x={valor_max.index(max(valor_max))+1}")
