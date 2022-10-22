import hashlib

def crackMD5():  
  print()
  print("  ______   ______   _   __  ______   ______   ")
  print(" |_    _| |  __  | | | / / |  ____| |  __  |  ")
  print("   |  |   | |  | | | |/ /  | |__    | |__| |  ")
  print("   |  |   | |  | | |   <   |  __|   |     <   ")
  print("  _|  |   | |__| | | |\ \  | |____  |  |\  \  ")
  print(" |____|   |______| |_| \_\ |______| |__| \__\ ")
  print()

  print("[Info] Herramienta para crackear un hash MD5 y compararlo con las palabras del diccionario")
  print("  ||   Escrito en Python y utiliza hashlib")
  print("  ||   Autor: @Jeremymr2")
  print()


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