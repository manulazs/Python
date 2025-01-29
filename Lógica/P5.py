
#Criando uma função de soma
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)  # Saída: 5

resultado = soma(8, 9)
print(resultado)  # Saída: 5

resultado = soma(3, 7)
print(resultado)  # Saída: 5

#Criando uma função de soma
def soma(a, b):
    return a + b

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = soma(numero1, numero2)
print("A soma é:", resultado)

#Parâmetros e Argumentos em uma função
def saudacao(nome):
    """Função que exibe uma saudação personalizada."""
    print("Olá, " + nome + "! Bem-vindo(a)!")

# Argumento passado para a função
nome_usuario = "Maria"

# Chamada da função com o argumento
saudacao(nome_usuario)


#Argumentos Default e Non-default



def exibir_informacoes(nome="Allan", idade=39, cidade="Desconhecida"):
    
    """Função que exibe informações pessoais."""
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)
    print()

# Argumentos sem valores default
exibir_informacoes("João", 25, "São Paulo")

# Argumento com valor default
exibir_informacoes("Maria", 30)

#Exemplo com print():
def saudacao(nome):
    
    """Função que imprime uma saudação personalizada."""
    print("Olá, " + nome + "! Bem-vindo(a) ao nosso programa.")

saudacao("João")

#Exemplo com return:
def soma(a, b):
    
    """Função que retorna a soma de dois números."""
    return a + b

resultado = soma(3, 4)
print("O resultado da soma é:", resultado)

#Vários argumentos *args com números

"""
 parâmetro especial *args, que permite receber um número variável de argumentos numéricos. 
 Dentro da função, os argumentos são tratados como uma tupla.
"""

def soma(*args):
    resultado = sum(args)
    return resultado

total = soma(2, 4, 6, 8, 10)
print("A soma dos números é:", total)


"""
Exercício: Função para Calcular Estatísticas de Números

Objetivo: Familiarizar com a definição de funções que 
aceitem um número variável de argumentos usando *args, bem como calcular 
algumas estatísticas básicas de um conjunto de números.

Instruções:

    1. Defina uma função chamada estatisticas que aceite 
    um número variável de argumentos numéricos.
    
    2. A função deve retornar a média, o maior e o menor número do conjunto.
    3. Peça ao usuário para inserir uma sequência de números, separados por espaços.
    4. Converta essa entrada do usuário em uma lista de números.
    5. Use a função estatisticas para calcular a média, o maior e o menor número da lista.
    6. Mostre ao usuário a média, o maior e o menor número.
"""

def estatisticas(*args):
    
    return sum(args) / len(args), max(args), min(args)


numeros = list(map(float, input("Digite uma sequência de números separados por espaços: ").split()))

media, maior, menor = estatisticas(*numeros)

print(f"Média: {media}")
print(f"Maior Número: {maior}")
print(f"Menor Número: {menor}")


#Vários argumentos xargs nomeando parametros

#função que recebe vários argumentos nomeados usando **kwargs:


def exibir_informacoes(**teste):
    
    """Função que exibe informações pessoais"""
    for chave, valor in teste.items():
        print(chave + ": " + str(valor))
        
exibir_informacoes(nome="João", idade=25, cidade="São Paulo", sexo="Masculino")


# Definindo uma variável global fora de qualquer função
variavel_global = "Eu sou uma variável global"

# Definindo a função funcao_exemplo
def funcao_exemplo():
    
    # Criando uma variável local dentro da função
    variavel_local = "Eu sou uma variável local"
    
    # Imprimindo a variável local
    print(variavel_local)
    
    # Imprimindo a variável global dentro da função (é possível acessá-la, mas 
    # para modificá-la, precisaríamos usar a palavra-chave 'global')
    print(variavel_global)
    

# Chamando a função funcao_exemplo, que imprimirá ambas as variáveis
funcao_exemplo()

# Imprimindo a variável global fora da função
print(variavel_global)

# print(variavel_local)  # Isso resultaria em um erro, pois variavel_local não existe fora da função.



# Definindo uma variável global chamada 'contador' e inicializando com 0
contador = 0


# Definindo a função 'incrementar_contador'
def incrementar_contador():
    
    # Informando à função que vamos usar a variável global 'contador' e não uma variável local
    global contador
    
    # Incrementando o valor da variável global 'contador'
    # contador = contador + 1
    contador += 1
    
    # Imprimindo o valor atualizado de 'contador'
    print(contador)

