
# Portfólio de Programação Matemática — Parte 1

Aluno: Lara Melissa Pierote
Matrícula: 2622082002
Disciplina: Estruturas Matemáticas para Computação
Turno: Matutino

# Atividade 1 — Teoria dos Conjuntos

*Arquivo:*
`P1/atividade_01_conjuntos/conjuntos.py`

*Como executar:*
Execute o arquivo `conjuntos.py`. O programa solicita os elementos dos conjuntos A e B.

Exemplo de entrada: 
Conjunto A: 1 2 3 4 5
Conjunto B: 2 4 6 8 10


*O Programa Apresenta*
- União
- Interseção
- Diferenças
- Cardinalidade
- Conjunto das partes
- Partição 
- Produto cartesiano
- Inlusão


# Atividade 2 — Divisibilidade

*Arquivo:*
`P1/atividade_02_divisibilidade/divisibilidade.py`

*Como executar:*
Execute o arquivo `divisibilidade.py`. O programa solicita os elementos positivos inteiros.

Exemplo de entrada:
Primeiro número positivo inteiro: 40
Segundo número positivo inteiro: 10


*O Programa Apresenta*
- DIV
- MOD
- Passo a Passso do teorema de Euclides
- MDC
- MMC


# Atividade 3 — Congruencia e teorema chines do resto

*Arquivo:*
`P1/atividade_03_congruencia/congruencia_teorema_chines.py`

*Como executar:*
Execute o arquivo `congruencia_teorema_chines.py`.

Exemplo de entrada:
a = 23, b = 8, n = 5 | 23 ≡ 8 (mod 5)
a = 17, b = 4, n = 6 | não congruentes (resto 1)
módulos 4, 8, 9 | recusado: 4 e 8 não são coprimos
x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7) e N = 105, x0 = 23


*O Programa Apresenta*
- Congruencia
- MODULO
- MDC
- NUMEROS PRIMOS
- PASSO A PASSO TEOREMA CHINES
- INVERSO


# Atividade 3 — Criptografia RSA

*Arquivo:*
`P1/atividade_03_criptografia/criptografia_rsa.py`

*Como executar:*
Execute o arquivo `criptografia_rsa.py`.

Exemplo de entrada:
p = 11, q = 13, e = 7 e n = 143, φ(n) = 120, d = 103
p = 11, q = 13, e = 6 é recusado: mdc(6, 120) = 6
p = 7, q = 7 é recusado: p e q iguais
M = 11, Euler não se aplica (mdc(11, 143) = 11), mas a decifragem ainda vale com o M


*O Programa Apresenta*
- PARTE A - leitura e verifica se são primos
- PARTE B - calcula o expoente, o inverso e apresenta as chaves
- PARTE C - Cifra e decifra
- PARTE D - teorema de Euler e Fermat


