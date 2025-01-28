#Ponto Flutuante (float): Números reais, que têm uma parte decimal.
flutuante = 42.0
print("Flutuante:", flutuante)

#Complexos (complex): Números complexos, que têm uma parte real e uma parte imaginária.
complexo = 3 + 4j
print("Complexo:", complexo)

#Strings (str): Sequências de caracteres.
texto = "Olá, Mundo!"
print("Texto:", texto)

#Listas (list): Uma coleção ordenada e mutável.
lista = [1, 2, 3, 3]
print("Lista:", lista)

#Tuplas (tuple): Uma coleção ordenada e imutável.
tupla = (1, 2, 3, 4, 5)
print("Tupla:", tupla)

#Conjuntos (set): Uma coleção não ordenada de itens únicos.
conjunto = {1, 2, 3, 3}
print("Conjunto:", conjunto)

#Dicionários (dict): Uma coleção não ordenada de pares chave-valor.
dicionario = {"chave": "valor"}
print("Dicionário:", dicionario)

#Booleanos (bool): Valores verdadeiro ou falso.
booleano = True
print("Booleano:", booleano)

#NoneType (None): Um tipo especial que representa a ausência de valor.
nenhum = None
print("NoneType (None):", nenhum)

#Variaveis

idade = 30
nome = "Nicole"

print("Nome:", nome)
print("Idade:", idade)
print("Nome:", nome, ", Idade:", idade)


nome = str("Ana Paula")
idade = 31

print(type(nome))
print(type(idade))
#As variáveis diferenciam letras maiúsculas de minúsculas

i = 30
I = "Ana"

print(i)
print(I)



var1, var2, var3, var4 = "Texto 1", "Texto 2", "Texto 3", "Texto 4"

print(var1)
print(var2)
print(var3)
print(var4)

#Podemos atribuir o mesmo valor a várias variáveis em uma única linha

var1 = var2 = var3 = var4 = "Ana Paula"

print(var1)
print(var2)
print(var3)
print(var4)

#Se tiver uma coleção de valores em uma lista, podemos extrair em variáveis. Isso é chamado de descompactar

exemplo = "Texto 1", "Texto 2", "Texto 3", "Texto 4"
var1, var2, var3, var4 = exemplo

print(var1)
print(var2)
print(var3)
print(var4)

#Para juntar textos e variáveis em Python usamos o caracter + ou ,

nome = "Ana Paula"

print("O nome dela é " + nome)
numero1 = "Dez"
numero2 = "Cinco"

print(numero1 + numero2)

#Para juntar textos e variáveis em Python usamos o caracter + ou ,


nome = "Thuane"
sobrenome = "Alves"

print("Nome completo: " + nome + " " + sobrenome)

# Exercício de Variáveis em Python

# 1. Declare uma variável chamada "idade" e atribua o valor 25 a ela.
idade = 25

# 2. Declare uma variável chamada "nome" e atribua o valor "João" a ela.
nome = "João"

# 3. Declare uma variável chamada "saldo" e atribua o valor 100.50 a ela.
saldo = 100.50

# 4. Crie uma variável chamada "soma" e atribua a ela a soma das variáveis "idade" e "saldo".
soma = idade + saldo

# 5. Imprima na tela o valor da variável "soma".
print("A soma é:", soma)


# Exercício de Variáveis em Python

# 1. Crie uma variável chamada "nota1" e atribua o valor 7.5 a ela.
nota1 = 7.5

# 2. Crie uma variável chamada "nota2" e atribua o valor 8.3 a ela.
nota2 = 8.3

# 3. Crie uma variável chamada "nota3" e atribua o valor 6.9 a ela.
nota3 = 6.9

# 4. Calcule a média das três notas e atribua o resultado a uma variável chamada "media".
media = (nota1 + nota2 + nota3) / 3

# 5. Imprima na tela o valor da variável "media" formatado com duas casas decimais.
print("A média é:", format(media, ".2f"))


nome = input("Digite seu nome: \n")

print("\nO seu nome é: " + nome)


nome = input("Digite seu nome: \n")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print("\nAluno:", nome, " Média:", media)


#Tabuada

nDigitado = int(input("A tabuada de qual número você deseja ver? "))

print(nDigitado, "* 1 =", nDigitado * 1)
print(nDigitado, "* 2 =", nDigitado * 2)
print(nDigitado, "* 3 =", nDigitado * 3)
print(nDigitado, "* 4 =", nDigitado * 4)
print(nDigitado, "* 5 =", nDigitado * 5)
print(nDigitado, "* 6 =", nDigitado * 6)
print(nDigitado, "* 7 =", nDigitado * 7)
print(nDigitado, "* 8 =", nDigitado * 8)
print(nDigitado, "* 9 =", nDigitado * 9)
print(nDigitado, "* 10 =", nDigitado * 10)


ano_atual = 2023
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

print("Sua idade é:", idade)

#Números randomicos - Números aleatórios
import random

print(random.randrange(1, 1000))


#Gerar um número de ponto flutuante aleatório entre 0 e 1:
print(random.random())

#Gerar um número inteiro aleatório entre dois valores (inclusive):
print(random.randint(10, 20)) # Gera um número entre 10 e 20, inclusive.

#Escolher aleatoriamente um elemento de uma lista:
frutas = ["maçã", "banana", "cereja"]
print(random.choice(frutas)) # Escolhe uma fruta aleatoriamente da lista.

#Embaralhar aleatoriamente uma lista:
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros) # A lista 'numeros' agora está embaralhada.

#Gerar um número de ponto flutuante aleatório em um intervalo específico:
print(random.uniform(5.5, 9.5)) # Gera um número de ponto flutuante entre 5.5 e 9.5.

