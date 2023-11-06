naves = [
    {"nombre": "Cometa Veloz", "longitud": 50, "tripulantes": 4, "pasajeros": 20},
    {"nombre": "Voyager", "longitud": 150, "tripulantes": 10, "pasajeros": 50},
    {"nombre": "Titán del Cosmos", "longitud": 70, "tripulantes": 6, "pasajeros": 30},
    {"nombre": "GX-1", "longitud": 80, "tripulantes": 4, "pasajeros": 30},
    {"nombre": "James Webb", "longitud": 100, "tripulantes": 8, "pasajeros": 40},
    {"nombre": "genesis", "longitud": 200, "tripulantes": 12, "pasajeros": 60},
]

naves_ordenadas = sorted(naves, key=lambda x: (x["nombre"], -x["longitud"]))

for nave in naves:
    if nave["nombre"] in ["Cometa Veloz", "Titán del Cosmos"]:
        print(nave)

top_5_pasajeros = sorted(naves, key=lambda x: -x["pasajeros"])[:5]

nave_mayor_tripulacion = max(naves, key=lambda x: x["tripulantes"])

naves_GX = [nave for nave in naves if nave["nombre"].startswith("GX")]

naves_con_seis_o_mas_pasajeros = [nave for nave in naves if nave["pasajeros"] >= 6]

nave_mas_pequena = min(naves, key=lambda x: x["longitud"])
nave_mas_grande = max(naves, key=lambda x: x["longitud"])

print("Naves ordenadas por nombre ascendente y longitud descendente:")
for nave in naves_ordenadas:
    print(nave)

print("\nInformación de las naves 'Cometa Veloz' y 'Titán del Cosmos':")
for nave in naves:
    if nave["nombre"] in ["Cometa Veloz", "Titán del Cosmos"]:
        print(nave)

print("\nLas cinco naves con más pasajeros:")
for nave in top_5_pasajeros:
    print(nave)

print("\nNave con mayor tripulación:")
print(nave_mayor_tripulacion)

print("\nNaves cuyo nombre comienza con 'GX':")
for nave in naves_GX:
    print(nave)

print("\nNaves con seis o más pasajeros:")
for nave in naves_con_seis_o_mas_pasajeros:
    print(nave)

print("\nNave más pequeña:")
print(nave_mas_pequena)

print("\nNave más grande:")
print(nave_mas_grande)
