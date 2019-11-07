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
    palavra = line[13:15]
    byte = line[15]
    #print("tag: " + tag),
    #print("palavras: " + palavra),
    #print("byte: " + byte)

    if cacheCount != isFull:
        cache[cacheCount].palavra = line
        cache[cacheCount].tag = tag
        print("Miss;" + str(cache[cacheCount].palavra))
        miss += 1
        cacheCount += 1
    else:
        if cacheCount == isFull:
            cacheCount = 0
            if cache[cacheCount].tag == tag:
                print("Hit;" + str(cache[cacheCount].palavra))
                print("Hit Counter: " + str(cache[cacheCount].count))
                hit += 1
                cache[cacheCount].count += 1
            if minValue > cache[cacheCount].count:
                minValue = cache[cacheCount].count
                cacheCount += 1
                
            if cache[cacheCount].count < minValue:
                cache[cacheCount].tag = tag
                cache[cacheCount].palavra = palavra
                cache[cache].count  = -1
                print("Miss;" + str(cache[cacheCount].palavra))
                miss += 1



print("Hits;" + str(hit))
print("Misses;" + str(miss)) 
print("Taxa de hits;" + str(round((float(hit) / (hit+miss))*10000) / 100) + "%")
print("Taxa de misses;" + str(round((float(miss) / (hit+miss))*10000) / 100) + "%")
