# Informa o nome do sistema
print('Software de Folha de Pagamento')

# Solicita o valor hora
vr_hora = float(input('Informe o valor hora : '))

# Solicita a quantidade de horas
qtd_hora = float(input('Digite a quantidade de horas trabalhada : '))

# Calcula o valor bruto
salario_bruto = vr_hora * qtd_hora

# Informa o valor bruto
print(f'O valor bruto do salario é {salario_bruto}')

# Faz as contas com base na taqbela de aliquotas

if salario_bruto >= 4600:
    aliquota_IR = 27
elif salario_bruto > 3700 and salario_bruto < 4600:
    aliquota_IR = 22
elif salario_bruto > 2800 and salario_bruto <= 3700:
    aliquota_IR = 15
elif salario_bruto > 1900 and salario_bruto <= 2800:
    aliquota_IR = 7
else:
    aliquota_IR = 0

# Valor do IR
valor_IR = salario_bruto * (aliquota_IR / 100)

# Valor do sindicato
valor_Sindicato = salario_bruto * (3 / 100)

# Valor FGTS
valor_FGTS = salario_bruto * (11 / 100)

# total de Descontos
total_descontos = valor_IR + valor_Sindicato

# Salario Liquido 
salario_liquido = salario_bruto - total_descontos

# Mostrar os valores
print(f'\n Salario Bruto : ({vr_hora} * {qtd_hora}) : R$ {salario_bruto}')

# Mostrar descontos
print(f'(-) IR ({aliquota_IR}% : R$ {valor_IR})')

# Mostrar valor sindicato
print(f'(-) Valor sindicato (3%): {valor_Sindicato}')

# Mostrar FGTS
print(f'FGTS (11%) : R${valor_FGTS}')

# Total de descontos
print(f'Total de descontos : {total_descontos}')

# Salario liquido
print(f'O salario liquido é {salario_liquido}')