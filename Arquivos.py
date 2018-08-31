import math
from random import *

class Arquivos():
    #Inicializando com a matriz e os vetores pra guardar as posicoes X-Y
    def __init__(self,n):
        self.matriz = []
        self.vet_x = []
        self.vet_y = []
        self.qnt_cidades = n
    
    def le_arq(self,path):
        #Inicializando a matriz com tamanho NxN
        #Cada posição da matriz contém uma lista com a distância da cidade da posição para todas as outras cidades .
        self.matriz = self.constroiMatriz(self.qnt_cidades,[])
        arq = open(path,'r')
        texto = arq.readlines()
        for linha in texto:
            linha = linha.split()
            self.vet_x.append(linha[1])
            self.vet_y.append(linha[2])
        arq.close()
        for i in range(0,self.qnt_cidades-1):
            self.matriz[i][i] = 0
            for j in range(i+1,self.qnt_cidades):
                if(self.matriz[i][j] == -1):
                    delta_x = int(self.vet_x[i]) - int(self.vet_x[j])
                    delta_y = int(self.vet_y[i]) - int(self.vet_y[j])
                    self.matriz[i][j] = round(math.sqrt((delta_x ** 2) + (delta_y ** 2)),2)
                    self.matriz[j][i] = self.matriz[i][j]
                else:
                    pass
        
    
    def constroiMatriz(self,n,matriz):
        for i in range(1,n+1):
            linha = []
            for j in range(1,n+1):
                linha.append(-1)
            matriz.append(linha)
        return matriz

    def constroi_solucao_aleatoria(self, cidades):
        j = 1
        cidade_escolhida = -1
        s = list()
        s.append(0)
        while(len(s) != 50):
            cidade_escolhida = randint(1,len(cidades))
            if cidade_escolhida not in s:
                s.append(cidade_escolhida)
        print(len(s))
        print(s)


#Criando a instância de arquivos e informando a quantidade de registros a serem lidos (51)
arq = Arquivos(51)

#Lendo o arquivo e preenchendo a matriz de distâncias entre as cidades
arq.le_arq('C:/Users/Wermeson Rocha/Documents/UFC/6º Semestre/Inteligência Artificial/arquivos_base/arquivos_base/C50.txt')
#print(arq.matriz)
lista = list(range(52))
lista = lista[1:]
arq.constroi_solucao_aleatoria(lista)
print(arq.matriz[0][50])