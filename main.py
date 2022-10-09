import argparse

def main():
  parser = argparse.ArgumentParser(description="""
  Bienvenidos al menú de opciones de la aplicación de herramientas de ciberseguridad básica, por favor seleccione una opción:
  """)  
  parser.add_argument("-s", "--searchIP", help="Obtiene el hostname y la dirección IP del host", action="store_true")
  parser.add_argument("-p", "--scanPorts", help="Obtiene los puertos abiertos de un host", action="store_true")
  parser.add_argument("-c", "--crackMD5", help="Desencripta un hash MD5 y lo compara con las palabras del diccionario", action="store_true")
  args = parser.parse_args()

  if args.searchIP:
    if args.searchIP:
      import searchIP
      searchIP.searchIP()

  if args.scanPorts:
    if args.scanPorts:
      import scanPorts
      scanPorts.scanPorts()

  if args.crackMD5:
    if args.crackMD5:
      import passCracker
      passCracker.crackMD5()


if __name__ == "__main__":
    main()