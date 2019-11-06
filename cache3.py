
class Linha:
    palavras = ['00','01','10','11']
    byte = 0
    tag = ""

class CounterTag:
    tag = ""
    counter = -1

# Reading file
f = open("binary.txt","r")



cache = [None] * 16
memory = [None] * 16
testing = [None] * 16

# Variaveis hit e miss 
hit = 0
miss = 0

# Counter to position
count = 0

# Counter to change the value from position
countToChange = 0

# Bigger value to change
minValue = 1000000


# Cada posicao do cache possui a inicializacao da classe Linha
for x in range (0,16):
    cache[x] = Linha()

for y in range (len(memory)):
    testing[y] = CounterTag()

for line in f:

    tag = line[0:13]
    palavra = line[13:15]
    byte = line[15:16]
    
    if memory[count] == None :
        memory[count] = tag
        print("Miss: " + str(int(line,2)))
        miss = miss + 1
        testing[count].tag = tag
        count = count + 1
    else:
        if memory[count] == tag :
            print("Hit: " + str(int(line,2)))
            hit = hit + 1
            count = count + 1

            for i in range(len(testing)):
                if testing[i].tag == tag:
                    testing[i].counter = testing[i].counter + 1
                    if testing[i].counter < minValue:
                        minValue = testing[i].counter

        else:
            if count == len(memory):
                for i in range(len(testing)):
                    if testing[i].counter == minValue:
                        print("Miss: " + str(int(line,2)))
                        testing[i].tag = tag


print("Hits: " + str(hit))
print("Misses: " + str(miss)) 
print("Taxa de hits: " + str(round((float(hit) / (hit+miss))*10000) / 100) + "%")
print("Taxa de misses: " + str(round((float(miss) / (hit+miss))*10000) / 100) + "%")
