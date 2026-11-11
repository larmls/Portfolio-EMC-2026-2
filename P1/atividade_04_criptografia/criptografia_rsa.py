"""
Atividade 3 - =Criptografia RSA

Nome: Lara Melissa Pierote
Matricula: 2622082002
Disciplina: Estruturas Matematicas para Computacao
Turno: Matutino


 Comandos usados e suas definições:
    
    
"""



def inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Insira um número inteiro válido.")


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
    


def primo(n):
    """Retorna True se n é primo, testando divisores até a raiz de n."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            print(f"   {n} é divisível por {d} ({n} = {d} * {n // d}), logo não é primo.")
            return False
        d += 1
    print(f"   Nenhum divisor de 2 até {d - 1} divide {n}: {n} é primo.")
    return True


def pedir_primos():
    while True:
        p = inteiro("Digite p (primo > 1): ")
        q = inteiro("Digite q (primo > 1): ")
        if p <= 1 or q <= 1:
            print("p e q devem ser inteiros maiores que 1. Tente novamente.\n")
            continue
        if p == q:
            print("p e q devem ser distintos. Tente novamente.\n")
            continue
        print(f"Verificando se {p} é primo:")
        p_primo = primo(p)
        print(f"Verificando se {q} é primo:")
        q_primo = primo(q)
        if p_primo and q_primo:
            return p, q
        print("Os dois números precisam ser primos. Tente novamente.\n")


def pedir_expoente(phi):
    while True:
        e = inteiro(f"Digite o expoente público e (1 < e < {phi}): ")
        if not (1 < e < phi):
            print(f"e deve estar entre 1 e {phi}. Tente novamente.")
            continue
        mdc, passos = MDC(e, phi)
        print(f"Verificando mdc({e}, {phi}):")
        for p in passos:
            print(f"   {p}")
        print(f"   mdc({e}, {phi}) = {mdc}")
        if mdc == 1:
            return e
        print(f"mdc diferente de 1: {e} não dá. Tente novamente.")


def rsa_parte_A():
    print("=== RSA: parâmetros ===")
    p, q = pedir_primos()
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"\nn = p * q = {p} * {q} = {n}")
    print(f"φ(n) = (p - 1)(q - 1) = {p - 1} * {q - 1} = {phi}")
    e = pedir_expoente(phi)
    print("\n--- Parâmetros RSA ---")
    print(f"p = {p}, q = {q}")
    print(f"n = {n}")
    print(f"φ(n) = {phi}")
    print(f"e = {e}")
    return p, q, n, phi, e


def chaves_rsa(e, phi, n):
    print(f"Procurando d tal que {e} * d ≡ 1 (mod {phi})")
    d = inverso(e, phi)
    print(f"Verificação: {e} * {d} = {e * d} ≡ {(e * d) % phi} (mod {phi})")
    print(f"\nChave pública:  (e, n) = ({e}, {n})")
    print(f"Chave privada:  (d, n) = ({d}, {n})")
    return d


def expoente(base, expoente, n):
    """Calcula base^expoente mod n por quadrados repetidos, reduzindo mod n a cada passo."""
    print(f"   Calculando {base}^{expoente} mod {n}")
    resultado = 1
    b = base % n
    e = expoente
    while e > 0:
        if e % 2 == 1:
            novo = (resultado * b) % n
            print(f"   expoente {e} é ímpar: resultado = {resultado} * {b} mod {n} = {novo}")
            resultado = novo
        else:
            print(f"   expoente {e} é par: resultado continua {resultado}")
        e //= 2
        if e > 0:
            quant = (b * b) % n
            print(f"   base = {b}^2 mod {n} = {quant}")
            b = quant
    print(f"   Resultado: {base}^{expoente} ≡ {resultado} (mod {n})")
    return resultado


def cifrar_decifrar(e, d, n):
    while True:
        M = inteiro(f"Digite o número M (0 <= M < {n}): ")
        if 0 <= M < n:
            break
        print(f"M deve estar entre 0 e {n - 1}. Tente novamente.")

    print("Cifragem: C ≡ M^e (mod n)")
    C = expoente(M, e, n)

    print("\nDecifragem: M' ≡ C^d (mod n)")
    M2 = expoente(C, d, n)

    print(f"Número original M = {M}")
    print(f"Número cifrado C = {C}")
    print(f"Decifragem M' = {M2}")
    if M2 == M:
        print("M' = M: a decifragem recuperou o número original.")
    else:
        print("M' é diferente de M: há algum erro nas chaves.")
    return M


def parte_d(M, n, phi, e, d, p):
    print("Teorema de Euler: se mdc(M, n) = 1, então M^φ(n) ≡ 1 (mod n)")
    mdc, passos = MDC(M, n)
    for passo in passos:
        print(f"   {passo}")
    print(f"mdc({M}, {n}) = {mdc}")

    if mdc == 1:
        print("Condição satisfeita: M é coprimo com n. Aplicando Euler:")
        r = expoente(M, phi, n)
        if r == 1:
            print(f"Confirmado: {M}^{phi} ≡ 1 (mod {n})")
    else:
        print("Condição NÃO satisfeita: M não é coprimo com n, então Euler não aplica.")
        print("Nesse caso o exoente continua valendo.")

    k = (e * d - 1) // phi
    print(f"Como e*d = {e * d} = 1 + {k} * {phi}, vale M^(e*d) = M * (M^φ(n))^{k} ≡ M (mod n).")
    print("É por isso que o deciframentorecupera M (quando M é coprimo com n).")

    print(f"\nPequeno Teorema de Fermat, com módulo primo p = {p}:")
    print("Se p é primo e p não divide a, então a^(p-1) ≡ 1 (mod p)")
    print(f"(Ele não é aplicado ao módulo n = {n}, porque n é composto.)")
    a = inteiro(f"Digite a base a (não divisível por {p}): ")
    if a % p == 0:
        print(f"{p} divide {a}: condição NÃO satisfeita, Fermat não se aplica.")
    else:
        print(f"{p} não divide {a}: condição satisfeita.")
        r = expoente(a, p - 1, p)
        if r == 1:
            print(f"Confirmado: {a}^{p - 1} ≡ 1 (mod {p})")

 
    
# Valores de exemplo para testar as partes B, C e D sem digitar tudo de novo.
# Pode mudar aqui se quiser testar outros primos.
P, Q, E = 11, 13, 7
N = P * Q                 
PHI = (P - 1) * (Q - 1)   


def testar_parte_a():
    rsa_parte_A()


def testar_parte_b():
    print(f"Usando p = {P}, q = {Q}, e = {E}, n = {N}, φ(n) = {PHI}")
    chaves_rsa(E, PHI, N)


def testar_parte_c():
    print(f"Usando e = {E}, n = {N}, d = inverso de {E} mod {PHI}")
    d = inverso(E, PHI)
    cifrar_decifrar(E, d, N)


def testar_parte_d():
    print(f"Usando p = {P}, q = {Q}, e = {E}, n = {N}, φ(n) = {PHI}")
    d = inverso(E, PHI)
    M = inteiro(f"Digite M (0 <= M < {N}): ")
    parte_d(M, N, PHI, E, d, P)


def main():
    while True:
        print("\n=== Testar RSA ===")
        print("1 - Parte A (primos, n, φ(n), e)")
        print("2 - Parte B (chaves)")
        print("3 - Parte C (cifrar e decifrar)")
        print("4 - Parte D (Euler e Fermat)")
        print("5 - Tudo em sequência")
        print("0 - Sair")
        opcao = inteiro("Escolha: ")

        if opcao == 1:
            testar_parte_a()
        elif opcao == 2:
            testar_parte_b()
        elif opcao == 3:
            testar_parte_c()
        elif opcao == 4:
            testar_parte_d()
        elif opcao == 5:
            p, q, n, phi, e = rsa_parte_A()
            print("=== Parte B: chaves ===")
            d = chaves_rsa(e, phi, n)
            print("=== Parte C: cifragem e decifragem ===")
            M = cifrar_decifrar(e, d, n)
            print("=== Parte D: Euler e Fermat ===")
            parte_d(M, n, phi, e, d, p)
        elif opcao == 0:
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()