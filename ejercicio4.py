# Función para restar dos polinomios
def restar_polinomios(polinomio1, polinomio2):
    len1, len2 = len(polinomio1), len(polinomio2)
    if len1 > len2:
        polinomio2.extend([0] * (len1 - len2))
    elif len2 > len1:
        polinomio1.extend([0] * (len2 - len1))
    
    resultado = [a - b for a, b in zip(polinomio1, polinomio2)]
    return resultado

def dividir_polinomios(polinomio1, polinomio2):
    if polinomio2 == [0]:
        return "No se puede dividir por cero"
    resultado, residuo = [], polinomio1[:]
    while len(residuo) >= len(polinomio2):
        coeficiente = residuo[0] / polinomio2[0]
        
        resultado.append(coeficiente)
        
        residuo = restar_polinomios(residuo, [coeficiente * x for x in polinomio2])
    
    return resultado, residuo

def eliminar_termino(polinomio, exponente):
    if exponente < len(polinomio):
        polinomio[exponente] = 0
    return polinomio

def existe_termino(polinomio, exponente):
    return exponente < len(polinomio) and polinomio[exponente] != 0

polinomio1 = [3, 0, 2]
polinomio2 = [1, 2, 0]
print("Restar polinomios:", restar_polinomios(polinomio1, polinomio2))
print("Dividir polinomios:", dividir_polinomios(polinomio1, polinomio2))
print("Eliminar término:", eliminar_termino(polinomio1, 2))
print("¿Existe término en el polinomio?", existe_termino(polinomio1, 2))
