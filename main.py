import argparse, signal
from _utils import handlerCtrsC

# Función para capturar la señal SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handlerCtrsC.def_handler)

def main():

  parser = argparse.ArgumentParser(description="""
    ______   ______   _   __  ______   ______   
   |_    _| |  __  | | | / / |  ____| |  __  |  
     |  |   | |  | | | |/ /  | |__    | |__| |  
     |  |   | |  | | |   <   |  __|   |     <   
    _|  |   | |__| | | |\ \  | |____  |  |\  \  
   |____|   |______| |_| \_\ |______| |__| \__\ 
   
  Bienvenidos al menú de opciones JOKER de herramientas de ciberseguridad básica
  """, formatter_class=argparse.RawTextHelpFormatter)
  
  parser.add_argument("-s", "--searchIP", help="Obtiene el hostname y la dirección IP del host", action="store_true")
  parser.add_argument("-p", "--scanPorts", help="Obtiene los puertos abiertos de un host", action="store_true")
  parser.add_argument("-md5", "--crackMD5", help="Desencripta un hash MD5 y lo compara con las palabras del diccionario", action="store_true")
  parser.add_argument("-gSO", "--getSO", help="Obtiene el sistema operativo del host", action="store_true")
  args = parser.parse_args()

  if args.searchIP:
    if args.searchIP:
      from _funcs import searchIP
      searchIP.searchIP()

  if args.scanPorts:
    if args.scanPorts:
      from _funcs import scanPorts
      scanPorts.scanPorts()

  if args.crackMD5:
    if args.crackMD5:
      from _funcs import passCracker
      passCracker.crackMD5()
  
  if args.getSO:
    if args.getSO:
      from _funcs import getSO
      getSO.getSo()



if __name__ == "__main__":
    main()