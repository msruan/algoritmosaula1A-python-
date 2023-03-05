#21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).

#entrada
far = float(input('Digite a temperatura em graus fahrenheit:'))

#proces
celsius = (far - 32) * 1.8

#saída
print('Essa temperatura em celsius corresponde a',celsius,'ºC')