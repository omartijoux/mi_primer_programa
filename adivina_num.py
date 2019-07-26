

number_to_guess = 2
counter = 0


while (counter < 5):
    user_number = int(input("Adivina un numero: "))
    if user_number == number_to_guess:
        print("Felicidades, adivinaste")
    elif user_number != number_to_guess & counter < 5:
        print("No es el numero")
        counter = counter + 1
    elif user_number != number_to_guess & counter == 5:
        print("Te quedaste sin oportunidades.")