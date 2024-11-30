# Método del punto fijo implementado manualmente
def fixed_point_method(g, x0, tol=1e-6, max_iter=100):
    """
    Método del punto fijo para resolver x = g(x).
    
    :parametro g: Función g(x)
    :parametro x0: Valor inicial
    :parametro tol: Tolerancia para la convergencia
    :parametro max_iter: Número máximo de iteraciones
    :return: Aproximación de la solución, número de iteraciones
    """
    x = x0
    for i in range(max_iter):
        x_next = g(x)
        if abs(x_next - x) < tol:
            return x_next, i + 1  # Solución encontrada y número de iteraciones
        x = x_next
    return x, max_iter  # Retorna la mejor aproximación después del máximo de iteraciones

# Parámetros iniciales
x0 = 0.5  # Valor inicial
tol = 1e-6  # Tolerancia

# Resolver la ecuación
solution_manual, iterations = fixed_point_method(g, x0, tol=tol)
solution_manual, iterations