# Chamando a função 'incrementar_contador' pela primeira vez
# Isso incrementa 'contador' para 1 e imprime o valor
incrementar_contador()  # Imprime 1

# Chamando a função 'incrementar_contador' novamente
# Agora, 'contador' é incrementado para 2 e o novo valor é impresso
incrementar_contador()  # Imprime 2

incrementar_contador()  # Imprime 3



print("\n---------------------------\n")

# Definindo a função 'funcao_externa'
def funcao_externa():
    
    # Criando uma variável 'variavel_externa' dentro do escopo da 'funcao_externa'
    variavel_externa = "Eu sou externa"
    
    # Definindo uma função aninhada chamada 'funcao_interna' dentro de 'funcao_externa'
    def funcao_interna():
        
        # Usando a palavra-chave 'nonlocal' para indicar que queremos
        # modificar a 'variavel_externa' do escopo imediatamente 
        # superior, ou seja, da 'funcao_externa'
        nonlocal variavel_externa
        
        print(variavel_externa)
        
        # Modificando a 'variavel_externa'
        variavel_externa = "Eu fui modificada pela função interna"
        
        # Imprimindo a 'variavel_externa' após modificá-la
        print(variavel_externa)
        
    # Chamando a 'funcao_interna' dentro da 'funcao_externa', que 
    # por sua vez modifica e imprime a 'variavel_externa'
    funcao_interna()
    
    # Imprimindo a 'variavel_externa' após a 'funcao_interna' 
    # ter sido chamada e ter modificado seu valor
    print(variavel_externa)

# Chamando a função 'funcao_externa' para executar o fluxo acima
funcao_externa()


#Atribuindo funções a variáveis:
# Definindo uma função simples
def saudacao():
    
    return "Olá, mundo!"

# Atribuindo a função à variável 'cumprimentar'
cumprimentar = saudacao

# Chamando a função através da variável
print(cumprimentar())  # Saída: Olá, mundo!

#---------------------------

#Passando funções como argumentos

# Definindo duas funções simples
def saudacao_nome(nome):
    
    return f"Olá, {nome}!"

def cumprimentar(funcao, nome):
    
    return funcao(nome)

# Usando a função 'cumprimentar' e passando 'saudacao_nome' como um argumento
print(cumprimentar(saudacao_nome, "Alice"))  # Saída: Olá, Alice!

#------------------------------


#Retornando funções de outras funções

# Definindo uma função que retorna outra função
def nivel_saudacao(nivel):
    
    def saudacao_basica():
        return "Oi!"
    
    def saudacao_avancada():
        return "Olá, como você está?"

    if nivel == "basico":
        
        return saudacao_basica
    
    else:
        return saudacao_avancada

# Chamando a função 'nivel_saudacao' que retorna uma função, e depois chamando a função retornada
cumprimento = nivel_saudacao("basico")
print(cumprimento())  # Saída: Oi!

cumprimento = nivel_saudacao("avancado")
print(cumprimento())  # Saída: Olá, como você está?


"""
Exercício: Calculadora Simples com Funções

Objetivo: Criar uma calculadora simples que pode realizar 
quatro operações básicas: adição, subtração, multiplicação e divisão.

O usuário deverá fornecer dois números e a operação desejada. A solução 
deve ser implementada usando funções.

Instruções:

    Defina quatro funções: adicionar(), subtrair(), multiplicar() e dividir(). 
    
    - Cada função deve aceitar dois parâmetros (números) e retornar o resultado 
    da operação correspondente.
    - Peça ao usuário para inserir dois números.
    - Peça ao usuário para escolher uma das quatro operações (por exemplo, 
    ele pode digitar "adicionar" para adição).
    - Com base na escolha do usuário, chame a função correspondente e imprima o resultado.

"""

# Definindo as funções para as operações básicas

# Definindo a função para adicionar dois números
def adicionar(a, b):
    
    # Retorna a soma de a e b
    return a + b  

# Definindo a função para subtrair um número do outro
def subtrair(a, b):
    
    # Retorna a diferença entre a e b
    return a - b  

