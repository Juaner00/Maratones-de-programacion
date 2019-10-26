def main():
    for i in range(int(input())):
        leng = int(input())
        F = list(map(int, input().split()))
        R = list(map(int, input().split()))

        # Index Usados
        xU = [0] * leng
        yU = [0] * leng

        # Crear la matriz
        matriz = []
        for i in range(leng):
            matriz.append([0] * leng)

        # Poner 1 los que son 0
        for i in range(leng):
            if F[i] == 0:
                xU[i] = 1
            if R[i] == 0:
                yU[i] = 1

        for indX, x in enumerate(F):
            if x == 0:
                continue
            for indY, y in enumerate(R):
                if y == 0:
                    continue
                if x == y and yU[indY] == 0:
                    matriz[indY][indX] = x
                    xU[indX] = 1
                    yU[indY] = 1
                    break

        # Si falta uno en y
        while yU.count(0) > 0:
            try:
                indY = yU.index(0)
                y = R[indY]
                for indX, x in enumerate(F):
                    if x >= y:
                        matriz[indY][indX] = y
                        yU[indY] = 1
                        break
            except:
                break

        # Si falta uno en x
        while xU.count(0) > 0:
            try:
                indX = xU.index(0)
                x = F[indX]
                for indY, y in enumerate(R):
                    if y >= x:
                        matriz[indY][indX] = x
                        xU[indX] = 1
                        break
            except:
                break

        # Contar los cubos utilizados
        cantInit = contBloques(matriz)

        # Llenar la matriz con los máximos cubos
        matriz2 = matriz

        for indX, x in enumerate(F):
            for indY, y in enumerate(R):
                if x >= y:
                    matriz2[indY][indX] = y
                if x < y:
                    matriz2[indY][indX] = x

        # Contar los bloques utilizados
        cantLLena = contBloques(matriz2)

        print("Matty needs at least {0} blocks, and can add at most {1} extra blocks.".format(cantInit,
                                                                                              cantLLena - cantInit))


def contBloques(matriz):
    # Contar los bloques utiliados
    cant = 0
    for i in matriz:
        cant += sum(i)
    return cant


main()
