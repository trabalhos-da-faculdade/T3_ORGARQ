#!/bin/bash

# --------------------------------
# COMPILADOR DO PROGRAMA NO LINUX
# --------------------------------

# Primeiro: Transformamos os Hexa em Binario
python hexToBin.py >> hextobin.txt

# Segundo: Pegamos os binarios e colocamos em 8 bits 
python 8bits.py >> binary.txt

# Verificamos qual cache queremos testar
echo "Qual cache deseja testar: [1 ou 2] ";
read number;

# Rodar a cache desejada e salvar a saida em um arquivo
python cache${number}.py >> cache${number}.csv

