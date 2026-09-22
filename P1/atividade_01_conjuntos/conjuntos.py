"""
Atividade 1 - Conjuntos

Nome: Lara Melissa Pierote
Matricula: 2622082002
Disciplina: Estruturas Matematicas para Computacao
Turno: Matutino


 Comandos usados e suas definições:
    Split quebra o texto em pedacos usando o espaco 
    Append adiciona item ao final da lista, construindo a lista
    Len() retorna o tamanho da lista (quantidade de elementos)
    Range() repete o for de acordo com a quantidade de elementos do conjunto
    
 
 OBSERVAÇÃO:  
    Quando pedir para digitar os elementos do conjunto, digite todos os elementos separados por espaco.
    
"""

def ler_conjunto (nome_conjunto):

    entrada = input(f"Digite os elementos do conjunto {nome_conjunto}: ")
    elementos = entrada.split()  


    conjunto = []
    for elemento in elementos:
        if elemento not in conjunto:
            conjunto.append(elemento)

    return conjunto




def uniao(conjunto_a, conjunto_b):
    resultado = []
    for elemento in conjunto_a:
        resultado.append(elemento)
        
    for elemento in conjunto_b:
           if elemento not in resultado:
            resultado.append(elemento)
        
    return resultado


""" Aqui será tem apenas um for porque o for vai percorrer o conjunto_a e verificar se cada elemento está no conjunto_b. 
 Se estiver, ele será adicionado ao resultado. """

def intersecao(conjunto_a, conjunto_b):
    resultado = []
    for elemento in conjunto_a:
        if elemento in conjunto_b:
            resultado.append(elemento)
    
    return resultado


""" Aqui a diferença é que tem o NOT IN, ou seja, se o elemento do conjunto_a não estiver no conjunto_b, 
ele será adicionado ao resultado. """

def diferenca(conjunto_a, conjunto_b):
    resultado = []
    for elemento in conjunto_a:
        if elemento not in conjunto_b:
            resultado.append(elemento)
    
    return resultado



""" Aqui iremos trabalhar conjuntos das partes, ou seja, todos os subconjuntos possíveis de um conjunto.
Para isso, utilizamos a fórmula 2^n, onde n é o tamanho do conjunto"""

def conjunto_das_partes(conjunto):
    n = len(conjunto)
    total = 2 ** n
    partes = []

    for i in range(total):
        subconjunto = []
        for j in range(n):
            bit = (i >> j) & 1 
# pra cada número i, ela olha bit por bit, se o bit j estiver concatenado (valendo 1), o elemento A[j] entra no subconjunto daquela vez.
            if bit:                   
                subconjunto.append(conjunto[j])
        partes.append(subconjunto)

    return partes





def particao (conjunto):
    particao = []
    for elemento in conjunto:
        particao.append([elemento])
        
    return particao





def produto_cartesiano(conjunto_a, conjunto_b):
    resultado = []
    for elemento_a in conjunto_a:
        for elemento_b in conjunto_b:
            resultado.append((elemento_a, elemento_b))
    
    return resultado


 
 
 
""" Aqui iremos verificar se o conjunto_a está incluso/contido no conjunto_b, ou seja, se todos os elementos do conjunto_a 
estão no conjunto_b. Para isso, utilizamos um for para ver o conjunto_a e verificar se cada elemento está no conjunto_b.
Se algum elemento não estiver, retornamos False, caso contrário, retornamos True."""
def esta_incluso(conjunto_a, conjunto_b):
    for elemento in conjunto_a:
        if elemento not in conjunto_b:
            return False
        
        
    return True





def main():
    
    print("================================================================")
    print("Atividade 1 - Conjuntos")
    print("Nome: Lara Melissa Pierote")
    print("Matricula: 2622082002")
    print("Disciplina: Estruturas Matematicas para Computacao")
    print("Turno: Matutino")
    print("================================================================")
    
    conjunto_a = ler_conjunto("A")
    conjunto_b = ler_conjunto("B")

    print(f"Conjunto A: {conjunto_a}")
    print(f"Conjunto B: {conjunto_b}")
    
    print()
    print(f"Cardinalidade de A: {len(conjunto_a)}")
    print(f"Cardinalidade de B: {len(conjunto_b)}")
    print(f"Cardinalidade de A u B: {len(uniao(conjunto_a, conjunto_b))}")
    print(f"Cardinalidade de A ∩ B: {len(intersecao(conjunto_a, conjunto_b))}")

    print()
    uniao_resultado = uniao(conjunto_a, conjunto_b)
    print(f"União de A e B: {uniao_resultado}")
    
    print()
    intersecao_resultado = intersecao(conjunto_a, conjunto_b)
    print(f"Interseção de A e B: {intersecao_resultado}")
    
    print()
    diferenca_resultado = diferenca(conjunto_a, conjunto_b)
    print(f"Diferença de A menos B: {diferenca_resultado}")
    
    print()
    diferenca_resultado = diferenca(conjunto_b, conjunto_a)
    print(f"Diferença de B menos A: {diferenca_resultado}")
    
    print()
    partes = conjunto_das_partes(conjunto_a)
    print(f"Conjunto das partes de A: {partes}")
    
    print()
    particao_a = particao(conjunto_a)
    print(f"Partição de A: {particao_a}")
    
    print()    
    produto_ab = produto_cartesiano(conjunto_a, conjunto_b)
    print(f"Produto cartesiano de A X B: {produto_ab}")

    print()
    inclusao_ab = esta_incluso(conjunto_a, conjunto_b)
    print(f"A está incluso em B? {inclusao_ab}")
    
    print()
    inclusao_ab = esta_incluso(conjunto_b, conjunto_a)
    print(f"B está incluso em A? {inclusao_ab}")
    print()
    
    
main()