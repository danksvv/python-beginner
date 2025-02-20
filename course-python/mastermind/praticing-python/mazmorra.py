import time
import os
import sys
import random


def sleepAndClear():
    time.sleep(2)
    os.system('clear')


def printer(message):
    for caracter in message:
        sys.stdout.write(caracter)  # Escribe sin hacer un salto de línea
        sys.stdout.flush()  # Forzar la impresión inmediata
        time.sleep(0.05)  # Pequeña pausa de 50ms entre caracteres
    print()  # Para el salto de línea final


def keySilver():
    printer("Has elegido la llave plateada.")
    sleepAndClear()
    print("""

                       ↑↑↑
                     ↑    ↑↑
                       ↑ ↑↑↑
                     ↑   ↑↑↑
                      ↑ ↑↑↑
                      ↑↑↑↑↑
                  ↑↑    ↑↑↑ ↑↑↑
                        ↑ ↑↑↑↑↑↑↑
                ↑    ↑↑  ↑  ↑↑↑↑↑↑
                  ↑↑↑  ↑   ↑ ↑↑  ↑
               ↑ ↑↑↑↑↑↑ ↑ ↑↑↑↑↑ ↑↑
               ↑ ↑↑↑↑↑↑↑↑↑↑↑↑↑↑ ↑↑↑
               ↑   ↑↑↑↑↑↑↑↑↑↑↑↑   ↑
                 ↑↑  ↑  ↑↑  ↑ ↑↑↑
            ↑↑↑↑   ↑↑↑↑↑↑↑↑↑↑   ↑↑ ↑↑↑
            ↑↑↑↑↑↑↑↑↑    ↑↑↑↑     ↑↑↑↑
              ↑↑↑↑↑↑↑↑↑↑↑↑ ↑↑↑   ↑↑↑
                  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑

            """)

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    monje = "Al abrir la puerta, te encuentras con un monje. \n" \
        "El monje te felicita por escoger la llave correcta, ya que todo no es oro todo lo que reluce. \n" \
        "Y a continuacion te lanza la siguiente pregunta : \n" \
        "¿Cual es el resultado de la siguiente operacion? \n" \

    printer(monje)

    print(f"{num1} + {num2} = ?")

    respuesta = int(input(">>> "))

    if respuesta == num1 + num2:
        printer("¡Respuesta correcta! Has superado el desafío.")

        monje = "El monje te felicita por resolverlo tan rapido. \n" \
            "Antes de irte te regala un reloj y te da un consejo, \n" \
            "El tiempo es oro, no lo desperdicies.Utilizalo sabiamente! \n" \
            "Y a continuacion desaparece dejando detras de el la salida a la mazmorra. \n"

        printer(monje)
        print("""

        ↑↑↑↑↑↑↑↑↑              ↑↑↑↑↑↑↑↑↑
       ↑↑↑↑↑↑↑↑↑↑↑↑↑        ↑↑↑↑↑↑↑↑↑↑↑↑↑
      ↑↑↑↑↑↑↑↑↑↑↑↑↑↑        ↑↑↑↑↑↑↑↑↑↑↑↑↑↑
     ↑↑↑↑↑↑↑↑↑↑↑↑↑            ↑↑↑↑↑↑↑↑↑↑↑↑↑
     ↑↑↑↑↑↑↑↑↑↑  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑  ↑↑↑↑↑↑↑↑↑↑
     ↑↑↑↑↑↑↑ ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
     ↑↑↑   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑  ↑↑↑↑
         ↑↑↑↑↑↑↑↑      ↑↑     ↑↑↑↑↑↑↑↑
        ↑↑↑↑↑↑↑        ↑↑        ↑↑↑↑↑↑
       ↑↑↑↑↑↑          ↑↑          ↑↑↑↑↑
       ↑↑↑↑↑           ↑↑           ↑↑↑↑↑
      ↑↑↑↑↑            ↑↑            ↑↑↑↑
      ↑↑↑↑↑            ↑↑            ↑↑↑↑↑
      ↑↑↑↑            ↑↑↑↑↑↑↑↑↑↑     ↑↑↑↑↑
      ↑↑↑↑            ↑↑↑            ↑↑↑↑↑
      ↑↑↑↑↑                          ↑↑↑↑↑
      ↑↑↑↑↑↑                        ↑↑↑↑↑
       ↑↑↑↑↑↑                      ↑↑↑↑↑↑
        ↑↑↑↑↑↑                    ↑↑↑↑↑↑
         ↑↑↑↑↑↑↑               ↑↑↑↑↑↑↑
           ↑↑↑↑↑↑↑↑↑       ↑↑↑↑↑↑↑↑↑↑
            ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
            ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
            ↑↑↑↑     ↑↑↑↑↑↑     ↑↑↑↑

            """)
        sleepAndClear()
    else:
        printer("Respuesta incorrecta. El monje te lanza un hechizo y desapareces.")
        sleepAndClear()


