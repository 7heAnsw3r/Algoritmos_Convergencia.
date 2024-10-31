def calcular_suma(a, b):
    suma = 0
    n = len(a)  # Suponemos que a y b tienen la misma dimensión n x n

    for i in range(n):
        for j in range(n):
            suma += a[i] * b[j][i]

    multiplicaciones = n * n
    sumas = n * (n - 1)

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

resultado, multiplicaciones, sumas = calcular_suma(a, b)
print("Resultado de de la suma :", resultado)
print("Número total de multiplicaciones:", multiplicaciones)
print("Número total de sumas:", sumas)
