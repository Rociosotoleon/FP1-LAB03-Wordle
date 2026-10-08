from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    if len(cadena) == 5 and cadena.isalpha():
        return True
    else:
        return False

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """ 
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """

    diferencia_minutos = (fin - inicio).total_seconds() / 60
    diferencia_segundos = (fin - inicio).total_seconds() % 60
    return (diferencia_minutos, diferencia_segundos)



def quitar_letra(cadena, caracter):
    res = ""
    caracter_quitado = False 
    for c in cadena:
        if c != caracter:
            res += c
        elif caracter_quitado == True:
            res += c
        else:
            caracter_quitado = True
    return res


def marcar_verdes(palabra_secreta, intento):
    verdes = ""
    restantes = ""
    for i in intento:
        if intento.find(i) == palabra_secreta.find(i):



# TODO: Escribe la cabecera completa e implementa la función marcar_amarillos

def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """
    # TODO: Implementa esta función
    return "_____"  # Elimina esta línea cuando la implementes


