"""
@titel Netz-IP-Generator
@author Leonard Voß
@description Dieser Netzadress  bzw. NetzIP-Generator errechnet die Adresse eines Netzwerkes, die Broadcast-Adresse durch die Angabe einer IP-Adresse und einer Subnetzmaske bzw. eines CIDR-Suffix.
@version 1.0
@type Open-Source
"""

import pyfiglet
import colorama
import os
import ipaddress                                    #Initialisierung der Bibliotheken
from colorama import init, Fore, Style

IPA1 = IPA2 = IPA3 = IPA4 = IPGENERAL = "Prüfvariable"
SUBNETA1 = SUBNETA2 = SUBNETA3 = SUBNETA4 = "Prüfvariable"
subnetmask1 = subnetmask2 = subnetmask3 = subnetmask4 = None
ip1 = ip2 = ip3 = ip4 = None                                    #Initialisierung globaler Variablen
choose = None
subnetmask1decimal = subnetmask2decimal = subnetmask3decimal = subnetmask4decimal = None
ip1decimal = ip2decimal = ip3decimal = ip4decimal = None
suffix = None
SUFFIXA = None

def mainsession():      #Hauptprogramm
    colorama.init()
    intro()
    ipconfig()
    if controliptype() == True and controlipnumbers() == True:
        ok(">> Gültige IP-Adresse")
        menue()
        if choose == "1" or choose == "Subnetzmaske" or choose == "[1]": 
            subnetmaskconfig()
            if controlsubmasktype() == True and controlsubmasknumbers() == True and controlsubnetmaskvalue() == True and controlsubnetmaskorder():
                ok(">> Gültige Subnetzmaske")
                outputnetworkadress()
        elif choose == "2" or choose == "Suffix" or choose == "[2]" or choose == "CIDR-Suffix":
            suffixconfig()
            print(" ")
            if controlsuffixtype() == True and controlsuffixnumbers() == True:
                ok(">> Gültiger CIDR-Suffix")
                outputsuffix()
        else:
            error(">> Ungültige Eingabe")
            restartmenue()
    restartprogram()

def error(n):
    print(Fore.RED)
    print(n)            #Ausgabe von Fehlermeldungen
    print(Fore.WHITE)

def suberrorpart1(n):
    print(Fore.RED)     #Ausgabe von mehrstufigen Fehlermeldungen
    print(n)

def suberrorpart2(n):
    print(Fore.YELLOW, n)
    print(Fore.WHITE)

def ok(n):
    print(Fore.GREEN)
    print(n)            #Ausgabe von Bestätigungen
    print(Fore.WHITE)

def binx(x):
    z = format(int(x), "08b")   #Umwandlung von Integer-Werten in Binärzahlen (8-Bit-Format)
    return z

def ipconfig():
    ip1config()
    ip2config()
    ip3config() #Konfiguration der IP-Adresse 
    ip4config()
    controlip() 
    global IPGENERAL
    IPGENERAL = str(IPA1 + "." + IPA2 + "." + IPA3 + "." + IPA4)
    return True

def ip1config():
    global IPA1
    IPA1 = input("1.Stelle der IP-Adresse: ")
    return IPA1

def ip2config(): 
    global IPA2
    IPA2 = input("2.Stelle der IP-Adresse: ")
    return IPA2

def ip3config(): 
    global IPA3 
    IPA3 = input("3.Stelle der IP-Adresse: ")
    return IPA3

def ip4config():
    global IPA4
    IPA4 = input("4.Stelle der IP-Adresse: ")
    return IPA4

def menue():
    global choose
    print(Fore.CYAN)
    print("Wie möchtest du das Subnetz angeben?")
    print(Fore.WHITE)
    print("[1] Subnetzmaske")                           #Menü zum auswählen des Subnetzes 
    print("[2] CIDR-Suffix")
    print("")
    choose = input("<< ")
    print(Fore.WHITE)

def controlip():
    global ip1decimal 
    ip1decimal = IPA1.isdecimal()
    global ip2decimal
    ip2decimal = IPA2.isdecimal()   #Kontrollprogramm für Dezimalzahlen
    global ip3decimal
    ip3decimal = IPA3.isdecimal()
    global ip4decimal
    ip4decimal = IPA4.isdecimal()

