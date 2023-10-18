import random
from typing import List, Tuple

Peso = float


def distribuir_perros(P: List[Peso]) -> List[List[Peso]]:
    P = sorted(P)
    corrales: List[List[Peso]] = list()
    corral = 0
    corrales.append([P[0]])
    for peso in P[1:]:
        if peso > corrales[corral][0]+5:
            corrales.append([peso])
            corral += 1
        else:
            corrales[corral].append(peso)
    return corrales


def corrales_raros(P: List[Peso]) -> List[List[Peso]]:
    P = sorted(P)
    corrales: List[List[Peso]] = list()
    corrales.append([P[0]])
    for peso in P[1:]:
        if peso < 5:
            corrales.append([peso])
        else:
            if corrales[-1][0] < 5:
                corrales.append([peso])
            else:
                corrales[-1].append(peso)
    return corrales


def contar_corrales(P: List[Peso]) -> int:
    if P == []:
        return 0
    P = sorted(P)
    corrales: int = 1
    umbral = P[0] + 5
    for peso in P[1:]:
        if peso > umbral:
            corrales += 1
            umbral = peso + 5
    return corrales


def main():
    P = [7.1, 8.3, 24.1, 3.4, 10.4]
    corrales = contar_corrales(P)
    print(corrales)


if __name__ == "__main__":
    main()
