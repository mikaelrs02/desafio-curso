# Desafio 1: O Código Secreto da Escola Vai na Web


# Missão 1: Restaurando as Regras Escolares 📝
def verificar_aprovacao(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"
# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno: "))
resultado = verificar_aprovacao(nota)
print(f"O aluno foi {resultado}.")
#----------------------------------------------

# Missão 2: O Sistema Eleitoral Secreto 📝
# Verifique a elegibilidade para votar com base na idade
def verificar_idade_votacao(idade):
    if idade >= 16:
        return "Você pode votar."
    else:
        return "Você não pode votar."

# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))
eligibilidade = verificar_idade_votacao(idade)
print(eligibilidade)
#----------------------------------------------

# Missão 3: Recuperando o Sistema de Notas 📊
# Classifica o aluno com base na nota
def classificar_nota(nota):
    if nota >= 90:
        return "Parabéns, você tirou A!"
    elif nota >= 80:
        return "Muito bem, você tirou B."
    elif nota >= 70:
        return "Bom trabalho, você tirou C."
    elif nota >= 60:
        return "Fique atento, você tirou D."
    else:
        return "Estude um pouco mais, você tirou F."

# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno: "))
classificacao = classificar_nota(nota)
print(classificacao)
#----------------------------------------------

# Missão 4: Restaurando a Identificação de Números ⚖️
# Cria um programa para somar dois números
def somar_numeros(num1, num2):
    return num1 + num2

# Solicita dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = somar_numeros(num1, num2)
print(f"A soma dos dois números é: {soma}")
#----------------------------------------------

# Missão 5: Recuperando o Cofre de Segurança 🔒
# Verifica se a senha fornecida está correta
def verificar_senha(senha_digitada):
    senha_correta = "Python123"
    if senha_digitada == senha_correta:
        return "Senha correta! Acesso concedido."
    else:
        return "Senha incorreta. Acesso negado."

# Solicita a senha
senha_digitada = input("Digite a senha: ")
verificacao_senha = verificar_senha(senha_digitada)
print(verificacao_senha)
#----------------------------------------------

# Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
# Exibe os números de 1 a 10 usando um loop while
def contar_numeros():
    numero = 1
    while numero <= 10:
        print(numero)
        numero += 1

print("Números de 1 a 10:")
contar_numeros()
#----------------------------------------------

# Missão 7: Organizando a Lista📋
# Organiza a lista de números em ordem crescente
def organizar_numeros():
    numeros = [8, 3, 10, 1, 5]
    numeros.sort()
    print("Lista organizada em ordem crescente:", numeros)

organizar_numeros()
#----------------------------------------------

# Missão 8: Acessando os Registros de Alunos 🏷️
# Exibe o primeiro e o último nome da tupla de alunos
def acessar_registros():
    alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
    print(f"Primeiro nome: {alunos[0]}")
    print(f"Último nome: {alunos[-1]}")

acessar_registros()
#----------------------------------------------

# Missão 9: Calculando Dobro de um Número 🛠️
# Crie uma função que receba um número e retorne o dobro do seu valor
def dobro(numero):
    return numero * 2

# Solicita um número
numero = float(input("Digite um número: "))
resultado_dobro = dobro(numero)
print(f"O dobro de {numero} é {resultado_dobro}.")
#----------------------------------------------

# Missão 10: Contando Letras 🔄
# Crie uma função que receba um nome e diga quantas letras esse nome tem
def contar_letras(nome):
    return len(nome)

# Solicita o nome
nome = input("Digite o nome: ")
quantidade_letras = contar_letras(nome)
print(f"O nome {nome} tem {quantidade_letras} letras.")
#----------------------------------------------
