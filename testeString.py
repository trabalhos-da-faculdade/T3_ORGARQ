class Linha:
    palavras = ['000','001','010','011']
    byte = 0
    tag = ""
    #linha = ""

f = open("binary.txt", "r")

cache = [None] * 16

for x in range(0,16):
     cache[x] = Linha()

for line in f:
    tag = line[0:13]
    #linha = line[13:15]
    #dec = int(linha,2)
    palavra = line[13:15]
    byte = line[15:16]

    print(tag)
    #print(linha)
    print(palavra)
    print(byte)
