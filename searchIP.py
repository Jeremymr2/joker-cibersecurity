import socket

# Obtiene el hostname y la direccion IP del host

def searchIP():
  hostname = socket.gethostname() # Obtiene el hostname
  ip = socket.gethostbyname(hostname) # Obtiene la direccion IP

  print("Hostname: " + hostname) # Imprime el hostname
  print("IP: " + ip) # Imprime la direccion IP