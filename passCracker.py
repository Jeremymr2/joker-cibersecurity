import hashlib

# Desencripta un hash MD5 y lo compara con las palabras del diccionario

def crackMD5():
  encontrado = 0
  input_hash = input("Ingrese el hash: ")
  pass_doc = input("Ingrese el nombre del archivo: ")

  try:
    pass_file = open(pass_doc, "r")
  except:
    print("No se pudo abrir el archivo")
    quit()

  for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == input_hash:
      print("La contraseña es: " + word)
      encontrado = 1
      break

  if not encontrado:
    print("Contraseña no encontrada, intente con otro archivo")

  pass_file.close()