# Definindo a função para multiplicar dois números
def multiplicar(a, b):
    
    # Retorna o produto de a e b
    return a * b  

# Definindo a função para dividir um número pelo outro
def dividir(a, b):
    
    # Retorna a divisão de a por b
    return a / b  

# Solicitando ao usuário o primeiro número e convertendo-o para float
num1 = float(input("Digite o primeiro número: "))

# Solicitando ao usuário o segundo número e convertendo-o para float
num2 = float(input("Digite o segundo número: "))

# Solicitando ao usuário que escolha uma das operações definidas
op = input("Escolha uma operação (adicionar, subtrair, multiplicar, dividir): ")

# Usando condicionais para determinar qual função chamar com base na escolha do usuário
if op == "adicionar":
    
    # Chama a função de adição se o usuário escolheu 'adicionar'
    resultado = adicionar(num1, num2)  
    
elif op == "subtrair":
    
    # Chama a função de subtração se o usuário escolheu 'subtrair'
    resultado = subtrair(num1, num2)   
    
elif op == "multiplicar":
    
    # Chama a função de multiplicação se o usuário escolheu 'multiplicar'
    resultado = multiplicar(num1, num2) 
    
elif op == "dividir":
    
    # Chama a função de divisão se o usuário escolheu 'dividir'
    resultado = dividir(num1, num2)     
    
else:
    
    # Imprime uma mensagem de erro se o usuário não escolheu uma operação válida
    print("Operação inválida.")         

# Imprime o resultado da operação escolhida
print("Resultado:", resultado)


"""
Exercício: Fábrica de Funções de Operações Matemáticas

Imagine que você está construindo uma calculadora. Porém, ao invés de 
implementar cada operação matemática (soma, subtração, multiplicação e divisão) 
diretamente, você decide criar uma "fábrica de funções". Esta fábrica, quando fornecida 
com o nome de uma operação, deve retornar uma função que realiza a operação desejada.

Instruções:

    - Escreva uma função chamada fábrica_de_operacoes que aceite uma 
    string: 'soma', 'subtracao', 'multiplicacao' ou 'divisao'.
    
    - Dependendo do argumento fornecido, sua função deve retornar uma das 
    operações matemáticas. Por exemplo, se o argumento for 'soma', a função 
    retornada deve ser capaz de somar dois números.
    
    - Se a operação não for reconhecida, retorne uma função que 
    imprima "Operação não suportada.".
    
    
Desafio Extra:
Adapte a fábrica para aceitar operações com 
mais de dois números. Por exemplo, a operação de soma deve 
ser capaz de somar três, quatro ou mais números de uma só vez.

Dica: Utilize argumentos variáveis (*args) para essa adaptação.
"""

def fabrica_de_funcoes(operacao):
    
    # Esta função recebe um número indefinido de argumentos e os soma.
    def soma(*args):
        
        return sum(args)
    
    # Esta função subtrai todos os números subsequentes do primeiro número.
    def subtracao(*args):
        
        resultado = args[0]
        
        # Itera sobre todos os números após o primeiro
        for num in args[1:]:
            
            #resultado = resultado - num
            resultado -= num
            
        return resultado
    
    # Esta função multiplica todos os números fornecidos.
    def multiplicacao(*args):
        
        resultado = 1
        
        # Itera sobre todos os números e os multiplica
        for num in args:
            
            #resultado = resultado * num
            resultado *= num
            
        return resultado
    
    # Esta função divide o primeiro número pelos números subsequentes.
    def divisao(*args):
        
        resultado = args[0]
        
        # Itera sobre todos os números após o primeiro
        for num in args[1:]:
            
            # Verifica se algum número é zero (para evitar divisão por zero)
            if num == 0:
                
                raise ValueError("Divisão por zero não é permitida.")
                
            resultado /= num
            
        return resultado
    
    # Retorna a função correspondente baseada no valor da 'operacao'
    if operacao == "soma":
        
        return soma
    
    elif operacao == "subtracao":
        
        return subtracao
    
    elif operacao == "multiplicacao":
        
        return multiplicacao
    
    elif operacao == "divisao":
        
        return divisao
    
    else:
        
        def operacao_nao_suportada(*args):

            return "Operação não suportada."
        
        return operacao_nao_suportada
    
    
