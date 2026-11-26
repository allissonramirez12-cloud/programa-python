"""
Curso: Fundamentos de Programación (213022) - UNAD
Fase 5 - Evaluación Final POA: Problema 1 (Nivel de compromiso en sesiones)
"""


def clasificar_compromiso(duracion_segundos: int, numero_clics: int) -> str:
    """
    Calcula el nivel de compromiso de una sesión según duración y clics.
    - 'Alto': duración > 180 s y clics > 8
    - 'Bajo': duración < 60 s o clics < 3
    - 'Medio': en cualquier otro caso
    """
    if duracion_segundos > 180 and numero_clics > 8:
        return "Alto"
    elif duracion_segundos < 60 or numero_clics < 3:
        return "Bajo"
    else:
        return "Medio"


def generar_reporte_sesiones(sesiones: list) -> None:
    """Recorre la matriz de sesiones e imprime el ID y su clasificación."""
    print("=" * 45)
    print("INFORME DE COMPROMISO POR SESIÓN")
    print("=" * 45)
    print(f"{'ID Cliente':<15} {'Clasificación':<15}")
    print("-" * 45)

    for sesion in sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(duracion, clics)
        print(f"{str(id_cliente):<15} {clasificacion:<15}")

    print("=" * 45)


def principal() -> None:
    # Matriz con al menos 5 sesiones: [ID del Cliente, Duración (s), Número de clics]
    matriz_sesiones = [
        ["CLI-101", 240, 12],  # Alto (>180s y >8 clics)
        ["CLI-102", 45, 6],     # Bajo (<60s)
        ["CLI-103", 150, 2],    # Bajo (<3 clics)
        ["CLI-104", 120, 5],    # Medio
        ["CLI-105", 180, 9],    # Medio (duración no es estrictamente > 180)
        ["CLI-106", 310, 15],   # Alto (>180s y >8 clics)
    ]

    generar_reporte_sesiones(matriz_sesiones)


if __name__ == "__main__":
    principal()