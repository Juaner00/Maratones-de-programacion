def main():
    testCase = int(input())

    for x in range(testCase):
        #Crear matriz
        n = input().split()
        matrix = []
        for i in range(int(n[2])):
            data = input().split()
            matrix.append(data)
            #matrix.append(input().split())
        #print(matrix)
        #Todos +
        negativo = False
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] < 0:
                    print("Test #{}: Non-symmetric.".format(x + 1))
                    negativo = True
                    break
            if negativo:
                break
        if negativo:
            continue

        #Simetrica
        simetrico = True
        for i in range(int(len(matrix) / 2) + 1):
            for j in range(len(matrix)):
                if matrix[i][j] != matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]:
                    simetrico = False
                    break
            if not simetrico:
                break
        if simetrico:
            print("Test #{}: Symmetric.".format(x + 1))
        else:
            print("Test #{}: Non-symmetric.".format(x + 1))

if __name__ == '__main__':
    main()
