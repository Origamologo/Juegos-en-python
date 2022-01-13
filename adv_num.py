#Adivina el numero
import random

print('¡Hola! ¿Cómo te llamas?')
nombre = input()
      
print('Bueno,', nombre, 'estoy pensando un número entre el 1 y 20, ¿puedes adivinarlo? Tienes 6 intentos.')

num = random.randint(1, 20)
intentos = 0
while intentos < 6:
    print('Intenta adivinar el número')
    adv = input()
    while adv.isdigit() == False:
        print('No has introducido un número. Intenta adivinar el número')
        adv = input()
    adv = int(adv)

    intentos += 1

    if adv < num:
        print('Estoy pensando en un número más alto')
    elif adv > num:
        print('Estoy pensando en un número más bajo')
    elif adv == num:
        print('¡Muy bien!', nombre, 'has adivinado el número en', intentos, 'intentos.')
        break
    elif adv != num:
        print('Fallaste. El número que estaba pensando era el', num)

def adv_num():
    num = random.randint(1, 20)
    intentos = 0
    while intentos < 6:
        print('Intenta adivinar el número')
        adv = input()
        while adv.isdigit() == False:
            print('No has introducido un número. Intenta adivinar el número')
            adv = input()
        adv = int(adv)

        intentos += 1

        if adv < num:
            print('Estoy pensando en un número más alto')
        elif adv > num:
            print('Estoy pensando en un número más bajo')
        elif adv == num:
            print('¡Muy bien!', nombre, 'has adivinado el número en', intentos, 'intentos.')
            break
    if adv != num:
        print('Fallaste. El número que estaba pensando era el', num)
    print('¿Quieres jugar de nuevo? (Si / No)')
    jugar = input()
    if jugar == 'Si' or jugar == 'S' or jugar == 's':
        adv_num()

    return None

print('¿Quieres jugar de nuevo? (Si / No)')
jugar = input()
if jugar == 'Si' or jugar == 'S' or jugar == 's':
    adv_num()