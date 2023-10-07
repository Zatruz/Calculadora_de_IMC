#O IMC é calculado dividindo o peso (em KG) pela altura ao quadrado (em metros).
print('Iniciando a Calculadora de Índice de Massa Corporal (IMC).')

nome = str(input('Informe o seu nome: '))
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)

print(f'{nome}, seu IMC é {imc:.2f} e é considerado: ')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 24.9:
    print('Peso Normal')
elif 25 <= imc < 29.9:
    print('Sobrepeso')
elif 30 <= imc < 34.9:
    print('Obesidade de Grau I')
elif 35 <= imc < 39.9:
    print('Obsidade de Grau II')
else:
    print('Obesidade de Grau III ou Mórbida')

#By: Thiago Sampaio -3511168602- /ADS 2ºSem
