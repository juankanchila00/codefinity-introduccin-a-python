# 1. Crear la lista inicial
vegetables = ["tomatoes", "potatoes", "onions"]

# 2. Eliminar "onions"
vegetables.remove("onions")

# 3. Agregar "carrots" si no está presente
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

# 4. Agregar "cucumbers" si no está presente
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

# 5. Ordenar la lista alfabéticamente
vegetables.sort()

# Resultado final
print(f"Updated Vegetable Inventory: {vegetables}")
