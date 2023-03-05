#entrada
salario = float(input('Insira o valor em reais:'))

#process
por_cem = salario / 100
aumento = salario + por_cem * 25

#saída
print("Com o aumento, o salário passa a ser de",aumento,'reais')
