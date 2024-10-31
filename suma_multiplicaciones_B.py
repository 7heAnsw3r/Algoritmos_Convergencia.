def calcular_suma_simplificada(a, b):
    suma = 0
    suma_elementos_b = 0
    n = len(a)  # Suponemos que a y b tienen la misma dimensión n x n

    # Calcular la suma de elementos de b
    for j in range(n):
        suma_elementos_b += sum(b[j])

    # Calcular suma usando a y suma_elementos_b
    for i in range(n):
        suma += a[i] * suma_elementos_b

    multiplicaciones = n
    sumas = n

    return suma, multiplicaciones, sumas


# Ejemplo de uso:
a = [1, 2, 3, 4, 5]
b = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

resultado, multiplicaciones, sumas = calcular_suma_simplificada(a, b)
print("Resultado de Suma:", resultado)
print("Número total de multiplicaciones:", multiplicaciones)
print("Número total de sumas:", sumas)
