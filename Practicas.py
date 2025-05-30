def met_mergesort(arr):
    if len(arr) <= 1:
        return arr[0] if arr else 0  # retorna el único número o 0 si está vacía
    
    mid = len(arr) // 2
    izq = arr[:mid]
    der = arr[mid:]

    suma_izq = met_mergesort(izq)
    suma_der = met_mergesort(der)

    return suma_izq + suma_der

# Ejemplo de uso
lista1 = [4, 6, 8, 4, 6, 2]
z = met_mergesort(lista1)
print(f"La suma es: {z}")
