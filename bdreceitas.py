# -*- coding: cp1252 -*-
import json
import re

class Receita:
    def __init__(self, nome,secao):
        self.nome=nome
        self.section=secao
        self.totalReceitas=8183

        ''' A função de ajuste, tem como objetivo estruturar o arquivo Json
            De forma que seja possivel consultar seus dados por categoria'''
        aux=self.section[0]
        self.ingredientes = aux['conteudo']

        if len(self.section) == 1:
            self.temPreparo = False
            self.preparo = list()
        else:
            
            aux2=self.section[1]
            self.preparo = aux2['conteudo']
            self.temPreparo = True
        
    def ajuste(self):
        ''' A função de ajuste, tem como objetivo estruturar o arquivo Json
            De forma que seja possivel consultar seus dados por categoria'''
        aux=self.section[0]
        self.ingredientes = aux['conteudo']

        if len(self.section) < 2:
            self.temPreparo = False
            aux2=self.section[1]
            self.preparo = aux2['conteudo']
        else:
            self.temPreparo = True

        #self.section = self.section.replace("[{u'conteudo': [u'","")
        #self.section = self.section.replace("', u'","\n")

    def teste(self):
        self.teste = self.ingredientes['conteudo']

        for item in self.ingredientes:
            print(item)
        #print (self.teste[3])

    ''' --- [ FUNÇÕES DE IMPRESSAO ] --- '''
    def imprimirNome(self):
        print (self.nome)

    def imprimirIngredientes(self):
        for item in self.ingredientes:
            print(item)

    def imprimirPreparo(self):
        if self.temPreparo == True:
            for item in self.preparo:
                print(item)
        else:
            print ("Nao tem modo de preparo")

    def imprimirReceita(self):
        print("-------------------------- [ RECEITA ] --------------------------")
        print (self.nome)
        print("------------------------ [ INGREDIENTES ] -----------------------")
        for item in self.ingredientes:
            print(item)
        print("-------------------------- [ PREPARO ] --------------------------")
        if self.temPreparo == True:
            for item in self.preparo:
                print(item)
        else:
            print ("Nao tem modo de preparo")

    ''' --- [ FUNÇÕES DE RETORNO ] --- '''
    def getNome(self):
        return self.nome

    def getIngredientes(self):
        return self.ingredientes

    def getPreparo(self):
        return self.preparo

    ''' --- [ FUNÇÕES DE QUANTIDADES ] --- '''

    def getQuantidadeNome(self):
        return len(self.nome)

    def getQuantidadeIngredientes(self):
        return len(self.ingredientes)

    def getQuantidadePreparo(self):
        if self.temPreparo == True:
            return len(self.preparo)
        else:
            return 0

    def temModoPreparo(self):
        return self.temPreparo

        
            
    ''' --- [ FUNÇÕES DE VERIFICAÇÃO] ---
        Nessa parte, os códigos verificam sem uma palavra está contida
        no titulo ou nos ingredientes da receita pesquisada, ao
        encontrar ou não encontrar, um resultado True ou false retorna'''
    def receitaDe(self,palavra):
        if re.search(palavra, self.nome, re.IGNORECASE):
            return True
        return False
    
    def receitaTem(self,palavra):
        for item in self.ingredientes:
            if re.search(palavra, item, re.IGNORECASE):
                return True
        return False
    
    ''' --- [ FUNÇÕES DE GLOBAIS ] ---
        Nessa parte, estão os códigos que fazem consultas em todas as
        receitas. Dei o nome de *FG justamamente por isso'''
    def queReceitasPossoFazerCom(self,listaIngredientes,receitas):
        resultado  = list() # Onde serão armazenadas as receitas encontradas
        totalIngredientes = len(listaIngredientes) #numero total de ingredientes procurados
        contador=0 #contador de ingredientes encontrados
        i = 0 # contador do primeiro laço
        # Esse laço percorre toda a lista de receitas
        while i < self.totalReceitas:
            j = 0  # contador do segundo laço
            # Esse laço percorr a lista de ingredientes procurados
            while j < totalIngredientes:
                k = 0;  # contador do terceiro laço
                numIngredientes = receita[i].getQuantidadeIngredientes()
                # O se abaixo procura os ingredientes dentro da receita da posição I
                if receita[i].receitaTem(listaIngredientes[j]) == True:
                    contador=contador+1
                j=j+1 #incrementando contador J
            # Esse si verifica se todos a receita I possui todos os ingredientes procurados
            if(contador==totalIngredientes):
                resultado.append(receita[i]) #Caso tenha todos os ingredientes, essa receita é guardada na lista de resultados
            contador=0# o contador é zerado para a proxima comparação
            i=i+1 # incrementa o contador I
        return resultado    

    def temReceitaDe(self,listaIngredientes,receitas):
        resultado  = list() # Onde serão armazenadas as receitas encontradas
        totalIngredientes = len(listaIngredientes) #numero total de ingredientes procurados
        contador=0 #contador de ingredientes encontrados
        i = 0 # contador do primeiro laço
        # Esse laço percorre toda a lista de receitas
        while i < self.totalReceitas:
            j = 0  # contador do segundo laço
            # Esse laço percorr a lista de ingredientes procurados
            while j < totalIngredientes:
                if receita[i].receitaDe(listaIngredientes[j]) == True:
                    contador=contador+1
                j=j+1 #incrementando contador J
            # Esse si verifica se todos a receita I possui todos os ingredientes procurados
            if(contador==totalIngredientes):
                resultado.append(receita[i]) #Caso tenha todos os ingredientes, essa receita é guardada na lista de resultados
            contador=0# o contador é zerado para a proxima comparação
            i=i+1 # incrementa o contador I
        return resultado
          

''' --- [ CARREGAMENTO DO PROGRAMA ] --- '''       
'''
# Abre o banco de dados local e carrega ele em Data
with open('afrodite.json') as f:     
    data = json.load(f)

# Inicializa uma lista
receita = list()

# Esse laço de repetição preenche a lista com Objetos do tipo receita e dados brutos do banco de dados
contador = 0
while contador < 8183:
    data2 = data[contador]['nome']
    data3 = data[contador]['secao']
    receita.append(Receita(data2,data3))                     
    contador = contador + 1
    '''
    

''' --- [ TESTANDO O PROGRAMA ] --- ''' 
'''
#receita[5].ajuste()
#receita[8182].ajuste()

if(receita[5].receitaDe("Geleia")==True):
    print ("Eh receita de GEleia")
else:
    print ("Nao Eh receita de GEleia")

if(receita[5].receitaTem("pimenta")==True):
    print ("A receita tem pimenta")
else:
    print ("A receita nao tem pimenta")                        
                                 

receita[240].imprimirReceita()
'''

'''
consulta = list()
consulta.append("Maria")
consulta.append("mole")

lista = receita[240].temReceitaDe(consulta,receita)

for item in lista:
    print ("Tem receita de : "+item.getNome())

consulta = list()
consulta.append("leite")
consulta.append("gelo")

lista = receita[240].queReceitasPossoFazerCom(consulta,receita)

for item in lista:
    print ("Receita com limao : "+item.getNome())

#receita[5].imprimirNome()
#receita[5].imprimirIngredientes()
#receita[5].imprimirPreparo()

#contador = 0
#while contador < 8150:
#    receita[contador].imprimir()
#    contador = contador + 1
'''




