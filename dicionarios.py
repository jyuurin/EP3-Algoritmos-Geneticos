import csv 

dicionarioItens = dict([])
dicionarioCidades = dict([])
dicionarioViagens = dict([])
dicionarioCidades["Escondidos"] = 0 #Adicionando escondidos pois ele não possui item

#abrindo o csv de itens. percorre e add cada linha no dicionario 
#a chave do dicionario são as cidades. e o valor é o restante da linha.
#preenche o dicionario cidades para que cada uma tenha os itens.
with open("items.csv", "r") as file:
  csvreader = csv.reader(file)
  for i,row in enumerate(csvreader):
    dicionarioItens[i+1] = (row[0], int(row[1]), int(row[2]), int(row[3])) #chave numero, retorna o item
    dicionarioCidades[row[4]] = i+1 #chave cidade, retorna o numero dela
    
#abrindo o csv de cidades
with open("cidades.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    dicionarioViagens[(dicionarioCidades[row[0]], dicionarioCidades[row[1]])] = (int(row[2]), int(row[3])) #id são as viagens (origem e destino), e elas retornam o tempo e o custo.
    dicionarioViagens[(dicionarioCidades[row[1]], dicionarioCidades[row[0]])] = (int(row[2]), int(row[3])) #mesma coisa com origem e destino invertido.


# print(dicionarioItens[dicionarioCidades["Limões"]])
# print(dicionarioCidades["Limões"])
# print(dicionarioViagens[(dicionarioCidades["Limões"], dicionarioCidades["Campos"])])
# print(dicionarioViagens[(1,2)])