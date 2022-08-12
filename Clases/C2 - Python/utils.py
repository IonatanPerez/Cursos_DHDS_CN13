''' Libreria con cosas utiles en desarrollo. '''

def generar_mensaje(titulo, nombre, segundo, apellido, servicio, vencimiento):
    if segundo: # Aca el "" tiene valor False, si hay contenido en el str entonces tiene valor True. Magias de Python que es super flexible.
        nombre_completo = nombre + " " + segundo
    else:
        nombre_completo = nombre
    print (f'{titulo} {nombre_completo} {apellido}, tiene una deuda con {servicio} que vence el {vencimiento}')


def mensaje_simple(nombre, segundo):
    print (f"Hola {nombre} {segundo}, tenemos un mensaje para usted pero se lo vamos a mandar en otro momento que nos cueste menos trabajo.")