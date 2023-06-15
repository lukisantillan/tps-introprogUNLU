from trabajo_seis import (que_tipo_es)
def test_que_tipo_es() :
      print("Testeando Funcion que_tipo_es()... ", end="")
      assert que_tipo_es("texto") == "Enviaste letras"
      assert que_tipo_es("numero1") ==  "Enviaste letras y numeros"
      assert que_tipo_es("222") == "Enviaste numero/s"
      print("Funciona!")
test_que_tipo_es()