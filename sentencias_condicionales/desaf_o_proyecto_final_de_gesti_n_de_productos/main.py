# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"


# 1. Verificamos si el producto es perecedero
if product_type == "Perishable":
    
    # Aplicar 30% de descuento
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
        
    # Aplicar 20% de descuento
    elif 4 <= days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
        
    # Aplicar 10% de descuento
    elif days_until_expiration >= 7 or stock_level <= 50:
        print("10% discount applied")

# 2. Si no es perecedero
else:
    print("No discount available for non-perishable items.")