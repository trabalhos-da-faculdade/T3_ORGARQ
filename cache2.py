# -------------------------------
# TESTE DE HIT OU MISS DA CACHE 2
# -------------------------------


class Linha:
    palavras = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    byte = 0
    tag = ""
    linha = ""


# Lendo o Arquivo onde estao os 8 Bits
f = open("binary.txt","r")

cache = [None] * 16

hit = 0
miss = 0

for x in range (0,16):
    cache[x] = Linha()

for line in f:

    tag = line[0:9]
    linha = line[9:13]
    dec = int(linha,2)
    palavra = line[13:14]
    byte = line[14:15]

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

