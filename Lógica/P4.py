#For laço de repetição
#Função range para imprimir os números inteiros de 1 a 10

#For - para
for numero in range(1, 11):
    
    print(numero)
    

#for - utilizando números

for i in range(10, 0, -1):
    
    print(i)
    

#for - utilizando números

#De 1 a 10 com um passo de 2.

#Começa em 2, termina antes de 12, com um passo de 2
for i in range(2, 12, 2):
    
    print(i)
# Inicializando a variável para armazenar a soma
soma = 0

# Iterando de 1 a 10, de 2 em 2 (capturando apenas os números ímpares)
for i in range(1, 11, 2):
    
    print(f"Número ímpar atual: {i}")
    
    #soma = soma + i
    soma += i  # Adicionando o número ímpar atual à soma

print(f"\nA soma dos números ímpares de 1 a 10 é: {soma}")
    

"""
Exercício: Multiplicação de Números

Objetivo: Escreva um programa que utilize um loop for para multiplicar os 
números de 1 a 5 e imprima o resultado de cada etapa e o resultado final.

Etapas:

    - Utilize um loop for para iterar pelos números de 1 a 5.
    - Multiplique cada número pelo resultado anterior (começando por 1).
    - Imprima o resultado de cada etapa.
    - Imprima o resultado final da multiplicação de todos os números.

Saída:

Multiplicando por 1, o resultado parcial é 1
Multiplicando por 2, o resultado parcial é 2
Multiplicando por 3, o resultado parcial é 6
Multiplicando por 4, o resultado parcial é 24
Multiplicando por 5, o resultado parcial é 120
"""

# Inicializando a variável resultado com 1
resultado = 1

# Utilizando um loop for para iterar pelos números de 1 a 5
for numero in range(1, 6):
    
    # Multiplicando o resultado pelo número atual
    #resultado = resultado * numero
    resultado *= numero 
    
    print(f"Multiplicando por {numero}, o resultado parcial é {resultado}")

print(f"O resultado final da multiplicação de 1 a 5 é: {resultado}")

"""
Exercício: Soma de Números Pares

Objetivo: Escreva um programa que peça ao usuário um número 
inteiro N e some todos os números pares de 1 até N, incluindo o próprio N (se for par). 

Utilize um loop for para esta tarefa.

Etapas:

    - Solicite ao usuário um número inteiro positivo N.
    - Utilize um loop for para iterar de 1 a N e some todos os números pares.
    - Imprima o resultado da soma.


Exemplo de Saída:

Digite um número inteiro positivo: 10
A soma dos números pares de 1 até 10 é: 30
"""

# Solicitando ao usuário o número
N = int(input("Digite um número inteiro positivo: "))

# Inicializando a variável para armazenar a soma
soma_pares = 0

# Utilizando um loop for para somar os números pares de 1 até N
for i in range(1, N + 1):
    
    # Verificando se o número é par
    if i % 2 == 0: 
        
        #Imprime cada etapa
        print(f"Número: {i} + {soma_pares} = {i+soma_pares}")
        
        soma_pares += i
        
        

# Imprimindo o resultado
print(f"A soma dos números pares de 1 até {N} é: {soma_pares}")

"""
Exercício: Tabela de Multiplicação

Objetivo: Escreva um programa que peça ao usuário um número inteiro positivo NN e 
exiba a tabela de multiplicação para esse número, de 1 a 10. Utilize um loop for para esta tarefa.

Etapas:

    - Solicite ao usuário um número inteiro positivo NN.
    - Utilize um loop for para iterar de 1 a 10.
    - Para cada iteração, multiplique o número NN pelo valor da iteração e imprima o resultado.
    
Exemplo de Saída:

Digite um número inteiro positivo para exibir a sua tabela de multiplicação: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Fim da tabela de multiplicação.

"""

# Solicitando ao usuário o número para criar a tabela de multiplicação
N = int(input("Digite um número inteiro positivo para exibir a sua tabela de multiplicação: "))

# Utilizando um loop for para criar a tabela de multiplicação de 1 a 10
for i in range(1, 11):
    
    resultado = N * i # Calculando o resultado da multiplicação
    
    print(f"{N} x {i} = {resultado}") # Imprimindo o resultado

# Imprimindo uma linha final
print("Fim da tabela de multiplicação.")


"""
Exercício: Soma dos Quadrados

Objetivo: Escreva um programa que peça ao usuário um número inteiro positivo NN e 
calcule a soma dos quadrados de todos os números inteiros de 1 até NN. Utilize um loop 
for para esta tarefa.

Etapas:

    - Solicite ao usuário um número inteiro positivo NN.
    
    - Utilize um loop for para iterar de 1 a NN, calculando o quadrado 
    de cada número e somando-o a uma variável.
    
    - Imprima o resultado da soma.

Exemplo de Saída:

Digite um número inteiro positivo: 5
Quadrado de 1: 1
Quadrado de 2: 4
Quadrado de 3: 9
Quadrado de 4: 16
Quadrado de 5: 25
A soma dos quadrados dos números de 1 até 5 é: 55


"""

