# Datos de entrada (ejemplo)

shelf1 = ("celery", "spinach", "cucumbers")

shelf1_update = ["tomatoes", "celery", "cilantro"]


# 1. Convertir la lista en una tupla
shelf1_update_tuple = tuple(shelf1_update)

# 2. Concatenar las tuplas para crear una nueva
shelf1_concat = shelf1 + shelf1_update_tuple

# 3. Contar las apariciones de "celery"
celery_count = shelf1_concat.count("celery")

# 4. Encontrar el índice de la primera aparición de "celery"
celery_index = shelf1_concat.index("celery")

# --- Visualización de resultados ---

print("Updated Shelf #1:", shelf1_concat)
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)




