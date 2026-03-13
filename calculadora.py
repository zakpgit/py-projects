def menu(): # Criei uma função onde eu deixo o meu "menu"
    print(""" ==== CALCULADORA ====
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Exponencial
6 - Raiz Quadrada
0 - Sair do programa
""")
    return int(input("Escolha o número equivalente a operação: ")) # O usuário escolhe e retorna no  programa

# Após isso, crio as funções de cálculo

def soma(a, b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b == 0:
        return "Erro. Divisão por zero."
    return a/b

def exponencial(a,b):
    return a**b

def raiz_quadrada(a):
    if a < 0:
        return "Erro. Número negativo."
    return a**0.5


def calculadora():
    while True: # Loop
        operacao = menu() # A função def menu() aparecerá

        if operacao not in [0,1,2,3,4,5,6]: # Se escolher um valor além desses, da erro
            print("Opção inválida. ")
            continue
        if operacao == 0:
            print("Saindo da calculadora...")
            break
        try: # Permite o programa rodar mesmo após o usuário inserir letras

            if operacao in [1,2,3,4,5]:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            elif operacao == 6:
                a = float(input("Digite o número: "))
            if operacao == 1:
                print("Resultado = ", soma(a, b))
            elif operacao == 2:
                print("Resultado = ", subtracao(a, b))
            elif operacao == 3:
                print("Resultado = ", multiplicacao(a, b))
            elif operacao == 4:
                print("Resultado = ", divisao(a, b))
            elif operacao == 5:
                print("Resultado = ", exponencial(a, b))
            elif operacao == 6:
                print("Resultado = ", raiz_quadrada(a))
            else:
                print("Operação inválida. Tente novamente.")
        except:
            print("Digite um número válido.")


calculadora()


