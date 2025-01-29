#Python função If ou seja função Se

numero1 = 90
numero2 = 12

#Se a variável número1 é maior que a variável número 2
if numero1 > numero2:
    
    print("O número da variável  numero1 é maior que o número da variável numero2")

#Python função If... elif
#if - Se
#elif - Senão Se

numero1 = 6
numero2 = 6

if numero1 > numero2:
    
    print("O número da variável  numero1 é maior que o número da variável numero2")
    
elif numero1 == numero2:
    
    print("O número da variável numero1 é igual ao número da variável numero2")


# Define o número secreto que o usuário deve adivinhar
numero_secreto = 7

# Solicita ao usuário para inserir um número inteiro entre 1 e 10
chute = int(input("Tente adivinhar o número secreto entre 1 e 10: "))

# Verifica se o número inserido pelo usuário é igual ao número secreto
if chute == numero_secreto:
    
    # Se o usuário adivinhar corretamente, imprime uma mensagem de sucesso
    print("Parabéns! Você adivinhou o número secreto.")

#else - Senão
else:
    
    # Se o usuário adivinhar errado, imprime uma mensagem de erro
    print("Desculpe, você não adivinhou o número secreto. Tente novamente!")



# Pergunta ao usuário sua idade
idade = int(input("Por favor, digite sua idade: "))

#if - se
# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    
    # Se a idade for maior ou igual a 18, imprime que o usuário está elegível para votar
    print("Você é elegivel para votar.")

#else - senão
else:
    
    # Se a idade for menor que 18, imprime que o usuário não está elegível para votar
    print("Você não é elegivel para votar.")




#Função If... elif ... else
#Se... Senão Se ... Senão

numero1 = 9
numero2 = 6

if numero1 > numero2:
    
    print(f"O {numero1} é maior que o {numero2}")
    
elif numero1 == numero2:
    
    print(f"O {numero1} é IGUAL ao {numero2}")
    
else:
    
    print(f"O {numero1} é MENOR que o {numero2}")

#and - E

numero1 = 50
numero2 = 21
numero3 = 200

if numero1 > numero2 and numero3 > numero1:
    
    print("As duas condições são verdadeiras")
    


nota = int(input("Por favor, digite a nota do estudante (0-100): "))

#Verifica em qual categoria a nota se encaixa
if nota >= 90 and nota <= 100:
    
    print("Excelente!")
    
elif nota >= 70 and nota <= 89:
    
    print("Bom!")
    
elif nota >= 50 and nota <= 69:
    
    print("Satisfatório!")
    
else:
    
    print("Insuficiente!")


# Solicita ao usuário o valor da compra
valor_compra = float(input("Por favor, digite o valor da sua compra: $"))

# Verifica em qual categoria de desconto a compra se encaixa
if valor_compra > 1000:
    
    # Se a compra for maior que R$1000, aplica um desconto de 20%
    desconto = 0.20 * valor_compra
    
    # Imprime uma mensagem informando o desconto de 20%
    print("Você recebeu 20% de desconto!")
    
elif valor_compra >= 500 and valor_compra <= 1000:
    
    # Se a compra for entre R$500 e R$1000, aplica um desconto de 10%
    desconto = 0.10 * valor_compra
    
    # Imprime uma mensagem informando o desconto de 10%
    print("Você recebeu 10% de desconto!")
    
else:
    
    # Se a compra for menor que $500, não aplica desconto
    desconto = 0
    
    # Imprime uma mensagem informando que não há desconto
    print("Você não recebeu desconto.")

# Calcula o valor final após o desconto
valor_final = valor_compra - desconto

# Imprime o valor do desconto e o valor final da compra
print(f"Valor do desconto: R${desconto:.2f}")
print(f"Valor final da compra: R${valor_final:.2f}")


#If ... Or
#Se ... Ou

numero1 = 19
numero2 = 150
numero3 = 18

if numero1 > numero2 or numero1 > numero3:
    
    print(f"O {numero1} é maior que {numero2} ou o {numero1} é maior que {numero3}!")
    

# Pergunta ao usuário se possui um convite VIP
convite_vip = input("Você possui um convite VIP? (sim/não):")

# Pergunta ao usuário está na lista de convidados
na_lista = input("Você está na lista de convidados? (sim/não):")

# Pergunta ao usuário se é um membro do clube
membro_clube = input("Você é um membro do clube? (sim/não):")
       
# Verifica se o usuário atende a pelo menos uma das condições
if convite_vip == "sim" or na_lista  == "sim" or membro_clube == "sim":
                  
    # Se atender a pelo menos uma das condições, permite a entrada
    print("Bem-vindo(a) ao evento!")
                     
else:
    
    # Se não atender a nenhuma das condições, nega a entrada
    print("Desculpe, você não pode entrar no evento.")

#Exercicio Par ou Impar
#Crie um algoritmo que solicite a entrada de um número positivo e inteiro e imprima se o
#número é PAR ou IMPAR

n1 = int(input("Digite um número: "))

verificaNumero = n1 % 2

if verificaNumero == 0:
    
    print(f"O número {n1} é PAR")
    
else:
    
    print(f"O número {n1} é IMPAR")


#Estrutura condicional ternária

#age - idade

age = 17
status = "adulto" if age >= 18 else "menor de idade"
print(status) #Saída: "adulto"

#Suponhamos que você queira determinar se um número é par ou impar:

numero = 42
resultado = "par" if numero % 2 == 0 else "impar"
print(resultado) #Saída: "par"


#Suponha que você tenha pontuação e queira categoriza-la
#como "baixa", "média" ou "alta"

score = 85
categoria = "baixa" if score < 50 else "média" if score < 80 else "alta"
print(categoria)

print()
