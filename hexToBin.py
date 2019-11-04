# ------------------------------------------------
# TRANSFORMAR OS VALORES HEXADECIMAIS EM BINARIOS
# ------------------------------------------------

import binascii

f = open("hex.txt","r") # Lendo o arquivo com os HEXADECIMAIS

for line in f:
    separado = line.split(",")
    for num in separado:
        if(num != "\n"):
            semEspaco = num.strip()
            decimal = int(semEspaco, 16)
            binario = bin(decimal).split("0b")
            print(binario[1])
            