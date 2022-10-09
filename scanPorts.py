import nmap

# Obtiene los puertos abiertos de un host

def scanPorts():
  print()
  print("  ______   ______   _   __  ______   ______   ")
  print(" |_    _| |  __  | | | / / |  ____| |  __  |  ")
  print("   |  |   | |  | | | |/ /  | |__    | |__| |  ")
  print("   |  |   | |  | | |   <   |  __|   |     <   ")
  print("  _|  |   | |__| | | |\ \  | |____  |  |\  \  ")
  print(" |____|   |______| |_| \_\ |______| |__| \__\ ")
  print()

  print("[Info] Herramienta para escanear los puertos abiertos en una dirección IP")
  print("  ||   Escrito en Python y utiliza Nmap")
  print("  ||   Autor: @Jeremymr2")
  print()

  ip=input("[+] IP Objetivo ==> ")
  nm = nmap.PortScanner()
  puertos_abiertos="-p "
  results = nm.scan(hosts=ip,arguments="-sT -n -Pn -T4") # Escanea los puertos TCP
  count=0
  print("\nHost : %s" % ip) # Imprime la IP del host
  print("State : %s" % nm[ip].state()) # Estado del host
  for proto in nm[ip].all_protocols(): # Itera los protocolos
    print("Protocol : %s" % proto) # Imprime el protocolo
    print() # Salto de línea
    lport = nm[ip][proto].keys() # Obtiene los puertos
    sorted(lport) # Ordena los puertos
    for port in lport: # Itera los puertos
      print ("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"])) # Imprime el puerto y su estado
      if count==0: # Si es el primer puerto
        puertos_abiertos=puertos_abiertos+str(port) # Lo agrega a la cadena
        count=1 # Cambia el valor de count
      else: # Si no es el primer puerto
        puertos_abiertos=puertos_abiertos+","+str(port) # Lo agrega a la cadena
  print("\nPuertos abiertos: "+ puertos_abiertos +" "+str(ip)) # Imprime los puertos abiertos
