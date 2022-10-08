import nmap

# Obtiene los puertos abiertos de un host

def scanPorts():
  ip = input("[+] Ingrese la dirección IP: ")
  nm = nmap.PortScanner()
  results = nm.scan(ip)
  print(results)