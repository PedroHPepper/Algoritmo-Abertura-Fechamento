class TransformaImagem:
    def erosão(self, matrizA):
        janela = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        matrizAB = []
        for l in range(len(matrizA)):
            linha = []
            for c in range(len(matrizA[0])):

                for x in range(len(janela)):
                    for y in range(len(janela)):
                        if ((l == 0 and x == 0) or (l == len(matrizA) - 1 and x == 2) or (c == 0 and y == 0) or (
                                c == len(matrizA[0]) - 1 and y == 2)):
                            janela[x][y] = 0
                        else:
                            if (x == 0):
                                linhaMatrizA = l - 1
                            if (x == 1):
                                linhaMatrizA = l
                            if (x == 2):
                                linhaMatrizA = l + 1
                            if (y == 0):
                                colunaMatrizA = c - 1
                            if (y == 1):
                                colunaMatrizA = c
                            if (y == 2):
                                colunaMatrizA = c + 1

                            janela[x][y] = matrizA[linhaMatrizA][colunaMatrizA]
                resultado=1
                for x in range(len(janela)):
                    for y in range(len(janela)):
                        if(janela[x][y]==0):
                            resultado=0
                            break

                linha.append(resultado)
            matrizAB.append(linha)

        return matrizAB

    def dilatação(self, matrizA):
        janela = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        matrizAB = []
        for l in range(len(matrizA)):
            linha = []
            for c in range(len(matrizA[0])):

                for x in range(len(janela)):
                    for y in range(len(janela)):
                        if ((l == 0 and x == 0) or (l == len(matrizA) - 1 and x == 2) or (c == 0 and y == 0) or (
                                c == len(matrizA[0]) - 1 and y == 2)):
                            janela[x][y] = 0
                        else:
                            if (x == 0):
                                linhaMatrizA = l - 1
                            if (x == 1):
                                linhaMatrizA = l
                            if (x == 2):
                                linhaMatrizA = l + 1
                            if (y == 0):
                                colunaMatrizA = c - 1
                            if (y == 1):
                                colunaMatrizA = c
                            if (y == 2):
                                colunaMatrizA = c + 1

                            janela[x][y] = matrizA[linhaMatrizA][colunaMatrizA]
                resultado = 0
                for x in range(len(janela)):
                    for y in range(len(janela)):
                        if(janela[x][y] == 1):
                            resultado = 1
                            break

                linha.append(resultado)
            matrizAB.append(linha)

        return matrizAB

