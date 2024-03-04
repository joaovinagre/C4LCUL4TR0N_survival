
import random
import os

#Essa poha ainda nao testa raiz
#Adicionar documento com histórico 
player = ""
streak = True
pontos = 0
Intro = ' ******** Bem-vindo ao desafio de C4LCUL4TR0N ******** \n O único jeito de conseguir chegar ao final do labirinto é respondendo corretamente à pelo menos 6 perguntas.\n Arredonde para duas casas decimais. \n Use ponto como vírgula. \n Ao responder "um", use 1.0. \n Insira seu nome e pressione "ENTER" para iniciar o desafio. \n'
respostas = []
gabarito = [] 
op = ['+','-','*','/', '**', '**']


def compararrespostas(lista1, lista2):
    if lista1 == lista2:
        global pontos
        pontos += 1
    else:
        global streak
        streak = False

def criarquestao(operação):
    ask = ' ?'
    space = ' '
    a, b, c = random.randint(0,100), random.randint(1,100), random.randint(0,len(operação)-1)
    if c == 4 or c == 5 :
        a, b = a/10, b-50 
        b = b/12
        b = round(b,0)
    questao = str(a) + space + operação[c] + space + str(b) + ask     #criando a questão
    buffer = eval(f"{a} {operação[c]} {b}")        
    buffer = round(buffer,2)
    gabarito.append(str(buffer))
    return print(questao)


### start:


player = input(Intro)

while streak:
    criarquestao(op)
    r = input()
    respostas.append(r)
    compararrespostas(respostas, gabarito)

if pontos <= 6:
    print(f" Você sobreviveu por {pontos} rodadas. \n Mais sorte na próxima {player}.")
else:
    print(f" Parabéns {player}, você venceu {pontos} rodadas!!")