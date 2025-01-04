from math import ceil, floor

def main(a, b, x, y):
    # Se definen mejores nombres para las variables
    panel_a = a
    panel_b = b
    techo_x = x
    techo_y = y

    if panel_a <= panel_b:
        panel_corto = panel_a
        panel_largo = panel_b
    else:
        panel_corto = panel_b
        panel_largo = panel_a

    # Configuración inicial
    # Alfa = número de paneles con su lado más corto hacia arriba (parado)
    # Beta = número de paneles con su lado más largo hacia arriba (acostado)
    alfa_inicial = techo_x//panel_corto
    beta_inicial = 0

    # Gamma = máximo número de paneles "parados" que caben "hacia abajo" (en el lado y del techo)
    # Theta = máximo número de paneles "acostados" que caben "hacia abajo" (en el lado y del techo)
    gamma = techo_y//panel_largo
    theta = techo_y//panel_corto
