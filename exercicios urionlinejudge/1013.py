# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. 

linha = input()
a,b,c = map(int, linha.split(" "))
# linha.split separa a posição da string quando encontra o caractere colocado entre parentes

resultado = (a + b + abs(a-b))/2

if(resultado > c):
    print("%d eh o maior" % (resultado))
else:
    print("%d eh o maior" % (c))