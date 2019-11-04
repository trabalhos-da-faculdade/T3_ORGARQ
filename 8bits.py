# -------------------------------
# FORMATAR OS BINARIOS EM 8 BITS
# -------------------------------


f = open("hextobin.txt","r") # lendo o arquivo hextobin

for line in f:
    if(line != "\n"): # se n tiver espacos
        val = line.zfill(17) # adiciona os zeros faltantes
        val = val.strip() # retira os espacos entre os valores
        print(val) # imprime o binario em 8 bit