#Imprimindo a posição das letras

posicaoLetra = "Python"
print(posicaoLetra[0])
print(posicaoLetra[1])
print(posicaoLetra[2])
print(posicaoLetra[3])
print(posicaoLetra[4])


# Slice
frase = "Olá, mundo!"

# Obtendo uma parte da string usando slice
parte = frase[4:8]
print(parte)  # Saida:  mun

# Obtendo os primeiros 5 caracteres da string
primeiros = frase[:5]
print(primeiros)  # Saida: Olá,

# Obtendo os últimos 6 caracteres da string
ultimos = frase[-6:]
print(ultimos)  # Saida: mundo!

#Verifica se a palavra python está na frase


frase = "O módulo de python é muito legal"

print("python" in frase)




#verifica se a palavra python está na frase
frase = "O módulo de python é muito legal"

#if - se
if "python" in frase:
    print("Sim, a palavra python está presente na frase.")

#strip - Usamos para remover espaços em branco do inicio e do final da frase

frase = "        O módulo de python é muito legal       "

print(frase.strip())




#split, join e strip são métodos muito úteis da str
frase = "Olá, como vai você?"
palavras = frase.split()  # Dividindo a frase em palavras usando o espaço em branco como separador
print(palavras)
# Saída: ['Olá,', 'como', 'vai', 'você?']


#Método join(): O método join() junta os elementos de uma lista em uma única string, utilizando um separador especificado entre cada elemento.

palavras = ['Olá,', 'como', 'vai', 'você?']
frase = ' '.join(palavras)  # Juntando as palavras com um espaço em branco entre elas
print(frase)
# Saída: "Olá, como vai você?"

texto = "   Olá!    "
texto_strip = texto.strip()  # Removendo espaços em branco do início e do final
print(texto_strip)
# Saída: "Olá!"



texto = "********Olá!*********"
texto_strip = texto.strip('*')  # Removendo os caracteres '*' do início e do final
print(texto_strip)
# Saída: "Olá!"



#Utilizando Formated Strings

nome = "Alice"
idade = 25
altura = 1.65

# Criando uma mensagem formatada usando f-string
mensagem = f"Olá, meu nome é {nome}. Tenho {idade} anos e minha altura é {altura:.2f} metros."

print(mensagem)




# Métodos para Strings
texto = "OLá, mundo!"

# Método upper() - Converte a string para maiúsculas
texto_upper = texto.upper()
print(texto_upper)  # Output: OLÁ, MUNDO!

# Método lower() - Converte a string para minúsculas
texto_lower = texto.lower()
print(texto_lower)  # Output: olá, mundo!

# Método capitalize() - Capitaliza a primeira letra da string
#a primeira letra "o" é convertida em maiúscula, resultando em "Olá, mundo!". As demais letras permanecem em minúsculas.
texto_capitalize = texto.capitalize()
print(texto_capitalize)  # Output: Olá, mundo!

# Método count() - Conta o número de ocorrências de um determinado caractere ou substring na string
ocorrencias = texto.count("o")
print(ocorrencias)  # Output: 2

# Método replace() - Substitui todas as ocorrências de uma substring por outra
texto_substituido = texto.replace("mundo", "amigo")
print(texto_substituido)  # Output: Olá, amigo!

# Método split() - Divide a string em uma lista de substrings com base em um caractere delimitador
palavras = texto.split(",")
print(palavras)  # Output: ['Olá', ' mundo!']

# Método join() - Junta uma lista de strings em uma única string, separadas por um caractere específico
lista_palavras = ['Olá', 'mundo!']
texto_junto = ",".join(lista_palavras)
print(texto_junto)  # Output: Olá,mundo!

# Exercício de Manipulação de Strings em Python

# 1. Crie uma variável chamada "nome" e atribua a ela o valor "Maria".
nome = "Maria"

# 2. Crie uma variável chamada "sobrenome" e atribua a ela o valor "Silva".
sobrenome = "Silva"

# 3. Crie uma variável chamada "idade" e atribua a ela o valor 30.
idade = 30

# 4. Concatene as variáveis "nome" e "sobrenome" em uma nova variável chamada "nome_completo".
nome_completo = nome + " " + sobrenome

# 5. Imprima na tela o valor da variável "nome_completo".
print(nome_completo)

# 6. Crie uma variável chamada "mensagem" que utilize a função format para criar uma frase 
#personalizada com as variáveis "nome_completo" e "idade".
mensagem = "Olá, meu nome é {} e tenho {} anos.".format(nome_completo, idade)

# 7. Imprima na tela o valor da variável "mensagem".
print(mensagem)

# Exercício de Manipulação de Strings em Python

# 1. Crie uma variável chamada "frase" e atribua a ela a seguinte 
#frase: "Python é uma linguagem de programação poderosa e versátil."

frase = "Python é uma linguagem de programação poderosa e versátil."

# 2. Imprima na tela o tamanho da frase, ou seja, a quantidade de 
#caracteres presentes nela.

tamanho_frase = len(frase)
print("Tamanho da frase:", tamanho_frase)

# 3. Crie uma variável chamada "palavra" e atribua a ela a primeira 
#palavra da frase.

palavra = frase.split()[0]
print("Primeira palavra da frase:", palavra)

# 4. Converta a variável "frase" para letras maiúsculas e atribua o 
#resultado a uma nova variável chamada "frase_maiuscula".

frase_maiuscula = frase.upper()
print("Frase em maiúsculas:", frase_maiuscula)

# 5. Substitua a palavra "poderosa" por "incrível" na variável 
#"frase" e atribua o resultado a uma nova variável chamada "frase_substituida".

frase_substituida = frase.replace("poderosa", "incrível")
print("Frase com substituição:", frase_substituida)


