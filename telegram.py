import telepot
import json
import re
from bdreceitas import Receita

class Pessoa:
    def __init__(self):
        self.nome="amg"
        
    def getId(self):
        return self.id

    def setSexo(self,sexo):
        self.sexo=sexo
    
    def getSexo(self):
        return self.sexo

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
pattern = re.compile("x")
print (pattern.search("dog"))

    
bot = telepot.Bot("COLOQUEAQUISEUCÓDIGODOBOTFATHER")

falouOI = ("Nao")
roteiro = 0 #Seguindo um roteiro para consultar uma receita
numeroAleatorio = 0 #Numero usado para sortear uma receita
receitasDe = list() #Guarda lista de receitas consultadas por titulo
receitasCom = list() #Guarda lista de receitas consultadas por ingredientes
pessoa = Pessoa()


def verificaRoteiro(msg,data):
    global roteiro
    

        

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
    listaOI= ("OI","Oi","oi","ola","Ola","Olá","Hi","hi","Hey","hey","Ei","ei","Eai","eai","Eae","eae")
    listaTCHAU = ("Tchau","tchau","Xau","xau","Fui","fui","Zarpei","zarpei")
    listaNOME = ("Palmirinha","palmirinha","amiguinha","vó")
    listaDESCULPA = ("desculpa","desculpe","sorry","desculpe-me")
    
    global falouOI
    global roteiro
    global numeroAleatorio
    global receitasDe
    global receitasCom

    if roteiro == 0:
        for item in listaOI:
            if re.search(mensagem, item, re.IGNORECASE):
                bot.sendMessage(data['id'],"Oi Amiguinho, tudo bem?")          
                falouOI=("Sim")
                #bot.sendMessage(data['id'],falouOI) # Ta aqui por teste
                bot.sendMessage(data['id'],"A vovo nao ta com as vistas boas...")
                bot.sendMessage(data['id'],"Voce eh amiguinho ou amiguinha?")
                roteiro=1
                return True
        for item in listaDESCULPA:
            if re.search(mensagem, item, re.IGNORECASE):
                bot.sendMessage(data['id'],"Aceito suas desculpas..Rum!")
                bot.sendMessage(data['id'],"Agora da um oi pra vovo...")
                #falouOI=("Nao")
                #bot.sendMessage(data['id'],falouOI)
                return True
        bot.sendMessage(data['id'],"Toda boa conversa, se inicia com uma saudacao!")
        bot.sendMessage(data['id'],"A vovo nao conversa com gente mau educada...")
        bot.sendMessage(data['id'],"RUM!!!")
        return False
        
    if roteiro == 1:
        listaSEXO = ("Amiguinho","amiguinho","Amiguinha","amiguinha")
        for item in listaSEXO:
            if re.search(mensagem, item, re.IGNORECASE):
                pessoa.setSexo(mensagem)
                bot.sendMessage(data['id'],"Bom saber, "+pessoa.getSexo()+"!")          
                #bot.sendMessage(data['id'],falouOI) # Ta aqui por teste
                bot.sendMessage(data['id'],pessoa.getSexo()+" a vovo conhece varias receitas...") 
                bot.sendMessage(data['id']," e ficaria muito feliz em te ensinar algumas ou sugerir alguma receita com os ingredientes que voce tiver.")
                bot.sendMessage(data['id'],pessoa.getSexo()+" pra saber como me perguntar, basta digitar 'como?'") 
                roteiro=2
                return True

    if roteiro == 2:
        ''' EM ROTEIRO 2 SÃO DEFINIDO OS COMANDOS QUE FAZEM CONSULTA DE RECEITAS '''
        
        if re.search(mensagem, "como?", re.IGNORECASE):
            #Colocar aqui a vovo pra falar as instruções
            bot.sendMessage(data['id'],"Agora só digitar os comandos, ta "+pessoa.getSexo()+"?!")

        # Palmirinha indica uma receita aleatoria
        elif re.search(mensagem, "me indica uma receita", re.IGNORECASE):
            bot.sendMessage(data['id'],"Vou pensar em uma aqui "+pessoa.getSexo()+"...")
            numeroAleatorio = 5; # TRocar essa linha por uma funcao de numeros aleatorios
            bot.sendMessage(data['id'],"O que acha de aprender "+receita[numeroAleatorio].getNome()+" ein "+pessoa.getSexo()+"?")
            bot.sendMessage(data['id'],"Me diz... sim ou nao?"+pessoa.getSexo())
            roteiro = 3 # Roteiro 3 e 4 sao destinados a receita aleatoria 

        # Pergunta a palmitinha se ela tem receitas de X
        elif re.search(mensagem, "tem receita de", re.IGNORECASE):
            bot.sendMessage(data['id'],"Deixa eu ver aqui "+pessoa.getSexo()+"...")
            '''
            Fazer funcao que consiga receber o nome da receita a ser consultada
            receitasDe = receita[0].temReceitaDe(VARIAVELAQUI,receita)
            '''
            bot.sendMessage(data['id'],"Tem essas "+pessoa.getSexo()+", digite um numero pra saber sobre a receita escolhida ou digite nao.")
            bot.sendMessage(data['id'],"Ta bom "+pessoa.getSexo()+"!?")
            roteiro = 5 # Roteiro 5 e 6 sao destinados a lista de receitas buscadas por titulo

        # Pergunta a palmitinha se ela tem receitas com N ingredientes
        elif re.search(mensagem, "tem receita com", re.IGNORECASE):
            bot.sendMessage(data['id'],"Deixa eu ver aqui "+pessoa.getSexo()+"...")
            '''
            Fazer funcao que consiga receber o nome dos ingredientes a serem consultados
            receitasCom = receita[0].queReceitasPossoFazerCom(VARIAVELAQUI,receita)
            '''
            bot.sendMessage(data['id'],"Tem essas "+pessoa.getSexo()+", digite um numero pra saber sobre a receita escolhida ou digite nao.")
            bot.sendMessage(data['id'],"Ta bom "+pessoa.getSexo()+"!?")
            roteiro = 7 # Roteiro 7 e 8 sao destinados a lista de receitas buscadas por conteudo 

    if roteito == 3:
        if re.search(mensagem, "sim", re.IGNORECASE):
            #Colocar aqui a vovo pra falar as instruções
            bot.sendMessage(data['id'],"Otimo "+pessoa.getSexo()+"!")
            bot.sendMessage(data['id'],"Pra fazer "+receita[numeroAleatorio].getNome()+" basta ter o seguinte:")
            listaIngrediente = receita[numeroAleatorio].getIngredientes()
            for item in listaIngrediente:
                bot.sendMessage(data['id'],item)

            if receita[numeroAleatorio].temModoPreparo() == True :
                bot.sendMessage(data['id'],pessoa.getSexo()+" e pra preparar essa receita, basta...")
                listaPreparo = receita[numeroAleatorio].getPreparo()
                for item in listaPreparo:
                    bot.sendMessage(data['id'],item)

                
            bot.sendMessage(data['id'],"Legal neh "+pessoa.getSexo()+", se quiser aprender mais eh so pedir!")
            roteiro=2

        elif re.search(mensagem, "nao", re.IGNORECASE):
            bot.sendMessage(data['id'],"Ta bom "+pessoa.getSexo()+", se quiser que a vovo indique novamente, basta pedir de novo ta?!")
            roteiro = 2

    
    for item in listaTCHAU:
        if re.search(mensagem, item, re.IGNORECASE):
            if roteiro < 2:
                bot.sendMessage(data['id'],"Tchau...")
            else:
                bot.sendMessage(data['id'],"Tchau "+pessoa.getSexo()+" :*")

            roteiro = 0
            #bot.sendMessage(data['id'],falouOI)  # Ta aqui por teste
            return True
    for item in listaNOME:
        if re.search(mensagem, item, re.IGNORECASE):
            bot.sendMessage(data['id'],"Oi eu, to aqui amiguinho!")
            falouOI=("Nao")
            bot.sendMessage(data['id'],falouOI)
            return True
    
    bot.sendMessage(data['id'],"Amiguinho, eu não entendi!")
    return False


def recebendoMensagem(msg):
    data = msg['from']
    
    
    analizaMensagem(msg['text'],data)
    
    print (data['username']+str(data['id'])+" enviou: "+msg['text'])

    '''if pessoaExiste(data['id']) == True:
        analizaMensagem(msg['text'],pessoaPos(data['id']))
    else:
        pessoas.append(Pessoa(data['username'],data['id']))
        analizaMensagem(msg['text'],pessoaPos(data['id']))'''



bot.message_loop(recebendoMensagem)

while True:
    pass
