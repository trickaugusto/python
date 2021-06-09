# Declaração de função, é usado red
def print_hello_world(qtd):
    for i in range(0, qtd):
        print("Hello world! %d" % i)

print_hello_world(5)

#############################################
########### Função recursiva ################
#############################################
def print_numbers_recursive(number):
    print(number)
    if number <= 0:
        return False
    return print_numbers_recursive(number-1)
#############################################
