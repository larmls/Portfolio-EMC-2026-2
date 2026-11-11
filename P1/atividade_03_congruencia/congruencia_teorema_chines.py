"""
Atividade 3 - Congruência e Teorema Chinês

Nome: Lara Melissa Pierote
Matricula: 2622082002
Disciplina: Estruturas Matematicas para Computacao
Turno: Matutino


 Comandos usados e suas definições:
    
    
"""

from os import name


def inteiro(mensagem):
    """  Função para ler um número inteiro do usuário. """
    while True:
        try:
            return int(input(mensagem))
        except:
            print("Insira um número inteiro válido.")
            
def  modulo():
    while True:
        n = inteiro("Digite o valor de n (n > 0): ")
        if n > 0:
            return n
        print("O valor de n deve ser maior que 0. Tente novamente.")

def congruencia(a, b, n):
    """ Função para verificar se a é congruente a b módulo n. """
    diferenca = a - b
    resto = diferenca % n
    
    print(f"Passo 1: diferença entre a e b = {a} - {b} = {diferenca}")
    print(f"Passo 2: resto de {diferenca} dividido por {n} = {resto}")
    
    if resto == 0:
        print(f"Passo 3: o resto é zero, então {n} divide a diferenca {diferenca}.")
        print(f"conclui-se que {a} \u2261 {b} (mod {n})")
        return True
    
    print(f"Passo 3: o resto não é zero, então {n} não divide a diferenca {diferenca}.")
    print(f"conclui-se que {a} NÃO É CONGRUENTE A {b} (mod {n})")
    return False
    
def parte1():
    print("Verificação de Congruência")
    a = inteiro("Digite o valor de a: ")
    b = inteiro("Digite o valor de b: ")
    n = modulo()
    
    congruencia(a, b, n)
    
    
    


def MDC(a, b):
    passo = []
    dividendo = a
    divisor = b
    while divisor != 0:
        quociente = dividendo // divisor
        resto = dividendo % divisor
        passo.append(f"{dividendo} = {divisor} * {quociente} + {resto}")
        dividendo = divisor
        divisor = resto
    resultado = dividendo
    return resultado, passo



def co_primos(modulos):
    """Retorna verdadeiro se todos os modulos forem coprimos entre si, caso contrário retorna falso."""
    for i in range(len(modulos)): #len retorna o tamanho da lista
        for j in range(i + 1, len(modulos)):
            print(f"Verificando se {modulos[i]} e {modulos[j]} são coprimos")
            
            mdc, passo = MDC(modulos[i], modulos[j])
            for p in passo:
                print(f"  {p}")
            print(f"MDC({modulos[i]}, {modulos[j]}) = {mdc}")
            
            if mdc != 1: #ESSA ! = significa diferente
                   print(f"{modulos[i]} e {modulos[j]} não são coprimos.")
                   return False
    
    print("Todos os modulos são coprimos entre si.")
    return True


def inverso(a, n):
    """Função para calcular o inverso de a módulo n usando o algoritmo estendido de Euclides."""
    a = a % n  # Reduz a para o intervalo [0, n-1]
    r0, r1 = n, a
    t0, t1 = 0, 1
    print(f"Calculando o inverso de {a} módulo {n}")
    
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
        print(f"q = {q}, resto = {r1}, t = {t1}")
    
    if r0 != 1:
        print(f" mdc({a}, {n}) = {r0} não é 1, então {a} não tem inverso módulo {n}.")
        return None
    
    x = t0 % n
    print(f"O inverso de {a} módulo {n} é {x}.")
    print(f"Verificação: {a} * {x} = {a * x} \u2261 {(a * x) % n} (mod {n})")
    return x
    

def teorema_chines(restos, modulos):
    """Funçao para resolver o sistema de congruências usando o Teorema Chinês do Resto."""
    k = len(modulos) # número de congruências
    
    N = 1
    for n in modulos:
        N *= n  # Calcula o produto de todos os modulos
    produto = "*".join(str(n) for n in modulos) #aqui é só para printar o produto de todos os 
    print(f"Passo 1: N = {produto} = {N}")
    
    soma = 0
    for i in range(k):
        ai, ni = restos[i], modulos[i]
        Ni = N // ni  # Calcula N_i = N / n_i
        print(f"Equação {i + 1}: x \u2261 {ai} (mod {ni})")
        print(f" N{i + 1} = {N} / {ni} = {Ni}")
        
        inv = inverso(Ni, ni)  # Calcula o inverso de N_i módulo n_i
        termo = ai * Ni * inv
        print(f"Termo {i + 1} = {ai} * {Ni} * {inv} = {termo}")
        soma += termo  # Soma os termos para obter a solução
        
    x0 = soma % N  # A solução é x0 = soma mod N
    print(f"Soma dos termos = {soma}")
    print(f"X0 = {soma} mod {N} = {x0}")
    
    print("\nVerificação:")
    certo = True
    for i in range(k):
        resto = x0 % modulos[i]
        esperado = restos[i] % modulos[i]
        print(f" {x0} mod {modulos[i]} = {resto}, esperado = {esperado}")
        if resto != esperado:
            certo = False
            
    if certo:
        print(f"A solução de x0 = {x0} satisfaz todas as congruências.")
    print(f"Solução: x = {x0} + t * {N}, com t inteiro.")
    return x0




def main():
    print("=== Teorema Chinês do Resto ===")

    while True:
        k = inteiro("Quantas congruências (3 ou 4)? ")
        if k in (3, 4):
            break
        print("Escolha 3 ou 4.")

    restos = []
    modulos = []
    for i in range(1, k + 1):
        print(f"\nEquação {i}: x ≡ a{i} (mod n{i})")
        a = inteiro(f"   Digite a{i}: ")
        while True:
            n = inteiro(f"   Digite n{i} (n{i} > 0): ")
            if n > 0:
                break
            print("   O módulo deve ser positivo.")
        restos.append(a)
        modulos.append(n)

    print("\nVerificando se os módulos são coprimos dois a dois:")
    if not co_primos(modulos):
        print("O sistema está fora das condições previstas para esta atividade.")
        return

    teorema_chines(restos, modulos)


if __name__ == "__main__":
    main()