# Testando o código
adicionar = fabrica_de_funcoes("soma")
print(adicionar(5, 3, 2, 9, 4, 7)) # Esperado: 30

subtrair = fabrica_de_funcoes("subtracao")
print(subtrair(50, 30, 5)) # Esperado: 15

multiplicar = fabrica_de_funcoes("multiplicacao")
print(multiplicar(5, 3, 2)) # Esperado: 30

dividir = fabrica_de_funcoes("divisao")
print(dividir(10, 2, 2)) # Esperado: 2.5

operacao_invalida = fabrica_de_funcoes("modulo")
print(operacao_invalida(5, 3)) # Esperado: "Operação não suportada."
            


"""
Funções Anônimas (Lambda)
o	Definição e uso
o	Limitações em relação às funções regulares


Função lambda


Funções lambda são funções anônimas de pequena extensão. Ao contrário 
de uma função definida com def, a função lambda pode ter apenas uma 
expressão e retorna implicitamente o resultado dessa expressão. Ela é 
frequentemente usada para pequenas operações que são convenientes de 
se definir sem nomear uma função completa.


"""

#Exemplo Prático 1: Definição e uso

#Função Regular para Dobrar um Número

def dobrar(n):
    
    return n * 2

print("Função Regular:", dobrar(5)) # Saída: 10 

#Função Lambda para Dobrar um Número
dobrar_com_lambda = lambda n: n * 2

print("Função Lambda:", dobrar_com_lambda(5)) # Saída: 10 


def classificar_numero(n):
    
    if n < 0:
        
        return "Negativo"
    
    elif n == 0:
        
        return "Zero"
    
    else:
        
        return "Positivo"

print(classificar_numero(5)) #Saída: Positivo

#Tentativa de Função lambda para Classificar Números (Menos Clara):

classificar_numero_lambda = lambda n: "Negativo" if n < 0 else ( "Zero" if n == 0 else "Positivo")

print(classificar_numero_lambda(5)) #Saída: Positivo

pessoas = [("João", 35), ("Maria", 25), ("Pedro", 40)]
pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])

print(pessoas_ordenadas)  # Saída: [('Maria', 25), ('João', 35), ('Pedro', 40)]

#No exemplo acima, estamos usando a função lambda 
#para especificar que queremos ordenar as tuplas pela idade (índice 1).


contador = 0

def aumentar_contador():
    
    global contador
    
    contador += 1 

aumentar_contador()
print(contador)

aumentar_contador()
print(contador)

aumentar_contador()
print(contador)

#Tentativa de Função Lambda Modificando uma Variável Global (Isso causará um erro):
# A seguinte linha causará um erro se descomentada
# aumentar_contador = lambda: global contador; contador += 1


#Esses exemplos práticos ajudam a entender a versatilidade e as 
#limitações das funções lambda em comparação com as funções regulares.

#função lambda com filter


# Lista original de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando filter() e lambda para obter apenas números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))



print(numeros_pares)  # Saída: [2, 4, 6, 8, 10]


# Lista original de nomes
nomes = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Tom"]

# Usando filter() e lambda para obter apenas nomes que começam com "A"
nomes_com_A = list(filter(lambda nome: nome[0] == "A", nomes))

print(nomes_com_A)  # Saída: ['Alice', 'Anna', 'Alex']


# Lista original de nomes
nomes = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Tom", "Alice"]

# Usando filter() e lambda para obter apenas as entradas que são "Alice"
nomes_Alice = list(filter(lambda nome: nome == "Alice", nomes))

print(nomes_Alice)  # Saída: ['Alice', 'Alice']


#Função lambda com map

# Lista original de números
numeros = [1, 2, 3, 4, 5]

# Usando map() e lambda para elevar cada número ao quadrado
numeros_ao_quadrado = list(map(lambda x: x**2, numeros))


print(numeros_ao_quadrado)  # Saída: [1, 4, 9, 16, 25]


# Lista original de palavras
palavras = ["maça", "banana", "arroz", "abacate"]

# Usando map() e lambda para obter o comprimento de cada palavra
comprimentos = list(map(lambda palavra: len(palavra), palavras))

