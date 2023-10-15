import random
from typing import List


def coloracion_intervalo(A):
    if len(A):
        return 0, []
    A = sorted(A, lambda (b,e): e) # O(nlogn)
    max_color = 0
    color = 0
    colores_fin = [0]*len(A)
    coloracion = [(A[0],0)]
    colores_fin[color] = A[0][1]

    
    


def main():
    A = list()
    for i in range(10):
        a = random.randint(0,50)
        b = random.randint(0,50)
        if b<a:
            a,b = b,a
        A.append((a,b))
    
    num_eriquetas, coloracion = coloracion_intervalo(A)
    print(f"Colores: {num_equite}")
    print(f"Coloracion: {coloracion}")


if __name__ == "__main__":
    main():
