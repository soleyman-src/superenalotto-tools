import requests                     #libreria per webscraping
import os                           #libreria per pulire il terminale                              
import random                       #libreria per la generazione numeri random
import socket                       #libreria per il controllo connessione
import time                         #libreria per il comando sleep
import winsound                     #libreria per emettere suoni windows
import webbrowser                   #libreria per aprire link 
from rich import *                  #libreria per i colori ecc
from bs4 import BeautifulSoup       #libreria per webscraping

spz = "\n"
def apriChrome():
    url = 'http://www.superenalotto.it/archivio-estrazioni'
    webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new(url)
    
def controlloInternet():
    try:
        requests.get('http://www.google.it/')
    except:
        print('[!] COLLEGARSI A INTERNET')
        time.sleep(3)
        menu()
    else:
        pass

def finestraOnTop():
    import win32gui
    import win32con

    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,200,200,0)

def modificaDimensioneFinestra():
    cmd = 'mode 50,20'
    dimensione = 'mode move: x=64 y=950'
    os.system(dimensione)
    os.system(cmd)
    

def estrattoreNumeri():
    URL = "https://www.superenalotto.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("div", class_="results")
    for job_element in job_elements:
        print(job_element.text)


def estrattoreData():
    URL = "https://www.superenalotto.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find("div", class_="redBoxDateTime")
    print("Estrazione di:",job_elements.text)

def ultimaEstrazione():
    os.system('cls')
    controlloInternet()
    estrattoreData()
    estrattoreNumeri()
    sceltax = input("Vuoi leggere le Estrazioni precedenti? (s/n) ")
    if sceltax == "s":
        apriChrome()
    else:
        menu()

def generatore():
    os.system('cls')
    print("GENERATORE NUMERI RANDOM\n   x SUPERENALOTTO\n")
    qtaNumeri = int(input("Quanti Numeri vuoi generare? "))
    i=0
    print("\n")
    for i in range(qtaNumeri):
        from rich.console import Console
        console = Console()
        console.print(random.randrange(1, 90), style="bold italic")
    print("\n")
    scelta2 = input("Vuoi generarli di nuovo? (s/n)")
    if scelta2 == "s":
        generatore()
    else:
        os.system('cls')
        menu()

def scelta():

    scelta = input("Vuoi generare dei numeri casualmente? (s/n): ")
    if scelta == "s":
        generatore()
    else:
        exit()

def loop():
    estrattoreData()
    estrattoreNumeri()
    scelta()

def menu():
    os.system('cls')
    print ("[underline green][italic]*=- SUPERENALOTTO TOOLS -=*[/italic][/underline green]", spz , spz)
    print ("[bold]1. Ultima Estrazione ", spz)
    print ("[bold]2. Numeri Casuali", spz)
    print ("[bold]3. Calcolo Vincita Sistema", spz)
    print ("[bold]4. Esci", spz , spz)
    sceltaMenu = input ("Scelta: ")
    if sceltaMenu == "1":
        ultimaEstrazione()
    elif sceltaMenu == "2":
        generatore()
    elif sceltaMenu == "3":
        calcoloVincita()
    elif sceltaMenu == "4":
        exit()
        
def calcoloVincita():
    os.system('cls')
    due = float(input("- 2 : \n"))
    tre = float(input("- 3 : \n"))
    quattro = float(input("- 4 : \n"))
    cinque = float(input("- 5 : \n"))
    costoSchedina = float(input("- Costo Schedina: \n"))
    tot = (due*5)+(tre*25)+(quattro*120)+(cinque*32000)
    tot2 = (tot)-(costoSchedina)
    os.system('cls')
    print("TOTALE:  ", tot , spz)
    print("COSTO SCHEDINA:  ", costoSchedina , spz)
    print("GUADAGNO TOT:  ", tot2 , spz)
    scelta4 = input("Vuoi tornare al menu? (s/n): ")
    if scelta4 == "s":
        os.system('cls')
        menu()
    else:
        exit()
        
finestraOnTop
modificaDimensioneFinestra()
menu()