"""
    list(): Esta função é utilizada para converter um iterável (como o resultado 
    do map()) em uma lista. A função map(), por padrão, retorna um iterador, e ao envolvê-lo 
    com list(), estamos convertendo esse iterador em uma lista real.

    map(): A função map() é uma função built-in do Python que aplica uma função a 
    todos os itens em um iterável (neste caso, a lista palavras). A ideia principal 
    aqui é transformar cada item da lista original (cada palavra) em um novo 
    valor (neste caso, o comprimento de cada palavra).
"""

print(comprimentos)  # Saída: [4, 6, 5, 7]

"""
Exercício: Filtrando e Transformando Dados com Lambda

Objetivo: Familiarizar-se com o uso de funções lambda 
juntamente com funções built-in como filter e map.

Instruções:

    1. Dada uma lista de números: numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28].
    
    2. Use a função filter() e uma função lambda para criar uma nova 
    lista que contém apenas os números ímpares da lista original.
    
    3. Em seguida, use a função map() e uma função lambda para 
    criar uma nova lista que contém o quadrado de cada número da lista de números ímpares.
    
    4. Imprima ambas as listas.
    
    Dicas:

    Use filter() para filtrar itens de uma lista.
    Use map() para aplicar uma função a cada item de uma lista.
"""

# Lista inicial de números
numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]

# Filtrando números ímpares
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))


# Obtendo o quadrado de cada número ímpar
quadrados_impares = list(map(lambda x: x ** 2, numeros_impares))

# Imprimindo os resultados
print(f"Números ímpares: {numeros_impares}")
print(f"Quadrados dos números ímpares: {quadrados_impares}")



#Funções Internas (built-in)

#print(): Utilizada para imprimir valores no console.

nome = "Maria"
print("Olá,", nome)  # Saída: Olá, Maria


#len(): Retorna o número de itens em um objeto.
lista = [1, 2, 3, 4]
print(len(lista))  # Saída: 4

#input(): Lê uma linha do input (entrada padrão).
#nome = input("Digite seu nome: ")  

# O usuário insere "Carlos" e pressiona enter
print("Seu nome é", nome)  # Saída: Seu nome é Carlos

#Conversão de tipos

#int(): Converte um valor para um inteiro.
numero_decimal = "7.9"
numero_inteiro = int(float(numero_decimal))  

#Nota: Aqui, primeiramente converti a string para float, e depois 
#para int, porque diretamente não podemos converter a string "7.9" para int.

print(numero_inteiro)  # Saída: 7

#float(): Converte um valor para ponto flutuante (decimal).
numero_str = "5.6"
numero_float = float(numero_str)
print(numero_float)  # Saída: 5.6

#str() - Converte um valor para string
numero = 123
numero_str = str(numero)
print(numero_str)


#1. Funções que chamam a si mesmas:

#Uma função recursiva é uma função que se chama a si mesma em sua definição.
# Define uma função chamada contar_regressivamente
def contar_regressivamente(n):
                           
    # Verifica se n é maior que 0
    if n > 0:
                           
        # Imprime o valor atual de n
        print(n)
                           
        # Chama a função contar_regressivamente passando n-1 como argumento (recursividade)
        contar_regressivamente(n-1)

# Chama a função contar_regressivamente com o valor inicial 5
contar_regressivamente(5)



#Fatorial:
#O fatorial de um número é o produto desse número por todos os seus 
#antecessores até 1. Por exemplo, 5! (lê-se "5 fatorial") é 5 × 4 × 3 × 2 × 1 = 120.
# Define uma função chamada fatorial
def fatorial(n):
                           
    # Se n for 0, o fatorial de 0 é definido como 1
    if n == 0:
        
        return 1
                           
    else:
        
        # Caso contrário, o fatorial de n é n multiplicado pelo fatorial de n-1 (chamada recursiva)
        return n * fatorial(n-1)

# Imprime o fatorial de 5
print(fatorial(5))  # Saída: 120




def recursao_infinita(n):
    
    print(n)
    
    return recursao_infinita(n+1)

#recursao_infinita(1)

print()


#Exemplo
def somar(a, b):
    return a + b


print(somar(2, 3))  # Saída: 5
print(somar.__doc__)  # Isso imprimirá a docstring da função


#2. Anotações de tipo (Type Hints)
def multiplicar(a: int, b: int) -> int:
    
    """Função que retorna a multiplicação de dois números inteiros."""
    return a * b

print(multiplicar(4, 5))  # Saída: 20










