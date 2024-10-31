import math

def calcular_arctan(x,tolerancia):
    i = 1
    resultado = 0
    while abs(4 * resultado - math.pi) >= tolerancia:
        #Calculamos el termino i-ésimo de nuestra serie
        termino = ((-1) ** (i+1)) * (x ** (2 * i - 1)) / (2 * i - 1)
        resultado += termino
        i += 1
    return i

# En nuestro primer ejemplo nos pide tener una tolerancia de 10^-3
tolerancia_1 = 1e-3
primera_tolerancia = calcular_arctan(1,tolerancia_1)
print(f"Número de términos necesarios para  |4P_n(1) - π| < 10^(-3): {primera_tolerancia}")

# Número de términos necesarios para  |4P_n(1) - π| < 10^(-3): 1001

# En nuestro segundo ejemplo nos pide tener una tolerancia de 10^-10
tolerancia_2 = 1e-10
segunda_tolerancia = calcular_arctan(1,tolerancia_2)
print(f"Número de términos necesarios para  |4P_n(1) - π| < 10^(-10): {segunda_tolerancia}")

# Ya que estamos tratando de encontrar la tolerancia para un numero tan bajo como lo es 10^-10,
# implica un tiempo de ejecucion demasiado elevado