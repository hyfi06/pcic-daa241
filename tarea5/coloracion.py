from typing import List, Tuple

Intervalo = Tuple[int, int]
Coloracion = Tuple[Intervalo, int]


def imprimir_intervalos(C: List[Coloracion]):
    range_max = max([e for (_, e), _ in C])
    range_min = min([b for (b, _), _ in C])
    print("|", end="")
    for i in range(range_min, range_max):
        print(f"-{i:2d}-|", end="")
    print('')

    for (b, e), c in C:
        print(" "*(b-range_min)*5, end="")
        print("|", end='')
        print(f"{c}"*(e-b-1)*5, end='')
        print(f"{c}"*4, end="")
        print("|")
    print()


def coloracion_intervalo(I: List[Intervalo]) -> Tuple[int, List[Coloracion]]:
    n: int = len(I)
    if n == 0:
        return 0, []
    I = sorted(I, key=lambda i: i[1])  # O(n log n)
    max_color: int = 0
    color: int = 0
    colores_fin: List[float] = [0]*n
    coloracion: List[Coloracion] = [(I[0], 0)]
    colores_fin[color] = I[0][1]

    for (b, e) in I[1:]:
        if b > colores_fin[color]:
            coloracion.append(((b, e), color))
            colores_fin[color] = e
            if color == max_color:
                color = 0
            else:
                color += 1
        else:
            max_color += 1
            coloracion.append(((b, e), max_color))
            colores_fin[max_color] = e
    return max_color+1, coloracion


def main():
    I: List[Intervalo] = [
        (1, 3), (4, 6), (2, 5), (0, 8), (9, 11)
    ]
    num_etiquetas, coloracion = coloracion_intervalo(I)
    print(f"Colores: {num_etiquetas}")
    print(f"Coloración: {coloracion}")
    imprimir_intervalos(coloracion)


if __name__ == "__main__":
    main()

# [((1, 8), 0), ((5, 10), 1), ((3, 10), 2), ((11, 12), 0), ((1, 13), 3), ((12, 15), 1), ((2, 16), 4), ((12, 17), 2), ((16, 18), 3), ((12, 19), 5)]