def controliptype():
    if ip1decimal != True or ip2decimal != True or ip3decimal != True or ip4decimal != True:
        error(">> Ungültige IP-Adresse [Nicht-Dezimalzahlen]")
        if ip1decimal != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("^")
        if ip2decimal != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("    ^")             #Fehlerausgabe wenn IP-Adresse Nicht-Dezimalzahlen enthält
        if ip3decimal != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("        ^")
        if ip4decimal != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("            ^")
        restartip()
        return False
    else:
        return True

def controlipnumbers():
    global ip1
    ip1 = int(IPA1)
    global ip2
    ip2 = int(IPA2)
    global ip3                  #Fehlermeldung von IP-Adresse zahlen die größer als 255 sind enthält
    ip3 = int(IPA3)
    global ip4
    ip4 = int(IPA4)
    if ip1 > 255 or ip2 > 255 or ip3 > 255 or ip4 > 255:
        error(">> Ungültige IP-Adresse [Adressbereich]:")
        if ip1 > 255:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("^")
        if ip2 > 255:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("    ^")
        if ip3 > 255:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("        ^")
        if ip4 > 255:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("            ^")
        restartip()
        return False
    else:
        return True

def intro():
    welcomemessage = pyfiglet.figlet_format("NetzIPGenerator")
    print(Fore.GREEN)                       #Initialisierung
    print("____________________________________________________________________________")
    print(Fore.GREEN)
    print(welcomemessage)
    print("      Written in PYTHON - by Leonard Voß (2020) - Open-Soure-Project")
    print("____________________________________________________________________________")
    print(Fore.CYAN)
    print("IPv4-Adresse: ")
    print(Fore.WHITE)

def subnetmaskconfig():
    subnetmask1config()
    subnetmask2config() #Initialisierung der Subnetzmaske
    subnetmask3config()
    subnetmask4config()

def subnetmask1config():
    global SUBNETA1
    SUBNETA1 = input("1.Stelle der Subnetzmaske: ")
    return SUBNETA1

def subnetmask2config():
    global SUBNETA2
    SUBNETA2 = input("2.Stelle der Subnetzmaske: ")
    return SUBNETA2

def subnetmask3config():
    global SUBNETA3
    SUBNETA3 = input("3.Stelle der Subnetzmaske: ")
    return SUBNETA3
    
def subnetmask4config():
    global SUBNETA4
    SUBNETA4 = input("4.Stelle der Subnetzmaske: ")
    return SUBNETA4

def controlsubmasknumbers():
    global subnetmask1
    subnetmask1 = int(SUBNETA1)
    global subnetmask2
    subnetmask2 = int(SUBNETA2) #Ausgabe von Fehlermeldung bei Zahlen über 255
    global subnetmask3              
    subnetmask3 = int(SUBNETA3)
    global subnetmask4
    subnetmask4 = int(SUBNETA4)
    if subnetmask1 > 255 or subnetmask2 > 255 or subnetmask3 > 255 or subnetmask4 > 255:
        error(">> Ungültige Subnetzmaske [Adressbereich]")
        if subnetmask1 > 255:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("^")
        if subnetmask2 > 255:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("    ^")
        if subnetmask3 > 255:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("        ^")
        if subnetmask4 > 255:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("            ^")
        restartsubnetmask()
        return False
    else:
        return True

def controlsubmasktype():
    global subnetmask1decimal 
    subnetmask1decimal = SUBNETA1.isdecimal()
    global subnetmask2decimal
    subnetmask2decimal = SUBNETA2.isdecimal()
    global subnetmask3decimal                       #Ausgabe von Fehlermeldungen bei Nicht-Dezimalzahlen
    subnetmask3decimal = SUBNETA3.isdecimal()
    global subnetmask4decimal
    subnetmask4decimal = SUBNETA4.isdecimal()
    if subnetmask1decimal != True or subnetmask2decimal != True or subnetmask3decimal != True or subnetmask4decimal != True:
        error(">> Ungültige IP-Adresse [Nicht-Dezimalzahlen]")
        if subnetmask1decimal != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("^")
        if subnetmask2decimal != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("    ^")
        if subnetmask3decimal != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("        ^")
        if subnetmask4decimal != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("            ^")
        restartsubnetmask()
        return False
    else:
        return True
    
