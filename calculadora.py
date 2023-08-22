operation = input('''
Por favor, digite a operação matemática que você gostaria de completar:
+ para Soma
- para Subtração
* para Multiplicação
/ para Divisão
''')


number_1 = int(input("Insira seu primeiro número: "))
number_2 = int(input("Insira seu segundo número: "))

if operation == '+':
  print('{}+{} = '.format(number_1, number_2))
  print(number_1 + number_2)

elif operation == '-':
  print('{}-{} = '.format(number_1, number_2))
  print(number_1 - number_2)

elif operation == '*':
  print('{}*{} = '.format(number_1, number_2))
  print(number_1 * number_2)

elif operation == '/':
  print('{}/{} = '.format(number_1, number_2))
  print(number_1 / number_2)

else:
  print('0')