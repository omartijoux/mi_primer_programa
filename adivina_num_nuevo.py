
num_to_guess = int(input("Que numero deseas adivinar? "))
num_selected = 0
while num_selected != num_to_guess:
    num_selected = int(input("Adivina el numero: "))
    if num_selected != num_to_guess:
        print("Intenta de nuevo")

print("Felicidades, adivinaste!")