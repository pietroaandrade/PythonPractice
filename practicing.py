# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor
# válido. *** 3 Tentativas incorretas ***

"""while True:
    num = input("Give me a number between zero and ten")
    if num.isnumeric():
        num = int(num)
        if num > 0 and num < 10:
            print(f"{num} is in the correct range")
            print(f"Number {num} is Accepted")
            break
        print(f"Number {num} is in the incorrect range")
    else:
        print(f"{num} is not a number")"""

# Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';

"""name = input("What's your name?")
while len(name) < 3:
    print("Invalid name length")
    name = input("What's your name?")
else:
    print("Name Accepted")
while True:
    age = input("What's your age?")
    if age.isnumeric():
        age = int(age)
        if age > 0 and age < 150:
            print("Accepted age")
            break
        else:
            print("Invalid age")
    else:
        print(f"{age} is not your age")
salary = input("What's your salary:")
while not salary.isnumeric():
    print("Salary must be a number bigger than 0")
    salary = input("What's your salary:")
print("salary accepted")

gender = input("What's your gender")
while not (gender == "m" or gender == "f"):
    print("There's only two genders...")
    gender = input("What's your gender")
print("Gender accepted")

ms = input("What's your marital status")
while not (ms == "m" or ms == "s" or ms == "w"):
    print("marital status: 'm', 's', 'w'")
    ms = input("What's your marital status")
print("Marital Status accepted")
"""

# Supondo que a população de um país A seja da ordem de 80000 habitantes com
# uma taxa anual de crescimento de 3% e que a população de B seja 200000
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse
# ou iguale a população do país B, mantidas as taxas de crescimento.

"""a = 80000
b = 200000
t = 0
while b > a:
    a *= 1.03
    b *= 1.015
    t += 1
print(t)
"""

# Faça um programa que leia 5 números e informe a soma e a média dos números.

"""soma = 0
i = 0
while i < 5:
    num = int(input("Give me a number"))
    soma += num
    i += 1
media = soma / i

print(soma)
print(media)"""

# Faça um programa que receba dois números inteiros e gere os números inteiros
# que estão no intervalo compreendido por eles.

"""a = int(input("Me de um numero"))
b = int(input("Me de um segundo numero"))

if b < a:
    a, b = b, a
a += 1
while a < b:
    print(a)
    a += 1"""

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
# pedir as informações.

"""while True:
    user = input("Sign-in username")
    password = input("Sign-in password")
    if password == user:
        print("User and password can't be the same")
        user = input("Sign-in username")
        password = input("Sign-in password")
    else:
        print("Signed-In Succesfully")
        break"""

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
# inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
# tabuada. A saída deve ser conforme o exemplo abaixo:

"""num = 1
while num <= 10:
    mult = 1
    print(f"tabuada do {num}")
    while mult <= 10:
        tabuada = num * mult
        print(f"{num} * {mult} = {tabuada}")
        mult += 1
    print()
    num+=1"""

# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um
# programa capaz de gerar a série até o n−ésimo termo

"""i = 0
a = 1
b = 1
contador = int(input("Me de um numero"))
while i < contador:
    c = a + b
    print(c)
    a = b               # }
    b = c               # }
    #a, b = b, c        other way of stating these
    i += 1"""

# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
# números pares e a quantidade de números ímpares.

"""i = 0
pares = 0
impares = 0
while i < 10:
    num = int(input("Me de um numero"))
    if num%2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1

print(f"Pares: {pares} e Impares: {impares}")
"""


# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
# usuário. Ex.: 5!=5.4.3.2.1=120

"""num = int(input("me de um numer para fatorial"))
fatorial = 1
while num >= 1:
   print(num)
   fatorial = fatorial * num
   num = num - 1
print(fatorial)
"""

# Faça um programa que peça um número inteiro e determine se ele é ou não um
# número primo. Um número primo é aquele que é divisível somente por ele mesmo e por um

"""num = int(input("Me de um numero, checarei se ele é primo:"))

i = 2
while i < num:
    if num%i == 0:
        print("nao primo")
        break
    i += 1
else:
    print("primo")
"""

#Faça um programa que calcule o mostre a média aritmética de N notas.

"""num_notas = int(input("quantas notas que calcular?"))
i = 0
media = 0
soma = 0
while i < num_notas:
    notas = int (input("me de as notas"))
    soma += notas
    i +=1
media = soma / num_notas

print(media)"""


# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# 1. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# 2. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# 3. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
# dobro do percentual do ano anterior. Faça um programa que determine o
# salário atual desse funcionário. Após concluir isto, altere o programa
# permitindo que o usuário digite o salário inicial do funcionário.


"""contador = 1
salario = 1000
anos = 30
percentual = 0.015

while contador <= anos:
    aumento = salario * percentual
    salario += aumento
    contador += 1
    percentual *= 2

print(salario)"""

contador = 1
salario = 1000
anos = 30
percentual = 0.015

while contador <= anos:
    aumento = salario * percentual
    salario += aumento
    contador += 1
    percentual *= 2

print(f"Salário final após {anos} anos: R$ {salario:.2f}")

# Solicitar o salário inicial e o ano atual
salario_inicial = float(input("Digite o salário inicial do funcionário (em R$): "))
ano_atual = int(input("Digite o ano atual: "))

# Inicializar o salário com o salário inicial e o ano de contratação
salario = salario_inicial
ano_contratacao = 1995
aumento_percentual = 1.5 / 100  # 1,5% de aumento em 1996
ano = 1996

# Calcular os aumentos anuais até o ano atual
while ano <= ano_atual:
    # Aplica o aumento no salário
    salario += salario * aumento_percentual
    # Dobrar o aumento percentual para o próximo ano
    aumento_percentual *= 2
    # Avançar para o próximo ano
    ano += 1

# Exibir o salário final
print(f"O salário do funcionário no ano de {ano_atual} é: R$ {salario:.2f}")

