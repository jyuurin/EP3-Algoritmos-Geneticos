# import csv
import genetica
import random

tamanhoPopulacao = 10
quantidadeGeracao = 100
populacao = []

for numero in range(tamanhoPopulacao):
  populacao.append(genetica.gerarIndividuoAleatorio())
  
for geracao in range(quantidadeGeracao):
  for numero in range(tamanhoPopulacao):
    mutacaoSorteada = random.choice([1, 2, 3, 4])
    match mutacaoSorteada:
        case 1:
          populacao.append(genetica.mutacaoA(populacao[numero]))
        case 2:
          populacao.append(genetica.mutacaoB(populacao[numero]))
        case 3:
          populacao.append(genetica.mutacaoC(populacao[numero]))
        case 4:
          populacao.append(genetica.mutacaoD(populacao[numero]))

  
  crossover = genetica.crossover(random.choice(populacao), random.choice(populacao))

  populacao.append(crossover[0])
  populacao.append(crossover[1])
  
  populacao = sorted(populacao, key=genetica.fitness, reverse = True)
  
  populacao = populacao[0 : len(populacao) - 12]
  
for individuo in populacao:
  print(individuo, genetica.fitness(individuo))
print(len(populacao))


