import cmath

def calcular_raices(a, b, c):
    if a == 0:
        print("No es una ecuación cuadrática.")
        return None

    # Calcular el discriminante
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        # Dos raíces reales y diferentes
        x1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    elif discriminante == 0:
        # Una raíz real doble
        x1 = x2 = -b / (2 * a)
    else:
        # Dos raíces complejas conjugadas
        realParte = -b / (2 * a)
        imaginarioParte = cmath.sqrt(-discriminante) / (2 * a)
        x1 = realParte + imaginarioParte * 1j
        x2 = realParte - imaginarioParte * 1j

    print(f"Las raíces son: x1 = {x1}, x2 = {x2}")
    return x1, x2

# Ejemplo de uso:
a, b, c = 1, -3, 2  # Coeficientes de la ecuación cuadrática
calcular_raices(a, b, c)

a, b, c = 1, 2, 1  # Coeficientes de otra ecuación cuadrática
calcular_raices(a, b, c)

a, b, c = 1, 1, 1  # Coeficientes de una ecuación cuadrática con raíces complejas
calcular_raices(a, b, c)
