# --------------------------------
# TESTE DE HIT OU MISS DA CACHE 1
# --------------------------------

class Linha:
    palavras = ['000','001','010','011','100','101','110','111']
    byte = 0
    tag = ""
    linha = ""

f = open("binary.txt","r")

cache = [None] * 16

hit = 0
miss = 0

for x in range (0,16):
    cache[x] = Linha()

for line in f:

    tag = line[0:8]
    linha = line[8:12]
    dec = int(linha,2)
    palavra = line[12:15]
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
