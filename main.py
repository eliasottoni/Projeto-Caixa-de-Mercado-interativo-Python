

notaF = []
valF = 0
a = 0
b = 1
d = 0
e = 1

print(f"{'=' * 35 : ^30}")

print(f"{'Bem-vindo ao Mercado Luizinho' : ^35}")

print(f"{'=' * 35 : ^30}")

while True:
    nomeP = input('Digite o nome do produto: ')
    valorP = float(input('Digite o valor do produto: '))
    valF += valorP
    notaF.append(nomeP)
    notaF.append(valorP)
    a += 1
    b += 1

    print(f"{'-' * 35 : ^30}")
    c = input('Deseja adicionar mais produtos? S/N ').upper()
    print(f"{'-' * 35 : ^30}")
    if c == 'N':
        cart = input('[D]inheiro ou [C]artão?: ').upper()[0]
        if cart == 'D':
            tr = int(input('Quanto você recebeu? '))
            break
print(f'o troco é {tr - valF:.2f}')
print(f"{'=' * 35 : ^30}")

g = input('Gerar nota: ')
if g == 'S':
    print(f"{'*=' * 10}")
    print(f'NOTA FISCAL \n')
    cont = len(notaF) / 2
    ci = int(cont)
    for c in range(0, ci):
        print(notaF[d], 'R$', notaF[e])
        d += 2
        e += 2
    print(f'TOTAL: {valF :.2f}')
    print(f"{'*=' * 10}")



