import re, subprocess, ctypes, os, sys, platform
from os import system

def is_admin():
    is_admin = False
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def getTtl(host):
    # Se obtiene el TTL del host
    command = ['ping', '-c', '1', host]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    (out,err) = proc.communicate()

    out = out.split()
    for i in range(len(out)-5):
        if out[i].decode('utf-8').find('TTL') == 0:
            out = out[i].decode('utf-8')
            break
        
    ttl_value = re.findall(r"\d{1,3}", out)[0]
 
    return ttl_value    
   
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
    # validar que es una ip valida
    if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
        ttl = getTtl(ip)
        print("[+] TTL: " + ttl)

    else:
        print("[!] La IP ingresada no es valida")
        print("[!] Ejemplo de IP valida: 192.168.1.1")
        sys.exit(1)
  else:
    print("[!] Error: No tienes privilegios de administrador")
    print("[!] Ejecuta el programa como administrador")
    sys.exit(1)