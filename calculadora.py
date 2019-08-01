
operacion_seleccionada = input("Que operacion quieres hacer? (Sumar, Restar, Multiplicar o Dividir): ")

primer_num = int(input("Dame tu primer numero: "))

segundo_num = int(input("Dame tu segundo numero: "))


if operacion_seleccionada == "Sumar":
    resultado = primer_num + segundo_num
    print("El resultado de {} {} + {} es {}".format(operacion_seleccionada,primer_num, segundo_num, resultado))

elif operacion_seleccionada == "Restar":
    resultado = primer_num - segundo_num
    print("El resultado de {} {} - {} es {}".format(operacion_seleccionada, primer_num, segundo_num, resultado))

elif operacion_seleccionada == "Multiplicar":
    resultado = primer_num * segundo_num
    print("El resultado de {} {} * {} es {}".format(operacion_seleccionada, primer_num, segundo_num, resultado))

elif operacion_seleccionada == "Dividir":
    resultado = primer_num / segundo_num
    print("El resultado de {} {} / {} es {}".format(operacion_seleccionada, primer_num, segundo_num, resultado))