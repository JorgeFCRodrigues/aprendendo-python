# Crie um script Python que leia dois números e
# tente mostrar a soma entre eles

# ERRADO
# valor1 = input('Informe o primeiro valor: ')
# valor2 = input('Informe o segundo valor: ')

# soma = valor1 + valor2

# print('O resultado da soma dos valores é: ', soma)

# CORRETO

# valor1 = int(input('Informe o primeiro valor: '))
# valor2 = int(input('Informe o segundo valor: '))

# soma = valor1 + valor2

# print('O resultado da soma dos valores é: {}'.format(soma))

# Desafio

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))

soma = valor1 + valor2

print('A soma entre {} + {} resulta em: {}'.format(valor1, valor2, soma))