# Solicitando ao usuário o número
N = int(input("Digite um número inteiro positivo: "))

# Inicializando a variável para armazenar a soma dos quadrados
soma_quadrados = 0

# Utilizando um loop for para somar os quadrados de 1 até N
for i in range(1, N + 1):
    quadrado = i**2 # Calculando o quadrado do número
    print(f"Quadrado de {i}: {quadrado}") # Imprimindo o quadrado do número
    soma_quadrados += quadrado # Adicionando o quadrado à soma

# Imprimindo o resultado
print(f"A soma dos quadrados dos números de 1 até {N} é: {soma_quadrados}")

#For - Utilizando Strings
#loop for para iterar sobre uma lista de caracteres alfabéticos, 
#imprimindo cada item da lista até encontrar o caractere "C"

#For = Para

lista = ["A", "B", "C", "D", "E"]

for item in lista:
    
    print(item)
    
    if item == "C":
        
        break
        



#For - Utilizando Strings

#For = Para

# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    
    print(fruta)

numero = int(input("Digite um número: "))

for i in range(1, numero + 1):
    
    print(i)


#For Utilizando If e Else
#Verifica se é par ou ímpar e imprime uma mensagem correspondente. 
    
# Iterando sobre uma lista de números e aplicando uma condição
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicia um loop 'for' para iterar através de cada número na lista 'numeros'
for numero in numeros:
    
    # Verifica se o número atual é par usando o operador de módulo (%), que retorna o resto da divisão por 2
    if numero % 2 == 0:
        
        # Se o número for par, imprime a mensagem indicando que o número é par
        print(numero, "é par")
        
    else:
        
        # Se o número não for par (ou seja, ímpar), imprime a mensagem indicando que o número é ímpar
        print(numero, "é ímpar")

        
        
print()

"""
Exercício: Lista de Compras

Objetivo: Use um loop for para iterar sobre uma lista de itens de 
compras e imprimir cada item em um formato específico.

Instruções:

    1. Crie uma lista chamada itens_compra contendo alguns itens que 
    você compraria em uma loja, por exemplo: ["maçã", "banana", "cenoura", "leite"].
    
    2. Use um loop for para iterar sobre os itens da lista.
    3. Para cada item na lista, imprima o item no seguinte formato: "Eu preciso comprar [item]".

Após concluir o exercício, sua saída deve se parecer com:

Eu preciso comprar maçã
Eu preciso comprar banana
Eu preciso comprar cenoura
Eu preciso comprar leite

"""

# Criando uma lista chamada 'itens_compra' contendo quatro itens (strings).
itens_compra = ["maçã", "banana", "cenoura", "leite"]

# Iniciando um loop 'for' que irá iterar sobre cada 'item' na lista 'itens_compra'.
for item in itens_compra:
    
    # Imprimindo uma frase com o item atual da iteração.
    # A função 'print' automaticamente insere um espaço entre os argumentos.
    print("Eu preciso comprar", item)



"""
Exercício: Estrelas Descendentes

Objetivo: Use um loop for para criar um padrão descendente 
de estrelas (*). Comece com 5 estrelas na primeira linha e reduza 
uma estrela em cada linha subsequente até não restar nenhuma estrela.

Instruções:

    1. Use um loop for para iterar de 5 a 0 (dica: pense sobre 
    a função range() de maneira descendente).
    
    2. Em cada iteração do loop, imprima o número atual 
    de estrelas em uma única linha.

Após concluir o exercício, sua saída deve se parecer com:

*****
****
***
**
*


"""

# Itera sobre os números de 5 a 1 (inclusive) em ordem descendente
for i in range(5, 0, -1):
    
    # Imprime 'i' estrelas
    print('*' * i)
    


"""
Exercício: Palavras com Mais de 4 Letras

Objetivo: Solicite ao usuário uma lista de palavras e, em 
seguida, exiba apenas as palavras que têm mais de 4 letras.

Instruções:

    1. Peça ao usuário que insira palavras separadas 
    por vírgula (por exemplo, ["casa","carro","sol","árvore"]).
    
    2. Use um loop for para iterar sobre essa lista de palavras.
    
    3. Dentro do loop, verifique o comprimento de cada palavra.
    
    4. Se a palavra tiver mais de 4 letras, imprima-a.

Após concluir o exercício, se o usuário inserir "casa,carro,sol,árvore", a saída deve ser:

carro
árvore

"""

# lista de palavras
palavras = ["casa","carro","sol","árvore", "ovo", "professor", "aluno"]

# Itera sobre a lista de palavras
for palavra in palavras:
    
    # Verifica se a palavra tem mais de 4 letras
    if len(palavra) > 4:
        
        # Imprime a palavra
        print(palavra)



#For Nested loops


