import re, subprocess, ctypes, os, sys
from os import system

def is_admin():
    is_admin = False
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin


# obtener el sistema operativo del host

def getSo(): # Hara de funcion main

  print()
  print("  ______   ______   _   __  ______   ______   ")
  print(" |_    _| |  __  | | | / / |  ____| |  __  |  ")
  print("   |  |   | |  | | | |/ /  | |__    | |__| |  ")
  print("   |  |   | |  | | |   <   |  __|   |     <   ")
  print("  _|  |   | |__| | | |\ \  | |____  |  |\  \  ")
  print(" |____|   |______| |_| \_\ |______| |__| \__\ ")
  print()

  print("[Info] Herramienta para obtener el sistema operativo del host con el menor ruido posible")
  print("  ||   Escrito en Python y utiliza sockets")
  print("  ||   Autor: @Bryan-Herrera-Dev")
  print()

  if is_admin():
    ip=input("[+] IP Objetivo ==> ")

  else:
    print("[!] Error: No tienes privilegios de administrador")
    print("[!] Ejecuta el programa como administrador")
    sys.exit(1)