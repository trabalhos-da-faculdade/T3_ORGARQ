# TRABALHO 3 DE ORGARQ

![GitHub last commit](https://img.shields.io/github/last-commit/trabalhos-da-faculdade/T3_ORGARQ) ![GitHub language count](https://img.shields.io/github/languages/count/trabalhos-da-faculdade/T3_ORGARQ) ![GitHub top language](https://img.shields.io/github/languages/top/trabalhos-da-faculdade/T3_ORGARQ)

### Como funciona este Repositorio

* Para testar as _caches_ , utilize o script `compile.sh`
* Se ele nao estiver compilavel use os seguintes comandos:

```bash
# Para transformar em executavel
chmod +x compile.sh

# Para rodar o programa
./compile.sh
```

* Para testar de novo, delete os .txt com o Script `clear.sh`
* Se ele nao estiver compilavel use os seguintes comandos

```bash
# Para transformar em executavel
chmod +x clear.sh

# Para rodar o programa
./clear.sh
```

#### Usando o script Compile

1. O script vai pegar o .txt com os hexadecimais e transformar em binario com o programa _hexToBin.py_ e salvar o resultado no `hextobin.txt`
2. Depois ele vai pegar o arquivo `hextobin.txt` e usar o programa _8bits.py_ para completar as lacunas faltantes para o valor ficar em 8 Bits e salva no arquivo `binary.txt`.
3. Depois o usuario deve selecionar qual cache deseja testar(1 ou 2) e ele vai guardar os valores de Hit ou Miss com a percentagem em um arquivo com o nome do cache testado(cache1.txt ou cache2.txt).