# Exemplo de loops aninhados
# Inicia o loop externo, iterando a variável 'i' de 1 a 3 (o valor final 4 é exclusivo)
for linha in range(1, 4):
    
    # Inicia o loop interno, iterando a variável 'j' de 1 a 3 (o valor final 4 
    #é exclusivo) para cada valor de 'i'
    for coluna in range(1, 4):
        
        # Imprime o produto de 'i' e 'j', junto com os valores de 'i' e 'j' e os 
        #símbolos de multiplicação e igual
        print(i, "*", j, "=", i * j)



quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)



print()

quadrados_impares = []

for x in range(10):  # Itera sobre os números de 0 a 9
    if x % 2 != 0:  # Verifica se x é ímpar
        quadrados_impares.append(x**2)  # Calcula o quadrado de x e adiciona à lista

print(quadrados_impares)


#List Comprehensions (Compreensão de Listas)
#Criando uma lista de todos os caracteres em uma string que não são vogais:
texto = "Hello World"
consoantes = [char for char in texto if char.lower() not in 'aeiou']
print(consoantes)


#consoantes = [char for char in texto if char.lower() not in 'aeiou']

consoantes = []


# Lista vazia para armazenar os caracteres que não são vogais
consoantes_exemplo2 = []  

# Itera sobre cada caractere na string 'texto'
for letra in texto:  
    
    # Verifica se o caractere não é uma vogal
    if letra.lower() not in 'aeiou':  
        
        # Adiciona o caractere à lista 'consoantes'
        consoantes_exemplo2.append(letra)
        
print(consoantes_exemplo2)


"""
Exercício

Crie um programa em Python que solicite ao usuário que digite um número inteiro
não negativo. Em seguida, calcule e exiba o fatorial desse número.

Digite um número inteiro não negativo: 5
O fatorial de 5 é: 120
"""

# Solicita ao usuário a entrada de um número inteiro não negativo
numero = int(input("Digite um número inteiro não negativo: "))

# Verifica se o número informado é negativo
if numero < 0:
    
    # Se for negativo, exibe uma mensagem de erro
    print("O número deve ser não negativo.")
    
else:
    
    # Inicializa uma variável para armazenar o fatorial do número
    fatorial = 1

    # Loop que percorre todos os números inteiros de 1 até o número informado pelo usuário (inclusive)
    for i in range(1, numero + 1):
        
        # Multiplica o valor atual de 'fatorial' pelo número atual (i) na iteração
        # fatorial = fatorial * i
        fatorial *= i

    # Imprime o resultado final, que é o fatorial do número informado pelo usuário
    print("O fatorial de", numero, "é:", fatorial)
    

"""
Exercício

Crie um programa em Python que solicite ao usuário que digite um número inteiro
não negativo. Em seguida, calcule e exiba o fatorial desse número.

Digite um número inteiro não negativo: 5
O fatorial de 5 é: 120
"""

# Solicita ao usuário a entrada de um número inteiro não negativo
numero = int(input("Digite um número inteiro não negativo: "))

# Verifica se o número informado é negativo
if numero < 0:
    
    # Se for negativo, exibe uma mensagem de erro
    print("O número deve ser não negativo.")
    
else:
    
    # Inicializa uma variável para armazenar o fatorial do número
    fatorial = 1
    
    # Imprime a mensagem inicial indicando o cálculo do fatorial
    print("Cálculo do fatorial de", numero, ":")

    # Loop para multiplicar os números de 1 até o número informado
    for multiplicador in range(1, numero + 1):
        
        # Multiplica o valor atual de 'fatorial' pelo número atual na iteração
        fatorial *= multiplicador
        
        # Imprime o número da iteração atual seguido de "!" e o símbolo de igual
        print(f"{multiplicador}! =", end=" ")

        # Loop para imprimir a expressão do fatorial (e.g., "1 * 2 * 3")
        for i in range(1, multiplicador + 1):
            
            print(i, end="")
            
            if i != multiplicador:
                
                # Imprime o símbolo de multiplicação se não for o último número
                print(" * ", end="")
                
        # Imprime o resultado parcial do fatorial para a iteração atual
        print(" = ", fatorial)

    # Imprime o resultado final, que é o fatorial do número informado pelo usuário
    print("O fatorial de", numero, "é:", fatorial)



#For Criando um Retangulo

# Criando um retângulo com loops for
largura = 5  # Define a largura do retângulo
altura = 3   # Define a altura do retângulo

for i in range(altura):  # Loop para iterar pelas linhas do retângulo
    
    for j in range(largura):  # Loop para iterar pelas colunas do retângulo
    
        print("*", end=" ")  # Imprime o caractere "*" e um espaço na mesma linha
    
    print()  # Avança para a próxima linha após imprimir uma linha completa



# Criando um triângulo com a ponta no meios usando loops for

altura  = 5

for i in range(altura):
    
    espacos = altura - i - 1   

    asteriscos = 2 * i + 1
    print(" " * espacos + "*" * asteriscos)








