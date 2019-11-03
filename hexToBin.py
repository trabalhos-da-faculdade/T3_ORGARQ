import binascii
f = open("numbers.txt","r")

for line in f:
    separado = line.split(",")
    for num in separado:
        if(num != "\n"):
            semEspaco = num.strip()
            decimal = int(semEspaco, 16)
            print(bin(decimal))