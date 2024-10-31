import math

def calcular_arctan(x, n):
    """Calcula el término n de la serie de Maclaurin para arctan(x)."""
    return ((-1) ** (n + 1)) * (x ** (2 * n - 1)) / (2 * n - 1)

def calcular_pi_aproximado(error_deseado):
    """Calcula el número de términos necesarios para alcanzar el error deseado usando la fórmula de arctan."""
    n1 = n2 = 1
    resultado1 = resultado2 = 0
    while abs(4 * (4 * resultado1 - resultado2) - math.pi) >= error_deseado:
        resultado1 += calcular_arctan(1 / 5, n1)
        resultado2 += calcular_arctan(1 / 239, n2)
        n1 += 1
        n2 += 1
    pi_aproximado = 4 * (4 * resultado1 - resultado2)
    return n1, n2, pi_aproximado

error_deseado = 1e-3
n1, n2, pi_aproximado = calcular_pi_aproximado(error_deseado)
print(f"Número de términos necesarios: n1={n1}, n2={n2}")
print(f"Valor aproximado de pi: {pi_aproximado}")


