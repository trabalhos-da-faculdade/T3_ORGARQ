# Linha class to record info
class Linha:
    palavras = ['00','01','10','11']
    byte = 0
    tag = ""
    palavra = ""
    count = -1 # counter to change postiion

# Reading file
f = open("binary.txt","r")

cache = [None] * 16

# Variaveis hit e miss 
hit = 0
miss = 0

# Start cache
for x in range(0,16):
    cache[x] = Linha()

# Counter to walk on the Cache 
cacheCount = 0 

# to check if cache memory is full
isFull = 16

# to insert the min value of count inside Linha
minValue = -1
# Reading the binary file

for line in f:

    tag = line[0:13]
    palavra = line[14:16]
    byte = line[15:16]
    print("tag: " + tag),
    print("palavras: " + palavra),
    print("byte: " + byte)

    if cache[cacheCount].tag == "":
        cache[cacheCount].palavra = line
        cache[cacheCount].tag = tag
        print("Miss;" + str(cache[cacheCount].palavra))
        miss = miss + 1
        cacheCount = cacheCount + 1
    else:
        if cacheCount == isFull:
                cacheCount = 0
        
        else:
            if cache[cacheCount].palavra == tag:
                print("Hit;" + str(cache[cacheCount].palavra))
                hit = hit + 1
                cache[cacheCount].count = cache[cacheCount].count + 1
                if minValue > cache[cacheCount].count:
                    minValue = cache[cacheCount].count
                    cacheCount = cacheCount + 1
                
            else:
                if cache[cacheCount].count < minValue and cache[cacheCount] != None:
                    cache[cacheCount].tag = tag
                    cache[cacheCount].palavra = palavra
                    cache[cache].count  = -1
                    print("Miss;" + str(cache[cacheCount].palavra))
                    miss = miss + 1
# TODO make this array start again



print("Hits;" + str(hit))
print("Misses;" + str(miss)) 
print("Taxa de hits;" + str(round((float(hit) / (hit+miss))*10000) / 100) + "%")
print("Taxa de misses;" + str(round((float(miss) / (hit+miss))*10000) / 100) + "%")
