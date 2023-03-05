#18. Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.(c = 2 * p * r)

import math
#entrada
raio = float(input('Informe o valor do raio da circunferência:'))

#process
comp = raio * 3.14 * 2

#saída
print('O comprimento da circunferência é',math.floor(comp))