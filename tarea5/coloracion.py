from typing import List, Tuple

Intervalo = Tuple[int, int]
Coloracion = Tuple[int, Intervalo]


def imprimir_intervalos(C: List[Coloracion]):
    range_max = max([e for _, (_, e) in C])
    range_min = min([b for _, (b, _) in C])
    print("|", end="")
    for i in range(range_min, range_max):
        print(f"{i:2d}  |", end="")
    print('')
    colores = max([c for c, _ in C])
    for color in range(colores+1):
        ini = range_min
        for (b, e) in [(b, e) for c, (b, e) in C if c == color]:
            print(" "*(b-ini)*(5 if ini == range_min else 4), end="")
            print("|", end='')
            print(f"{color}"*(e-b-1)*5, end='')
            print(f"{color}"*4, end="")
            print("|", end="")
            ini = e
        print()


def coloracion_intervalo(I: List[Intervalo]) -> Tuple[int, List[Coloracion]]:
    if I == []:
        return 0, []
    I = sorted(I, key=lambda i: i[1])  # O(n log n)
    colores: int = 1
    coloracion: List[Coloracion] = [(0, I[0])]
    puntero: int = 0
    for b, e in I[1:]:
        color, (_, ec) = coloracion[puntero]
        if b > ec:
            coloracion.append((color, (b, e)))
            puntero += 1
        else:
            coloracion.append((colores, (b, e)))
            colores += 1
    return colores, coloracion


def contar_coloracion(I: List[Tuple[float, float]]):
    n = len(I)
    if n == 0:
        return 0
    I = sorted(I, key=lambda i: i[1])
    colores = 1
    coloracion = [0]*n
    puntero = 0
    for i, (b, _) in enumerate(I[1:]):
        _, descarte = I[puntero]
        if b > descarte:
            coloracion[i+1] = coloracion[puntero]
            puntero += 1
        else:
            coloracion[i+1] = colores
            colores += 1
    return colores


def main():
    I: List[Intervalo] = [
        (1, 3), (4, 6), (2, 5), (0, 8), (9, 11)
    ]
    I = [(0, 6), (1, 3), (4, 5), (2, 7), (8, 9)]
    I = [(0, 2), (1, 3), (2, 4), (3, 6), (2, 7), (4, 8), (5, 9), (7, 10)]
    num_etiquetas, coloracion = coloracion_intervalo(I)
    print(f"Colores: {contar_coloracion(I)}")
    print(f"Coloración: {coloracion}")
    imprimir_intervalos(coloracion)


if __name__ == "__main__":
    main()

# [((1, 8), 0), ((5, 10), 1), ((3, 10), 2), ((11, 12), 0), ((1, 13), 3), ((12, 15), 1), ((2, 16), 4), ((12, 17), 2), ((16, 18), 3), ((12, 19), 5)]
