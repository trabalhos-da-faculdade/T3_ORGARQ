
class Linha:
    palavras = ['00','01','10','11']
    byte = 0
    tag = ""

# Reading file
f = open("binary.txt","r")



cache = [None] * 16
memory = [None] * 264

# Variaveis hit e miss 
hit = 0
miss = 0

# Counter
count = 0

# Cada posicao do cache possui a inicializacao da classe Linha
for x in range (0,16):
    cache[x] = Linha()

for line in f:

    tag = line[0:13]
    palavra = line[13:15]
    byte = line[15:16]

  # TODO put tag on memory



# print("Hits: " + str(hit))
# print("Misses: " + str(miss)) 
# print("Taxa de hits: " + str(round((float(hit) / (hit+miss))*10000) / 100) + "%")
# print("Taxa de misses: " + str(round((float(miss) / (hit+miss))*10000) / 100) + "%")

for i in range(0,263):
    print(memory[i])