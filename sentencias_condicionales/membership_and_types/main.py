# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

# Write your code here
# --- 1. Operadores de Pertenencia ---
# Verificamos si las subcadenas existen en la descripción
contains_raw = 'raw' in description
contains_Imported = 'Imported' in description

# --- 2. Comparaciones de Tipo ---
# Verificamos si las variables tienen el tipo de dato esperado
price_is_float = type(price) is float
count_is_int = type(count) is int


print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)