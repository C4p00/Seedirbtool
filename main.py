import requests
import os 
from colorama import *
import time
#<============Librerias============>
rojo = Fore.RED
verde = Fore.GREEN
amarillo = Fore.YELLOW
blanco = Fore.WHITE
azul = Fore.BLUE
def banner():
  print("""
    ██████ ▓█████ ▓█████    ▓█████▄  ██▓ ██▀███   ▄▄▄▄   
▒██    ▒ ▓█   ▀ ▓█   ▀    ▒██▀ ██▌▓██▒▓██ ▒ ██▒▓█████▄ 
░ ▓██▄   ▒███   ▒███      ░██   █▌▒██▒▓██ ░▄█ ▒▒██▒ ▄██
  ▒   ██▒▒▓█  ▄ ▒▓█  ▄    ░▓█▄   ▌░██░▒██▀▀█▄  ▒██░█▀  
▒██████▒▒░▒████▒░▒████▒   ░▒████▓ ░██░░██▓ ▒██▒░▓█  ▀█▓
▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░    ▒▒▓  ▒ ░▓  ░ ▒▓ ░▒▓░░▒▓███▀▒
░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░    ░ ▒  ▒  ▒ ░  ░▒ ░ ▒░▒░▒   ░ 
░  ░  ░     ░      ░       ░ ░  ░  ▒ ░  ░░   ░  ░    ░ 
      ░     ░  ░   ░  ░      ░     ░     ░      ░      
                           ░                         ░ 
  [!] Tool en la version beta
  """)
def menu():
  print(f"""
  {verde}[1]{blanco} Busqueda de directorios con wordlists
  {verde}[2]{blanco} Wordlists disponibles
  {verde}[3]{blanco} Exit
  """)
def Bdw():
  wordlists = [
    "big", "big.txt", "catala", "catala.txt", "common", "common.txt", "small", "small.txt", "Big", "Catala", "Common", "Small", "Big.txt", "Catala.txt", "Common.txt", "Small.txt", "spanish.txt", "Spanish", "Spanish.txt"
  ]
  url = input(f"{verde}[{blanco}*{verde}] {blanco}URL: ")
  wordlist = str(input(f"{verde}[{blanco}*{verde}] Wordlist: "))
  if (wordlist in wordlists):
    print(f"{verde}[*] {blanco} Wordlist encontrada: {wordlist}")
  else:
    print(f"{rojo}[!] {blanco} Wordlist no encontrada...")
    time.sleep(1)
    print("Te recomendamos hacer el comando numero 2 para ver las wordlist disponibles...")
    return Bdw()
  wols = open(wordlist, "r", encoding="UTF-8")
  palabras = []
  lineas = wols.readlines()
  count = 0
  for line in lineas:
    palabras.append(line.strip('\n'))
    domain = url + palabras[count]
    ge = requests.get(domain)
    if (ge.status_code == 200):
      print(f"{verde}[+]{blanco} URL: {domain}", end="\n")
      lid = []
      lid.append(domain)
    else:
      pass
    count += 1
banner()
while(True):
  root = input(f"{verde}seedirb@H&C{blanco}:{azul}~{blanco}$ ")
  if (root == "1"):
    try:
      Bdw()
    except (KeyboardInterrupt):
      print("[+] KeyboardInterrupt...")
      time.sleep(3)
      exit()
  if (root == "2"):
    print(f"""
    |=======================================|
    |  {verde}Wordlists{blanco}                            |
    |=======================================|
    | big.txt                               |
    | catala.txt                            | 
    | common.txt                            |
    | small.txt                             |
    | spanish.txt                           |
    |=======================================|
    """)
  if (root == "help"):
    menu()
  if (root == "clear"):
    os.system("clear")
  else:
    pass
