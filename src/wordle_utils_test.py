from wordle_utils import es_palabra_valida
from wordle_utils import quitar_letra

def test_es_palabra_valida():
    print("Probando es_palabra_valida...")
    assert es_palabra_valida("casar") == True
    assert es_palabra_valida("casa") == False
    assert es_palabra_valida("casarr") == False
    assert es_palabra_valida("c4sar") == False
    assert es_palabra_valida("casa ") == False
    assert es_palabra_valida(" casa") == False
    assert es_palabra_valida("CASAR") == True

def test_quitar_letra():
    print("Probando es_palabra_valida...")
    assert quitar_letra("casar", "a") == "csar"
    assert quitar_letra("casar", "c") == "asar"
    assert quitar_letra("casar", "r") == "casa"
    assert quitar_letra("casar", "z") == "casar"
    assert quitar_letra("aaaaa", "a") == "aaaa" 

    


#test_es_palabra_valida()
test_quitar_letra()
print("✅Todas las pruebas pasaron correctamente.")