def controlsubnetmaskorder():
    if controlsubnetmask1order() != True or controlsubnetmask2order() != True or controlsubnetmask3order() != True:
        error(">> Ungültige Subnetzmaske [Ungütige Anordnung]")
        if controlsubnetmask1order() != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("    ^")
        if controlsubnetmask2order() != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("        ^")     #Ausgabe bei Fehlermeldungen, ausgelöst durch eine falsche Reihenfolge
        if controlsubnetmask3order() != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("            ^")
        restartsubnetmask()
        return False
    else:
        return True

def controlsubnetmask1order():
    if subnetmask1 == 0 and subnetmask2 > 0:
        return False
    if subnetmask1 == 1 and subnetmask2 > 0:
        return False
    if subnetmask1 == 3 and subnetmask2 > 0:
        return False
    if subnetmask1 == 7 and subnetmask2 > 0:
        return False
    if subnetmask1 == 15 and subnetmask2 > 0:
        return False
    if subnetmask1 == 31 and subnetmask2 > 0:
        return False
    if subnetmask1 == 63 and subnetmask2 > 0:
        return False
    if subnetmask1 == 127 and subnetmask2 > 0:
        return False
    else: 
        return True

def controlsubnetmask2order():
    if subnetmask2 == 0 and subnetmask3 > 0:
        return False
    if subnetmask2 == 1 and subnetmask3 > 0:
        return False
    if subnetmask2 == 3 and subnetmask3 > 0:
        return False
    if subnetmask2 == 7 and subnetmask3 > 0:
        return False
    if subnetmask2 == 15 and subnetmask3 > 0:
        return False
    if subnetmask2 == 31 and subnetmask3 > 0:
        return False
    if subnetmask2 == 63 and subnetmask3 > 0:
        return False
    if subnetmask2 == 127 and subnetmask3 > 0:
        return False
    else: 
        return True

def controlsubnetmask3order():
    if subnetmask3 == 0 and subnetmask4 > 0:
        return False
    if subnetmask3 == 1 and subnetmask4 > 0:
        return False
    if subnetmask3 == 3 and subnetmask4 > 0:
        return False
    if subnetmask3 == 7 and subnetmask4 > 0:
        return False
    if subnetmask3 == 15 and subnetmask4 > 0:
        return False
    if subnetmask3 == 31 and subnetmask4 > 0:
        return False
    if subnetmask3 == 63 and subnetmask4 > 0:
        return False
    if subnetmask3 == 127 and subnetmask4 > 0:
        return False
    else: 
        return True

def controlsubnetmaskvalue():
    if controlsubnetmaskvalue1() != True or controlsubnetmaskvalue2() != True or controlsubnetmaskvalue3() != True or controlsubnetmaskvalue4() != True:
        error("Ungültige Subnetzmaske [Ungültiger Wertebereich]")
        if controlsubnetmaskvalue1() != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("^")
        if controlsubnetmaskvalue2() != True:
            suberrorpart1("XXX.XXX.XXX.XXX")        #Ausgabe von Fehlermeldungen bei ungültigen Werten
            suberrorpart2("    ^")
        if controlsubnetmaskvalue3() != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("        ^")
        if controlsubnetmaskvalue4() != True:
            suberrorpart1("XXX.XXX.XXX.XXX")
            suberrorpart2("            ^")
        restartsubnetmask()
        return False
    else:
        return True

def controlsubnetmaskvalue1():
    if subnetmask1 == 255 or subnetmask1 == 254 or subnetmask1 == 252 or subnetmask1 == 248 or subnetmask1 == 240 or subnetmask1 == 224 or subnetmask1 == 192 or subnetmask1 == 128 or subnetmask1 == 0:
        return True

