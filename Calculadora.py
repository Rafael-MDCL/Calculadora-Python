import math

def  calculadora():
    while True:
        print('Calculadora Simples')
        print()
        print('1. Soma')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('5. Potenciação')
        print('6. Raiz Quadrada')
        print('7. Sair')
        operacao = input("Selecione uma opção ou '7' para sair:")

        if operacao == '5':
            print('Obrigado por utilizar minha primeira calculador simples')
            break



        if operacao != '6':
            numero_1= float(input('Digite o numerador:'))
            numero_2= float(input('Digite o denominador:'))
        else:
            numero_1= float(input('Digite a raiz quadrada do número:'))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print('o resultado da soma é:', resultado)
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print('o resultado da subtração é:', resultado)
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print('o resultado da multiplicação é:', resultado)
        elif operacao == '5':
            resultado = numero_1 ** numero_2
            print('o resultado da potenciação é:', round(resultado, 2))
        elif operacao == '6':
            resultado = math.sqrt(numero_1)
            print('o resultado da sua radiciação é:', round(resultado, 2))
        else:
            if numero_2 == 0:
                print('divisões por Zero são impossíveis. Tente novamente')
                continue
            else:
                resultado = numero_1 / numero_2
                print('o resultado da divisão é:', round(resultado, 2))


        if operacao not in ['1','2','3','4','5','6','7']:
            print('Opção inválida! Tente novamente.')
            continue



calculadora()