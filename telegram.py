import telepot
import json
from bdreceitas import Receita

class Pessoa:
    def __init__(self, nome,id):
        self.nome=nome
        self.id=nome

    def setFriend(self, friend):
        self.friend

    def getId(self):
        return self.id




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
    
bot = telepot.Bot("ID-DO-SEU-BOT-AQUI")


pessoas = list()

def pessoaExiste(id):
    for item in pessoas:
        if item.getId() == id:
            return True
    return False

def pessoaPos(id):
    contador = 0
    while contador < len(pessoas):
        if pessoas[contador].getId == id:
            return contador
        contador=contador+1

def analizaMensagem(mensagem,data):
    if mensagem == "qual meu id?":
        bot.sendMessage(data['id'],"Amiguinho, seu id eh "+str(data['id']))
    else:
        lista = list()
        lista.append(mensagem)
        lista2 = receita[0].temReceitaDe(lista,receita)
        bot.sendMessage(data['id'],lista2)

def recebendoMensagem(msg):
    data = msg['from']
    
    
    analizaMensagem(msg['text'],data)
    
    print (data['username']+" enviou: "+msg['text'])
    bot.sendMessage(data['id'],"Bla bla bla")

    '''if pessoaExiste(data['id']) == True:
        analizaMensagem(msg['text'],pessoaPos(data['id']))
    else:
        pessoas.append(Pessoa(data['username'],data['id']))
        analizaMensagem(msg['text'],pessoaPos(data['id']))'''

  

bot.message_loop(recebendoMensagem)

while True:
    pass
