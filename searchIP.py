import socket

# Obtiene el hostname y la direccion IP del host

def searchIP():
  hostname = socket.gethostname()
  ip = socket.gethostbyname(hostname)

  print("Hostname: " + hostname)
  print("IP: " + ip)