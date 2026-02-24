# 1. Inicializar listas individuales
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# 2. Crear lista principal (Deli Department)
deli_dept = [meat, cheese, condiment]

# Imprimir estado inicial
print(f"Initial Deli List: {deli_dept}")

# 3. Reabastecer artículo: Si es "Ham" y stock < 100, actualizar a 100
# Accedemos a meat[0] para el nombre y meat[2] para la cantidad

if meat[0] == "Ham" and meat[2] < 100:
    meat[2] = 100

# 4. Agregar carne de temporada
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

# 5. Eliminar condimento de la lista principal
deli_dept.remove(condiment)

# 6. Ordenar lista alfabéticamente (por el primer elemento de cada sublista)
deli_dept.sort()

# Resultado final
print(f"Updated Deli List: {deli_dept}")