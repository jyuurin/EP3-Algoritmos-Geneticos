import random
from dicionarios import dicionarioCidades, dicionarioItens, dicionarioViagens

def fitness(individuo):
  tempo = 0
  peso = 0
  lucro = 0
  tempoViagem = 0
  tempoRoubo = 0
  despesa = 0
  faturamento = 0
  #salva o valor inicial como escondidos
  origem = dicionarioCidades["Escondidos"]

  if len(individuo) < 2:
    return -1

  if len(individuo) != len(set(individuo)):
    return -1
  # https://www.trainingint.com/how-to-find-duplicates-in-a-python-list.html
  
  for destino in individuo:
    #Pega informação das viagens, dos itens, valores e peso
    viagem = dicionarioViagens[(origem,destino)] 
    item = dicionarioItens[destino] 
    tempoViagem += viagem[0]
    tempoRoubo += item[2]
    peso += item[1]
    despesa += viagem[1]
    faturamento += item[3]
    #origem passa a ser o lugar atual
    origem = destino

  viagem = dicionarioViagens[(origem, dicionarioCidades["Escondidos"])]
  tempoViagem += viagem[0]
  despesa += viagem[1]

  tempo = tempoViagem + tempoRoubo
  lucro = faturamento - despesa

  ##print(tempoViagem, tempoRoubo, despesa, faturamento)  

  if tempo > 72:
    return -1

  if peso > 20:
    return -1

  return lucro

def gerarIndividuoAleatorio():
  individuo = []
  cidades = list(range(1,14))
  individuo = random.sample(cidades, 6)

  return individuo

#primeira mutaçao: adicionar nova cidade aleatoria
def mutacaoA(individuo):  
  novoIndividuo = list(individuo)
  cidades = list(range(1,14))
  novoIndividuo.append(random.choice(cidades))

  return novoIndividuo
  
#segunda mutação: trocar cidades de lugar
def mutacaoB(individuo):
  novoIndividuo = individuo.copy()
  posicoesSorteadas = random.sample(list(range(len(novoIndividuo))), 2)

  novoIndividuo[posicoesSorteadas[0]] = individuo[posicoesSorteadas[1]]
  novoIndividuo[posicoesSorteadas[1]] = individuo[posicoesSorteadas[0]]
  
  return novoIndividuo

#terceira mutação: remover cidades
def mutacaoC(individuo):  
  novoIndividuo = individuo.copy()
  novoIndividuo.pop(random.choice(range(len(novoIndividuo))))

  return novoIndividuo 

#quarta mutação: inverter a ordem das cidades
def mutacaoD(individuo):
  novoIndividuo = individuo.copy()
  novoIndividuo.reverse()

  return novoIndividuo

def crossover(individuo1, individuo2):
  metadeIndividuo1 = len(individuo1) // 2
  metadeIndividuo2 = len(individuo2) // 2
  
  novoIndividuo1 = individuo1[:metadeIndividuo1] + individuo2[metadeIndividuo2:] 
  novoIndividuo2 = individuo2[:metadeIndividuo2] + individuo1[metadeIndividuo1:]

  return [novoIndividuo1, novoIndividuo2]