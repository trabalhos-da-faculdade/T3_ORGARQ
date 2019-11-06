# --------------------------------
# TESTE DE HIT OU MISS DA CACHE 1
# --------------------------------

# Exercicio 1
#   Mapeamento Direto
#       10 Bits para tag
#       3  Bits para linha
#       2  Bits para palavra
#       1  Bit para selecao do byte em uma palavra
#   Cache com 8 Linhas
#   4 Palavras por Linha




# Criado uma class que sera usado para o teste
class Linha:
    palavras = ['0000','0001','0010','0011','0100','0101','0110','0111']
    byte = 0
    tag = ""
    linha = ""

# Lendo o Arquivo onde estao os 8 Bits
f = open("binary.txt","r")

# Inicialicao do array do Cache
cache = [None] * 16

# Variaveis hit e miss 
hit = 0
miss = 0

# Cada posicao do cache possui a inicializacao da classe Linha
for x in range (0,16):
    cache[x] = Linha()

# Lendo cada valor de cada linha do arquivo
for line in f:

    tag = line[0:10]
    linha = line[11:14]
    dec = int(linha,2)
    palavra = line[14:16]
    byte = line[15:16]

    if cache[dec].byte == 0 :
        print("Miss: " + str(int(line,2)))
        miss = miss + 1
        cache[dec].byte = 1
        cache[dec].linha = linha
        cache[dec].tag = tag
    else:
        if cache[dec].tag != tag :
            print("Miss: " + str(int(line,2)))
            miss = miss + 1
            cache[dec].tag = tag
        else:
            print("Hit: " + str(int(line,2)))
            hit = hit + 1

print("Hits: " + str(hit))
print("Misses: " + str(miss)) 
print("Taxa de hits: " + str(round((float(hit) / (hit+miss))*10000) / 100) + "%")
print("Taxa de misses: " + str(round((float(miss) / (hit+miss))*10000) / 100) + "%")

for i in range(0,16):
    print(cache[i].linha)