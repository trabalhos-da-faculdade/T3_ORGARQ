
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

# Counter to position
count = 0

# Counter to change the value from position
countToChange = 0


# Cada posicao do cache possui a inicializacao da classe Linha
for x in range (0,16):
    cache[x] = Linha()

for line in f:

    tag = line[0:13]
    palavra = line[13:15]
    byte = line[15:16]
    
    if memory[count] == None :
        memory[count] = tag
        print("Miss: " + str(int(line,2)))
        miss = miss + 1
        count = count + 1
    else if memory[count] == tag :
        print("Hit: " + str(int(line,2)))
        hit = hit + 1
        count = count + 1
    else if 
    
    



# print("Hits: " + str(hit))
# print("Misses: " + str(miss)) 
# print("Taxa de hits: " + str(round((float(hit) / (hit+miss))*10000) / 100) + "%")
# print("Taxa de misses: " + str(round((float(miss) / (hit+miss))*10000) / 100) + "%")

for i in range(0,263):
    print(memory[i])