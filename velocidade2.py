#6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

import math
#entrada
km_h = float(input('Digite a velocidade em km/h:'))

#proces
m_s = km_h / 3.6

#saída
print('Essa velocidade corresponde a',math.floor(m_s),'m/s')