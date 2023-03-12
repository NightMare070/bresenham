import matplotlib.pyplot as plt

# Pedimos al usuarios las coordenadas de la recta a graficar
x0 = int(input("Dame el valor de x0: "))
y0 = int(input("Dame el valor de y0: "))
x1 = int(input("Dame el valor de x1: "))
y1 = int(input("Dame el valor de y1: "))

# Creamos una lista donde se guardaran los puntos obtenidos
puntos = []

# Funcion del algoritmo de Bresenham


def bresenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    m = dy / dx
    puntos.append((x0, y0))

    # Algoritmo en caso de que m sea menor a 1
    if m < 1:
        pk = (2*dy) - dx
        if x0 < x1 and y0 < y1:
            while x0 != x1:
                if pk >= 0:
                    x0 += 1
                    y0 += 1
                    pk = pk + 2*(dy) - 2*(dx)
                    puntos.append((x0, y0))
                else:
                    x0 += 1
                    pk = pk + 2*(dy)
                    puntos.append((x0, y0))
        if x0 > x1 and y0 < y1:
            while x0 != x1:
                if pk >= 0:
                    x0 -= 1
                    y0 += 1
                    pk = pk + 2*(dy) - 2*(dx)
                    puntos.append((x0, y0))
                else:
                    x0 -= 1
                    pk = pk + 2*(dy)
                    puntos.append((x0, y0))
        if x0 < x1 and y0 > y1:
            while x0 != x1:
                if pk >= 0:
                    x0 += 1
                    y0 -= 1
                    pk = pk + 2*(dy) - 2*(dx)
                    puntos.append((x0, y0))
                else:
                    x0 += 1
                    pk = pk + 2*(dy)
                    puntos.append((x0, y0))
        if x0 > x1 and y0 > y1:
            while x0 != x1:
                if pk >= 0:
                    x0 -= 1
                    y0 -= 1
                    pk = pk + 2*(dy) - 2*(dx)
                    puntos.append((x0, y0))
                else:
                    x0 -= 1
                    pk = pk + 2*(dy)
                    puntos.append((x0, y0))
    # Algoritmo en  caso de que m sea mayor a 1
    else:
        pk = 2*(dx) - dy
        if y0 < y1 and x0 < x1:
            while y0 != y1:
                if pk >= 0:
                    y0 += 1
                    x0 += 1
                    pk = pk + 2*(dx) - 2*(dy)
                    puntos.append((x0, y0))
                else:
                    y0 += 1
                    pk = pk + 2*(dx)
                    puntos.append((x0, y0))
        if y0 > y1 and x0 < x1:
            while y0 != y1:
                if pk >= 0:
                    y0 -= 1
                    x0 += 1
                    pk = pk + 2*(dx) - 2*(dy)
                    puntos.append((x0, y0))
                else:
                    y0 -= 1
                    pk = pk + 2*(dx)
                    puntos.append((x0, y0))
        if y0 < y1 and x0 > x1:
            while y0 != y1:
                if pk >= 0:
                    y0 += 1
                    x0 -= 1
                    pk = pk + 2*(dx) - 2*(dy)
                    puntos.append((x0, y0))
                else:
                    y0 += 1
                    pk = pk + 2*(dx)
                    puntos.append((x0, y0))
        if y0 > y1 and x0 > x1:
            while y0 != y1:
                if pk >= 0:
                    y0 -= 1
                    x0 -= 1
                    pk = pk + 2*(dx) - 2*(dy)
                    puntos.append((x0, y0))
                else:
                    y0 -= 1
                    pk = pk + 2*(dx)
                    puntos.append((x0, y0))

# Funcion que determina condiciones y llama al algoritmo de bresenham
def algoritmo(x0, y0,x1,y1):
    if x0 == x1 and y0 == y1:
        puntos.append((x0, y0))

    if x0 == x1:
        while y0 != y1:
            if y0 > y1:
                puntos.append((x0, y0))
                y0 -= 1
            else:
                puntos.append((x0, y0))
                y0 += 1

    if y0 == y1:
        while x0 != x1:
            if x0 > x1:
                puntos.append((x0, y0))
                x0 -= 1
            else:
                puntos.append((x0, y0))
                x0 += 1
        puntos.append((x1, y1))

    else:
        bresenham(x0, y0,x1,y1)

# Llamada de condiciones y aplicación de algoritmo en caso necesario
algoritmo(x0, y0,x1,y1)

# Graficación de los puntos obtenidos
x, y = zip(*puntos)
plt.plot(x, y, marker="s", color="black", markersize=10, linewidth=0)
plt.plot([x0, x1], [y0,y1], color="red")
plt.show()

print(puntos)
