
# Como funciona a Memória Associativa

* Passos de como fazer o acesso á memória associativa

1. Extrair a Tag do endereço requisitado
2. Se Tag está na memória associativa
    1. (HIT) Acessar memória cache com o índice fornecido pela memória associativa
    2. Ir para o Passo 7
3. Se Tag não estiver, deu MISS
4. Se não existir posição livre na cache
    1. Escolher endereço para substituir de acordo com a politica escolhida(nosso caso o contador)
5. Buscar dado no nível inferior
6. Cadastrar posição na memória associativa para pesquisas futuras
7. Efetuar Leitura
8. Fim