sleepAndClear()
print("""


▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖    ▗▖ ▗▖ ▗▄▖ ▗▄▄▖ ▗▄▄▖ ▗▄▄▄▖ ▗▄▖ ▗▄▄▖
▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌       ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌  █  ▐▌ ▐▌▐▌ ▐▌
▐▌ ▐▌▐▛▀▀▘▐▌   ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘    ▐▌ ▐▌▐▛▀▜▌▐▛▀▚▖▐▛▀▚▖  █  ▐▌ ▐▌▐▛▀▚▖
▐▙█▟▌▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖    ▐▙█▟▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▗▄█▄▖▝▚▄▞▘▐▌ ▐▌


    """)
sleepAndClear()


instruccion = "Dentro de esta mazmorra, deberás elegir entre dos caminos. \n" \
    "Cada camino te llevará a un destino diferente. \n" \
    "¿Estás listo para comenzar? (s/n): "

printer(instruccion)

respuesta = input(">>> ")

if respuesta.lower() == "s":
    printer("¡Muy bien! Comencemos...")
    sleepAndClear()
    desafio01 = "Debes elegir entre dos caminos: el camino de la izquierda o el camino de la derecha. \n" \
        "¿Cuál eliges? (i/d): "

    printer(desafio01)

    camino = input(">>> ")

    if camino.lower() == "i":
        printer("Has elegido el camino de la izquierda.")
        sleepAndClear()
        print("""

                      ---...
                    ---++-----
                  ...-##++##+---
                 ...##+----+##---.
                .--##--------##..-
                ..+#----------#+-..
                ..#+-----------#--.
                --#---++--++---#--.
                --#------------#--.
               .--#----------+-#--
                .-#----------#-#-.
                ..#------------#..
                --#------------#--
                .-#-++++++++++-#--
                .-#------------#-.
                --#------------#--
                --#++++++++++++#--

        """)

        puerta = "En este camino te encuentras con una puerta cerrada. \n" \
            "Debes elegir entre dos llaves: la llave dorada o la llave plateada. \n" \
            "¿Cuál eliges? (d/p): "

        printer(puerta)

        llave = input(">>> ")

        if llave.lower() == "d":
            printer("Has elegido la llave dorada.")
            sleepAndClear()
            print("""

  #
             +
  %   =               +:
 +   : *   .             @  -
------*.                     *-
-----------------::=+---==----%
------------------------------
------------------------:::::
------------+--:::::::::::::@
---------:::::::::::::::::::
------::::::-::::::::::::::
-----::::::--::::::::::+
----::::::-=:::::::@
----::::::-:::::::
----:::::::::::::
----:::::::::::::
---:-#::::::::::.
---:--=:::::::::@
---::--:::::::::
---:--::::::::@
--::-#::::::::
--:::::::::::@
--::::::::::-

    """)
            precipicio = "Al abrir la puerta, te encuentras con un precipicio. \n" \
                "acabas de caer al vacio, lo siento tu recorrido termina aqui! \n" \

            printer(precipicio)

        elif llave.lower() == "p":
            keySilver()
        else:
            printer(
                "No has elegido ninguna de las dos llaves. Tu recorrido termina aquí.")

    elif camino.lower() == "d":
        printer("Has elegido el camino de la derecha.")
        sleepAndClear()
        print("""


                ███████▓██▓███████
            ████░░░░░░░░██░░░░░░░░████
          ██░░░░░░░░▓████████▓░░░░░░░░██
        ██░░░░░▓███▓▓▓▓▓▓▓▓▓▓▓▓███▓░░░░░██
      ████░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒░░████
    ██░░░░███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███░░░░██
   ██░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██
  ██░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░██
 ██░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█░░░░██
 █▒░░░█▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████▒▒▓▓▓▓▓▓▓▓▓▓▓▓█░░░▒█
██░░░██▓▓▓▓▓▓▓▓▓▓▒▒██        ██▒▒▓▓▓▓▓▓▓▓▓▓██░░░██
██░░░█▓▓▓▓▓▓▓▓▓▓▓▒██          ██▒▓▓▓▓▓▓▓▓▓▓▓█░░░██
█▒░░░█▓▓▓▓▓▓▓▓▓▓▒▒█▓          ▓█▒▒▓▓▓▓▓▓▓▓▓▓█░░░▒█
██████▓▓▓▓▓▓▓▓▓▓▒▒█▒          ▒█▒▒▓▓▓▓▓▓▓▓▓▓██████
█░░░░▓▓▓▓▓▓▓▓▓▓▓▒▒█▒          ▒█▒▒▓▓▓▓▓▓▓▓▓▓█░░░░█
█░░░░█▓▓▓▓▓▓▓▓▓▓▒████████████████▒▓▓▓▓▓▓▓▓▓▓█░░░░█
█░░░░█▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓█░░░░█
█░░░░█▓▓▓▓▓▓▓▓██░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓█░░░░█
█░░░░█▓▓▓▓▓▓██░░░░░░░░░░██░░░░░░░░░░██▓▓▓▓▓▓█░░░░█
█░░░░█▓▓▓▓██▒░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓▓▓█░░░░█
█░░░░█▓▓▓██░░░░░░░░░░░░░██░░░░░░░░░░░░░██▓▓▓█░░░░█
█░░░░█▓██░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░██▓█░░░░█
█░░░░██▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██░░░░█


    """)
        tunel = "has llegado a un tunel con poca luz, en medio se encuentra una caja \n" \
            "dicha caja se encuentra con telaranas y polvo, ¿la abres? (s/n): "

        printer(tunel)

        caja = input(">>> ")

        if caja.lower() == "s":
            printer("La caja contiene una moneda de plata. la cual te dara suerte.")
            sleepAndClear()
        else:
            printer("Decides no abrir la caja y sigues tu camino.")
            sleepAndClear()

        printer("Al final del tunel te encuentras con un rio subterraneo. \n"
                "en el cual se encuentra un barquero, el cual te ofrece cruzar el rio. \n"
                "¿Aceptas? (s/n): ")

        respuesta = input(">>> ")

        if respuesta.lower() == "s":
            printer("Aceptas la oferta del barquero y subes a su barca.")
            sleepAndClear()
            print("""

                       ██████████
                        ██▓▓▓▓▓▓██
                        ██▓▓▓██████
                        █▓▓▓▓██  █          █
                        █▓▓▓▓▓████         █▒██
                        ██▓▓▓▓▓▓▓██     ███▒▒█       ███▒▓▓██
                         █▓▓▓▓▓▓██    ████▒▒██       █▒▒▒▓▓▓██
                        █▓▓▓▓▓▓▓▓██▓▓▓▓██▒████      ██▒▒██▓▓██
                       ██▓██▓▓█▓▓▓█▓▓▓██▒██▓▓█       ██▒▓██▓██
                       ██▓▓▓▓▓██▓▓█████▒███▓▓█       ██▒██▓██
                       ██▓█▓▓▓█▓▓▓████▒██ ████       █▒▓▓█▓██
                       █▓▓█▓▓██▓▓▓███▒██   ███      ▒▒▒▓▓███
                      ██▓██▓▓▓███▓██▒██           ██▒███▓▓███
                      ██▓██▓▓▓▓▓▓█████           █▓▒▒█████████
                      ██▓▓▓██▓▓▓▓▓▓██         ███▒▒▒▒█▒▒▒▒▒▒██
                      █▓▓▓▓▓▓██▓▓▓▓▓█       ███▒▒▒▒▒▒█▒████▒██
                     ██▓▓▓▓▓▓▓██▓▓▓███  ████▒▒▒▒▒▒▒▒▓██▓▒▒▒██
                    ██▓▓▓▓▓▓▓█▒██▓▓█████▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓███
                   ██▓▓▓▓▓▓██▒▒██▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██
                 ██▓▓▓▓▓███▒▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██
            █▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██
            █▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██
            █▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓██
            █▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██
            █▒▒▒▒▒███▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓███
            █▒▒▒▒▒▒▒▒███▒▒██▒▒▒▒▒▓▓▓▓▓▓▓▓▓████
            ██████████████████████████████

            """)

            printer("Cruzas el rio y llegas al otro lado. \n"
                    "El barquero te indica el camino a seguir y esta a punto de irse. \n"
                    "En agradecimiento le das las gracias, y te quedas pensando si darle la moneda de plata. \n"
                    "¿Qué decides hacer, darle la moneda? (s/n): ")

            respuesta = input(">>> ")

            if respuesta.lower() == "s":
                printer("Le das la moneda de plata al barquero.")
                sleepAndClear()
                print("""
                                              
                                              
                                              
                                              
         ██████                               
      ████████████                            
    ████████████████                          
   ██████████████████████████████████████     
   ███    █████████████████████████████████   
  ███     █████████████████████████████████   
   ███    ████████████████████████████████    
   ███████████████████████   █    █    █      
    ████████████████                          
      ████████████                            
         ██████                               
                                              
                                              
                                              
                                              
            """)

                printer("El barquero te agradece y a cambio te da una llave. \n"
                        "Sigues tu camino y te adentras en la mazmorra.")
                printer("Al final del camino te encuentras con una puerta cerrada. \n"
                        "Decides usar la llave que te dio el barquero. \n")
                keySilver()
            else:
                printer("Decides no darle la moneda de plata al barquero. \n"
                        "El barquero se va y tu sigues tu camino.")
                sleepAndClear()
                print("""
                              ░░░   ░                                    
                        ▒▒░░                                         
                       ▒▒▒░░░                                        
                       ▒░▒▒ ░░      ░                                
                       ▒▒▒▒▒░▒▒▒                                     
                   ░  ▒░ ░░▒░ ▒▒▒░░░                                 
                  ░  ░ ▒▒▒▒▒▒░░░                                     
                  ░▒░  ▒▒░░░  ░▒░░                                   
                  ░ ▒ ░▒▒░░░▒░▒░                                     
                   ░░▒▒░▒▒▒░░                                        
                     ░▒▒░░░  ░░░                                     
                       ▒▒▒▒▒░░▒▒ ░ ░▒░                               
                 ░▒▒▒▒▒▒▒▒▒▒▒░ ▒▒ ░ ░▒   ░░                          
              ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ░  ▒ ░                                
            ░░░░░░▒░░▒▒▒▒▒▒░▒░░▒▒▒░▒▒▒▒░ ▒░                          
             ▒░▒▒░▒▒▒▒  ▒▒▒░▒ ░░ ▒ ░ ░▒ ░▒░                          
           ░░  ░░▒▒░ ▒▒▒░▒▒░░░░ ░▒▒ ▒▒░  ▒▒░                         
           ▒░░   ▒░░▒░▒▒ ░▒░░░░ ░░  ▒ ░     ▒                        
              ░▒░ ▒▒░░▒▒▒▒▒░░░░▒▒▒▒░░▒░      ▒                       
                 ▒░  ▒▒░░ ▒░▒░░▒▒▒░  ░░        ░                     
                  ▒▒░     ░▒░░ ▒▒▒▒▒ ░          ░                    
                  ▒▒▒ ▒░░ ░▒░░░▒▒▒▒▒░░            ░                  
                   ░░   ▒▒░▒░░░ ▒▒▒▒░              ░░░░              
                  ░  ░   ░▒▒▒ ░ ░▒▒▒▒░░              ▒░▒░            
                      ░░      ░ ░░░░░ ░░░▒▒░░      ░▒▒░▒             
                ░     ░    ░  ░                  ░░░░░░▒▒            
                ░░░                                                  
              ░░    ░░                                               
                 ░░ ░                                                
                   ▒
                """)
                printer("Llegas al final del camino y te encuentras con una puerta cerrada. \n"
                        "Al no tener la llave para abrir la puerta, te quedas esperando eternamente a que regrese el barquero.")

else:
    printer("¡Hasta la próxima!")
    sleepAndClear()
