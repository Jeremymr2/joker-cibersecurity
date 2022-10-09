import socket

# Obtiene el hostname y la direccion IP del host

def searchIP():

  print()
  print("  ______   ______   _   __  ______   ______   ")
  print(" |_    _| |  __  | | | / / |  ____| |  __  |  ")
  print("   |  |   | |  | | | |/ /  | |__    | |__| |  ")
  print("   |  |   | |  | | |   <   |  __|   |     <   ")
  print("  _|  |   | |__| | | |\ \  | |____  |  |\  \  ")
  print(" |____|   |______| |_| \_\ |______| |__| \__\ ")
  print()

  print("[Info] Herramienta para obtener el hostname y la dirección IP del host")
  print("  ||   Escrito en Python y utiliza sockets")
  print("  ||   Autor: @Jeremymr2")
  print()

  hostname = socket.gethostname() # Obtiene el hostname
  ip = socket.gethostbyname(hostname) # Obtiene la direccion IP

  print("Hostname: " + hostname) # Imprime el hostname
  print("IP: " + ip) # Imprime la direccion IP