def controlsubnetmaskvalue2():
    if subnetmask2 == 255 or subnetmask2 == 254 or subnetmask2 == 252 or subnetmask2 == 248 or subnetmask2 == 240 or subnetmask2 == 224 or subnetmask2 == 192 or subnetmask2 == 128 or subnetmask2 == 0:
        return True 

def controlsubnetmaskvalue3():
    if subnetmask3 == 255 or subnetmask3 == 254 or subnetmask3 == 252 or subnetmask3 == 248 or subnetmask3 == 240 or subnetmask3 == 224 or subnetmask3 == 192 or subnetmask3 == 128 or subnetmask3 == 0:
        return True

def controlsubnetmaskvalue4():
    if subnetmask4 == 255 or subnetmask4 == 254 or subnetmask4 == 252 or subnetmask4 == 248 or subnetmask4 == 240 or subnetmask4 == 224 or subnetmask4 == 192 or subnetmask4 == 128 or subnetmask4 == 0:
        return True
def outputnetworkadress():
    binip1 = binx(ip1)
    binip2 = binx(ip2)
    binip3 = binx(ip3)     #Ausgabe der IP-Adresse
    binip4 = binx(ip4)
    binsubmask1 = format(int(subnetmask1), "08b")
    binsubmask2 = format(int(subnetmask2), "08b")
    binsubmask3 = format(int(subnetmask3), "08b")
    binsubmask4 = format(int(subnetmask4), "08b")
    dot = "."
    IP = str(ip1) + str(dot) + str(ip2) + str(dot) + str(ip3) + str(dot) + str(ip4)
    MASK = str(subnetmask1) + str(dot) + str(subnetmask2) + str(dot) + str(subnetmask3) + str(dot) + str(subnetmask4)
    net = ipaddress.IPv4Network(IP + '/' + MASK, False)    
    if str(IPGENERAL) == str(net.broadcast_address):
        error(">> Ungültige IP-Adresse [Broadcast = IP-Adresse]")
    else:
        print(Fore.CYAN)
        print("IPv4-Adresse:")
        print(Fore.YELLOW)
        dot = "."
        print(ip1, dot, ip2, dot, ip3, dot, ip4)
        print(Fore.WHITE)
        print(">>", str(binip1 + binip2 + binip3 + binip4))
        print(Fore.CYAN)
        print("Subnetzmaske:")
        print(Fore.YELLOW)
        print(subnetmask1, dot, subnetmask2, dot, subnetmask3, dot, subnetmask4) 
        print(Fore.WHITE)
        print(">>", str(binsubmask1 + binsubmask2 + binsubmask3 + binsubmask4))   #Ausgabe der Subnetzmaske in Binärcode 
        networkip1 = ip1 & subnetmask1
        networkip2 = ip2 & subnetmask2
        networkip3 = ip3 & subnetmask3   #Generierung der NetzIP bzw. Netzadresse
        networkip4 = ip4 & subnetmask4
        print(Fore.CYAN)
        print("CIDR-Suffix:")
        print(Fore.YELLOW)
        cidrsuffix = binsubmask1.count("1") + binsubmask2.count("1") + binsubmask3.count("1") + binsubmask4.count("1")
        print("/" + str(cidrsuffix))
        print(Fore.CYAN)
        dot = "."
        print("Netz-IP: ")           #Ausgabe der Daten
        print(Fore.YELLOW)
        print(networkip1, dot, networkip2, dot, networkip3, dot, networkip4)
        print(Fore.WHITE)
        print(">>", str(format(networkip1, "08b") + format(networkip2, "08b") + format(networkip3, "08b") + format(networkip4, "08b")))
        print(Fore.CYAN)
        print('Broadcast:')
        print(Fore.YELLOW) 
        print(net.broadcast_address)
        binbroad = format(int(net.broadcast_address), "0b")
        print(Fore.WHITE)
        print(">>", binbroad)

def suffixconfig():
    print(" ")              #Konfigurierung des CIDR-Suffix
    global SUFFIXA
    SUFFIXA = input("CIDR-Suffix: /")

def controlsuffixtype(): 
    suffixdecimal = SUFFIXA.isdecimal()
    if suffixdecimal != True:
        error(">> Ungütiger CIDR-Suffix [Nicht-Dezimalzahl")   #Fehlermeldung bei Nicht-Dezimalzahlen
        restartsuffix()
        return False    
    else:
        return True

