# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
from cryptography.fernet import Fernet

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Resuelvo catpcha tipo reCaptchav2
"""
if module == "nuevoKey":
    # Modulo Crear Key
    ruta = GetParams('content')
    nombrekey = GetParams('idnombrekey')
    
    key = Fernet.generate_key()
    archivo = ruta+"\\"+nombrekey+".key"

    file = open(archivo, "wb")
    file.write(key)
    file.close

if module == "encriptarVar":
    # Modulo para encryptar el contenido de una variable
    ruta = GetParams('content')
    var = GetParams('idVar')
    varEncript = GetParams('idVarEncript')

    try:
        file = open(ruta, 'rb')
        key = file.read()
        file.close()

        contenido = GetVar(var)
        contenido = contenido.encode()
        f = Fernet(key)
        codificado = f.encrypt(contenido)
        SetVar(varEncript, codificado)
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "decriptarVar":
    # Modulo para decryptar el contenido de una variable
    ruta = GetParams('content')
    var = GetParams('idVar')
    varDecript = GetParams('idVarDecript')

    try:
        file = open(ruta, 'rb')
        key = file.read()
        file.close()

        contenido = GetVar(var)
        contenido = str(contenido)
        f = Fernet(key)
        desencriptado = f.decrypt(eval(contenido))
        SetVar(varDecript, desencriptado.decode())

    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e