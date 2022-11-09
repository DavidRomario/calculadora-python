# criar função receber como parametro um numero, uma operação e outro numero

def calculadora(numero, operacao, numero_dois):
    if operacao == "soma":
        result = numero + numero_dois
        print('soma:', result)
    if operacao == "subtracao":
        result = numero - numero_dois
        print('subtracao:', result)
    if operacao == "divisao":
        result = numero / numero_dois
        print("divisao:", result)
    if operacao == "multiplicacao":
        result = numero * numero_dois
        print("mutiplicacao:", result)


calculadora(1, "soma", 2)
calculadora(2, "subtracao", 1)
calculadora(4, "divisao", 2)
calculadora(3, "multiplicacao", 3)
