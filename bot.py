def responder_bot(mensaje):
    mensaje = mensaje.lower()

    if 'hola' in mensaje:
        return 'Hola, bienvenido(a) a VilSof'

    elif 'precio' in mensaje or 'plan' in mensaje:
        return 'BotMini $150.000, BotMid $300.000, BotBig $450.000'

    elif 'asesor' in mensaje:
        return 'Muy bien, te derivo con humano, te recuerdo que nuestro horario de atencion es de lunes a viernes, 9 a 18 h'

    else:
        return 'no te entendí, escribe hola, precio o asesor'


print(responder_bot('Hola, quiero cotizar un bot'))
print(responder_bot('Cuánto cuestan los planes?'))
print(responder_bot('quiero un ASESOR'))
print(responder_bot('blablabla'))