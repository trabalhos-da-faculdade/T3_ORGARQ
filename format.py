f = open("binary.txt","r")

for line in f:
    if(line != "\n"):
        val = line.zfill(17)
        print(val)