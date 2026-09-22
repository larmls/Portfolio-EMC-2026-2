"""
Atividade 2 - Divisibilidade

Nome: Lara Melissa Pierote
Matricula: 2622082002
Disciplina: Estruturas Matematicas para Computacao
Turno: Matutino


 Comandos usados e suas definições:
    Append adiciona item ao final da lista, construindo a lista
    
"""

def ler_inteiro_positivo(numero):
    while True:
        entrada = input(numero)
        if entrada.isdigit(): #verifica se a entrada é um número inteiro positivo
            return int(entrada)
        else:
            print("Entrada inválida. Digite um número inteiro positivo.")
            


def divisao_inteira(numero_a, numero_b):
    return numero_a // numero_b

def resto_divisao(numero_a, numero_b):
    return numero_a % numero_b





def MDC(a, b):
    passo = []
    dividendo = a
    divisor = b
    
    while divisor != 0: #repete enquando o resto for diferente de zero
        
        # aqui é o algoritmo de Euclides para calcular o MDC
        quociente = dividendo // divisor
        resto = dividendo % divisor
        passo.append(f"{dividendo} = {divisor} * {quociente} + {resto}")
        dividendo = divisor
        divisor = resto
        
    MDC = dividendo
    return MDC, passo



        
        
        
"""Apenas aplicar a fórnula do MMC, que é o produto dos dois números dividido pelo MDC"""
def MMC(a, b, MDC):
    return (a * b) // MDC

resultado_mdc, resultado_passo = MDC(48, 18)
resultado_mmc = MMC(48, 18, resultado_mdc)

        

def main():
    
    print("================================================================")
    print("Atividade 2 - Divisibilidade")
    print("Nome: Lara Melissa Pierote")
    print("Matricula: 2622082002")
    print("Disciplina: Estruturas Matematicas para Computacao")
    print("Turno: Matutino")
    print("================================================================")
    
    numero_a = ler_inteiro_positivo("Digite o primeiro número inteiro positivo: ")
    numero_b = ler_inteiro_positivo("Digite o segundo número inteiro positivo: ")
    
    
    div_resultado = divisao_inteira(numero_a, numero_b)
    mod_resultado = resto_divisao(numero_a, numero_b)
    print(f"Divisão inteira de {numero_a} DIV {numero_b} = {div_resultado}")
    print(f"Resto da divisão de {numero_a} MOD {numero_b} = {mod_resultado}")
    
    MDC_resultado, passo = MDC(numero_a, numero_b)
    print("================================================================")
    print("Teorema de Euclides - MDC: ")
    for passo in passo:
        print(passo)
        
        
    print()
    MMC_resultado = MMC(numero_a, numero_b, MDC_resultado)
    print(f"MMC de {numero_a}, {numero_b} = {MMC_resultado}")
    print("")   


main()