# Estudiante: Carlos Andres Sepulveda
# Grupo: 423
# Problema 3 - Reabastecimiento de inventario

def calcular_cantidad(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


inventario = [
    ["A001", "Teclado", 8, 15],
    ["A002", "Mouse", 20, 10],
    ["A003", "Monitor", 4, 12],
    ["A004", "Memoria USB", 10, 10],
    ["A005", "Disco SSD", 3, 8]
]

print("=" * 45)
print("INFORME DE REABASTECIMIENTO DE INVENTARIO")
print("=" * 45)
print(f"{'Articulo':<25}{'Cantidad a pedir':>20}")
print("-" * 45)

for articulo in inventario:
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_cantidad(
        stock_actual, stock_minimo
    )

    print(f"{nombre:<25}{cantidad:>20}")

print("=" * 45)