def controlsuffixnumbers():
    suffix = int(SUFFIXA)
    if suffix > 32:
        error(">> Ungültiger CIDR-Suffix [Adressbereich]") #Fehlermeldung bei ungültigem Suffix [über 32]
        restartsuffix()
        return False
    else:
        return True

def outputsuffix():
    translate = {"0": 00000000000000000000000000000000, "1": 10000000000000000000000000000000, "2": 11000000000000000000000000000000, "3": 11100000000000000000000000000000, "4": 11110000000000000000000000000000, "5": 11111000000000000000000000000000, "6": 11111100000000000000000000000000, "7": 11111110000000000000000000000000, "8": 11111111000000000000000000000000, "9": 11111111100000000000000000000000, "10": 11111111110000000000000000000000, "11": 11111111111000000000000000000000, "12": 11111111111100000000000000000000, "13": 11111111111110000000000000000000, "14": 11111111111111000000000000000000, "15": 11111111111111100000000000000000, "16": 11111111111111110000000000000000, "17": 11111111111111111000000000000000, "18": 11111111111111111100000000000000, "19": 11111111111111111110000000000000, "20": 11111111111111111111000000000000, "21": 11111111111111111111100000000000, "22": 11111111111111111111110000000000, "23": 11111111111111111111111000000000, "24": 11111111111111111111111100000000, "25": 11111111111111111111111110000000, "26": 11111111111111111111111111000000, "27": 11111111111111111111111111100000, "28": 11111111111111111111111111110000, "29": 11111111111111111111111111111000, "30": 11111111111111111111111111111100, "31": 11111111111111111111111111111110, "32": 11111111111111111111111111111111}
    binsuffix = translate[SUFFIXA]
    binsuffix1 = str(binsuffix)[0:8]
    binsuffix2 = str(binsuffix)[8:16]
    binsuffix3 = str(binsuffix)[16:24]
    binsuffix4 = str(binsuffix)[24:32]  #Ausgabe des Suffix
    decsuffix1 = int(binsuffix1, 2)
    decsuffix2 = int(binsuffix2, 2)
    decsuffix3 = int(binsuffix3, 2)
    decsuffix4 = int(binsuffix4, 2)
    networkip1 = ip1 & decsuffix1
    networkip2 = ip2 & decsuffix2
    networkip3 = ip3 & decsuffix3
    networkip4 = ip4 & decsuffix4
    dot = "."
    IP = IPA1 + str(dot) + IPA2 + str(dot) + IPA3 + str(dot) + IPA4
    MASK = str(decsuffix1) + str(dot) + str(decsuffix2) + str(dot) + str(decsuffix3) + str(dot) + str(decsuffix4)
    net = ipaddress.IPv4Network(IP + '/' + MASK, False)
    binbroad = format(int(net.broadcast_address), "0b")
    if str(IPGENERAL) == str(net.broadcast_address):
        error(">> Ungültige IP-Adresse [Broadcast = IP-Adresse]")
    else:
        print(Fore.CYAN)
        print("IPv4-Adresse:")
        print(Fore.YELLOW)
        print(IPA1, dot, IPA2, dot, IPA3, dot, IPA4)
        print(Fore.WHITE)
        binip1 = binx(ip1)
        binip2 = binx(ip2)
        binip3 = binx(ip3)
        binip4 = binx(ip4)
        print(">>", str(binip1 + binip2 + binip3 + binip4))
        print(Fore.CYAN)
        print("Subnetzmaske:")
        print(Fore.YELLOW)
        print(decsuffix1, dot, decsuffix2, dot, decsuffix3, dot, decsuffix4)
        print(Fore.WHITE)
        print(">>", str(binsuffix1 + binsuffix2 + binsuffix3 + binsuffix4))
        print(Fore.CYAN)
        print("CIDR-Suffix:")
        print(Fore.YELLOW)
        print("/" + SUFFIXA)
        dot = "."
        print(Fore.CYAN)
        print("Netz-IP: ")           #Ausgabe der Daten
        print(Fore.YELLOW)
        print(networkip1, dot, networkip2, dot, networkip3, dot, networkip4)
        print(Fore.WHITE)
        print(">>", str(format(networkip1, "08b") + format(networkip2, "08b") + format(networkip3, "08b") + format(networkip4, "08b")))
        print(Fore.WHITE)
        print(Fore.CYAN)
        print('Broadcast:')
        print(Fore.YELLOW) 
        print(net.broadcast_address)
        print(Fore.WHITE)
        print(">>", binbroad)

