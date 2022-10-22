import socket
from _utils.bannerEmmiter import bannerEmmiter

# Obtiene el hostname y la direccion IP del host

def searchIP():
  bannerEmmiter(['@Jeremymr2'], 'Herramienta para obtener el hostname y la dirección IP del host', 'Escrito en Python y utiliza sockets')

  hostname = socket.gethostname() # Obtiene el hostname
  ip = socket.gethostbyname(hostname) # Obtiene la direccion IP

  print("Hostname: " + hostname) # Imprime el hostname
  print("IP: " + ip) # Imprime la direccion IP