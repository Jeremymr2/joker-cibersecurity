import hashlib
from _utils.bannerEmmiter import bannerEmmiter

def crackMD5():  
  bannerEmmiter(['@Jeremymr2'], 'Herramienta para crackear un hash MD5 y compararlo con las palabras del diccionario', 'Escrito en Python y utiliza hashlib')
  

  encontrado = 0
  input_hash = input("Ingrese el hash: ") # Pide el hash
  pass_doc = input("Ingrese la dirección del archivo: ") # Pide el nombre del archivo

  try:
    pass_file = open(pass_doc, "r") # Abre el archivo
  except:
    raise("No se pudo abrir el archivo") # Imprime un mensaje de error

  for word in pass_file: # Itera las palabras del archivo
    enc_wrd = word.encode('utf-8') # Codifica la palabra
    digest = hashlib.md5(enc_wrd.strip()).hexdigest() # Obtiene el hash MD5 de la palabra

    if digest == input_hash: # Si el hash coincide
      print("La contraseña es: " + word) # Imprime la contraseña
      encontrado = 1 # Cambia el valor de encontrado
      break # Sale del ciclo

  if not encontrado: # Si no se encontró la contraseña
    print("Contraseña no encontrada, intente con otro archivo") # Imprime un mensaje

  pass_file.close() # Cierra el archivo