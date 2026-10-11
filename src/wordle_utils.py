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

    diferencia_minutos = (fin - inicio).total_seconds() // 60
    diferencia_segundos = (fin - inicio).total_seconds() % 60
    return (diferencia_minutos, round(diferencia_segundos, 2))



def quitar_letra(cadena, caracter):
    res = ""
    caracter_quitado = False 
    for c in cadena:
        if c != caracter or caracter_quitado == True:
            res += c
        else:
            caracter_quitado = True
    return res


def marcar_verdes(palabra_secreta, intento):
    verdes = ""
    restantes = ""
    for i in range(5):
        if intento[i] == palabra_secreta[i]:
            verdes += "V"
        else:
            verdes += "_"
            restantes += palabra_secreta[i]

    return verdes, restantes

def marcar_amarillos(intento: str, verdes: str, restantes: str) -> str:
    colores = ""
    for i in range(5):
        if verdes[i] == "V":
            colores += "V"
        elif verdes[i] == "_":
            if intento[i] in restantes: 
                colores += "A"
                restantes = restantes.replace(intento[i], "", 1)
            else:
                colores += "_"
    return colores



def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
        Devuelve:
         Una cadena de 5 caracteres con 'V', 'A' y '_'
     """
    verdes, restantes = marcar_verdes(palabra_secreta, intento)
    colores = marcar_amarillos(intento, verdes, restantes)
    return colores

