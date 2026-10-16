def responder_bot(mensaje):
    mensaje = mensaje.lower()

    if 'cotiz' in mensaje: 
        return 'Hola, bienvenido(a) a VilSof, precios aprox ---> BotMini $150.000, BotMid $300.000, BotBig $450.000'
   
    elif 'hola' in mensaje:
        return 'Hola, bienvenido(a) a VilSof'

    elif 'precio' in mensaje or 'plan' in mensaje:
        return 'BotMini $150.000, BotMid $300.000, BotBig $450.000'

    elif 'asesor' in mensaje:
        return 'Muy bien, te derivo con humano, te recuerdo que nuestro horario de atencion es de lunes a viernes, 9 a 18 h'

    else:
        return 'no te entendí, escribe hola, precio o asesor'


print("Bot de VilSof listo. Escribe 'salir' para terminar.")

while True:
    texto = input("Tú: ")
    if texto.lower() == "salir":
        print("Bot: ¡Hasta luego!")
        break
    print("Bot:", responder_bot(texto))