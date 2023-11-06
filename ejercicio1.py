def mover_piedras(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover piedra {n} desde {origen} a {destino}")
    else:
        mover_piedras(n-1, origen, auxiliar, destino)
        print(f"Mover piedra {n} desde {origen} a {destino}")
        mover_piedras(n-1, auxiliar, destino, origen)

mover_piedras(14, "x", "y", "z")