def restartmenue(): #Korrekturfunktion bei unzulässiger Menüauswahl
    menue()
    if choose == "1" or choose == "Subnetzmaske" or choose == "[1]": 
        subnetmaskconfig()
        if controlsubmasktype() == True and controlsubmasknumbers() == True:
            ok(">> Gültige Subnetzmaske")
            outputnetworkadress()
    elif choose == "2" or choose == "Suffix" or choose == "[2]" or choose == "CIDR-Suffix":
        suffixconfig()
        print(" ")
        if controlsuffixtype() == True and controlsuffixnumbers() == True:
            ok(">> Gültiger CIDR-Suffix")
            outputsuffix()
    else:
        error(">> Ungültige Eingabe")
        restartmenue()
    
def restartip(): #Korrekturfunktion bei falscher IP-Adresse
    ipconfig()
    if controliptype() == True and controlipnumbers() == True:
        ok(">> Gültige IP-Adresse")
        menue()
        if choose == "1" or choose == "Subnetzmaske" or choose == "[1]": 
            subnetmaskconfig()
            if controlsubmasktype() == True and controlsubmasknumbers() == True and controlsubnetmaskvalue() == True and controlsubnetmaskorder():
                ok(">> Gültige Subnetzmaske")
                outputnetworkadress()
        elif choose == "2" or choose == "Suffix" or choose == "[2]" or choose == "CIDR-Suffix":
            suffixconfig()
            print(" ")
            if controlsuffixtype() == True and controlsuffixnumbers() == True:
                ok(">> Gültiger CIDR-Suffix")
                outputsuffix()
        else:
            error(">> Ungültige Eingabe")
            restartmenue()
    
def restartsubnetmask(): #Korrekturfunktion bei falscher Subnetzmaske
    if choose == "1" or choose == "Subnetzmaske" or choose == "[1]": 
        subnetmaskconfig()
        if controlsubmasktype() == True and controlsubmasknumbers() == True and controlsubnetmaskvalue() == True and controlsubnetmaskorder() == True:
            ok(">> Gültige Subnetzmaske")
            outputnetworkadress()
    elif choose == "2" or choose == "Suffix" or choose == "[2]" or choose == "CIDR-Suffix":
        suffixconfig()
        print(" ")
        if controlsuffixtype() == True and controlsuffixnumbers() == True:
            ok(">> Gültiger CIDR-Suffix")
            outputsuffix()
    else:
        error(">> Ungültige Eingabe")
        restartmenue()
    
def restartsuffix(): #Korrekturfunktion bei falschem Suffix
    if choose == "2" or choose == "Suffix" or choose == "[2]" or choose == "CIDR-Suffix":
        suffixconfig()
        print(" ")
        if controlsuffixtype() == True and controlsuffixnumbers() == True:
            ok(">> Gültiger CIDR-Suffix")
            outputsuffix()
    else:
        error(">> Ungültige Eingabe")
        restartmenue()
    
def restartprogram(): #Abfrage ob das Programm erneut gestartet / ausgeführt werden soll
    print(Fore.LIGHTBLACK_EX)
    print("Möchtest du das Programm erneut ausführen? [Y/N]")
    answer = input ("<< ")
    if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes" or answer == "YES" or answer == "1" or answer == "True":
        ok(">> Programm wird erneut ausgeführt...")
        os.system("cls")
        mainsession()
    elif answer == "N" or answer == "n" or answer == "No" or answer == "no" or answer == "NO" or answer == "0" or answer == "False":
        print(">> Ok.")
    else:
        error(">> Ungültige Eingabe")
        restartprogram()

mainsession()   #Ausführen des Programmcode