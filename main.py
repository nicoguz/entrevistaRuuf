from math import ceil, floor

def max_paneles(a, b, x, y):
    # Se definen mejores nombres para las variables
    panel_a = a
    panel_b = b
    techo_x = x
    techo_y = y

    # Chequeo inicial
    if (panel_a > techo_x and panel_a > techo_y)\
        or (panel_b > techo_x and panel_b > techo_y)\
        or (techo_x < panel_a and techo_x < panel_b)\
        or (techo_y < panel_a and techo_y < panel_b):
        return 0

    if panel_a <= panel_b:
        panel_corto = panel_a
        panel_largo = panel_b
    else:
        panel_corto = panel_b
        panel_largo = panel_a

    # Definimos una heurística
    max_paneles = (techo_x*techo_y)//(panel_a*panel_b)

    # --- Configuración inicial ---
    # Alfa = número de paneles con su lado más corto hacia arriba (parado)
    # Beta = número de paneles con su lado más largo hacia arriba (acostado)
    alfa = techo_x//panel_corto
    beta = 0

    # Gamma = máximo número de paneles "parados" que caben "hacia abajo" (en el lado y del techo)
    # Theta = máximo número de paneles "acostados" que caben "hacia abajo" (en el lado y del techo)
    gamma = techo_y//panel_largo
    theta = techo_y//panel_corto

    # Partimos solo con paneles "parados"
    n_paneles = alfa * gamma

    if n_paneles == max_paneles:
        return n_paneles
    
    mayor_paneles_logrado = n_paneles
    
    # Iteramos reduciendo el número de paneles "parados"
    while alfa > 0:
        alfa -= 1

        techo_ocupado = alfa*panel_corto + beta*panel_largo
        # Vemos si cabe un panel acostado después de sacar uno parado
        if techo_x - techo_ocupado >= panel_largo:
            beta += 1

            # Se calcula nuevo número de paneles solo si logramos añadir uno acostado
            n_paneles = alfa*gamma + beta*theta

            if n_paneles == max_paneles:
                return n_paneles
            if n_paneles > mayor_paneles_logrado:
                mayor_paneles_logrado = n_paneles
    
    return mayor_paneles_logrado

def main(a, b, x, y):
    orientación_1 = max_paneles(a, b, x, y)
    orientación_2 = max_paneles(a, b, y, x)

    return max(orientación_1, orientación_2)

if __name__ == "__main__":
    a = 1
    b = 2
    x = 3
    y = 4
    print(main(a, b, x, y))
        
