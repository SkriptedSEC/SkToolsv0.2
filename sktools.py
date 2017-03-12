#!/usr/bin/env python
# _*_ coding: utf8 _*_


import os
import sys, traceback
import subprocess
from sys import exit
#from datetime import *
def logo():
    print '''\033[1;94m
   ██████  ██ ▄█▀ ██▀███   ██▓ ██▓███  ▄▄▄█████▓▓█████ ▓█████▄ 
 ▒██    ▒  ██▄█▒ ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌
 ░ ▓██▄   ▓███▄░ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░▒███   ░██   █▌
   ▒   ██▒▓██ █▄ ▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌
 ▒██████▒▒▒██▒ █▄░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ ░▒████▒░▒████▓ 
 ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒ 
 ░ ░▒  ░ ░░ ░▒ ▒░  ░▒ ░ ▒░ ▒ ░░▒ ░         ░     ░ ░  ░ ░ ▒  ▒ 
 ░  ░  ░  ░ ░░ ░   ░░   ░  ▒ ░░░         ░         ░    ░ ░  ░ 
       ░  ░  ░      ░      ░                       ░  ░   ░    
                        \033[1;91mSkTools v0.2\033[1;m                           
 \033[1;m   '''


# create launcher
def create_launcher():
    cwd = os.getcwd()
    filewrite = open("/usr/local/bin/sktools", "w")
    filewrite.write("#!/bin/bash\ncd %s\nsudo chmod +x sktools.py\n sudo python sktools.py" % (cwd))
    filewrite.close()
    subprocess.Popen("sudo chmod +x /usr/local/bin/sktools && sudo chmod 777 /usr/local/bin/sktools", shell=True).wait()


def inicio():
    try:
        #actual = datetime.time(datetime.now())
        #local = actual.strftime("%I:%M:%S")
        print " \033[1;91m\t\t    Bienvenido\033[1;m"
        print " \033[1;91m\t\tEscoje una opcion\033[1;m"
        print "\033[1;96m1.- Limpiar sistema\033[1;m       \033[1;96m2.- Actualizar lista de paquetes\033[1;m"
        print "\033[1;96m3.- Hacer un upgrade\033[1;m      \033[1;96m4.- Otras\033[1;m"
        print "\033[1;96m5.- Salir\033[1;m"
    except KeyboardInterrupt:
        print("\n")
        print("\033[1;91m\t\t[!]Saliendo, God Bye ;)...\nGracias Por Usar sktools :)\033[1;m")
        exit()
        sys.exit()


def uno():
    print "Escogiste limpiar sistema"
    print "Por favor espere..."
    cmd1 = os.system("sudo apt-get autoclean && apt-get autoremove && apt-get purge")
    logo()
    todo()


def dos():
    print "Escogiste actualizar lista de paquetes"
    cmd1 = os.system("sudo apt-get update")
    logo()
    todo()


def tres():
    print "Escogiste hacer un upgrade"
    print "Actualizando ;)"
    cmd1 = os.system("sudo apt-get dist-upgrade")
    logo()
    todo()


def cuatro():
    logo()
    print '''
    \033[1;91m\n\t\t    Escoge Una Opcion\033[1;m
    \033[1;96m
1.- Hacking Tools                 2.- Accesorios
    
3.- Servicios                     4.- Entornos De Escritorio
    
5.- Remover Entorno De Escritorio 6.- Añadir Repositorios 

7.- Remover Repositorios          8.- Salir

\033[1;91mEscriba 'back' Sin Comillas Para Regresar Al Menu Anterior\033[1;m
    '''
    cuatroop = raw_input("\033[1;92m> \033[1;m")

    if cuatroop == "1":
        def mistools():
            logo()
            print '''
            \033[1;96m
    1.-Recolección De Información     2.-Analisis De Vulnerabilidades

    3.-Aplicaciones Web               4.-Bases De Datos
      
    5.-Ataques A Contraseñas          6.-Ataques Wireless

    7.-Ingeniería Inversa             8.-Explotación

    9.-Husmeando Envenenando          10.-Manteniendo Acceso

    11.-Analisis Forense              12.-Herramientas De Reporte

    13.-Ingeniería Social             14.-Programacion

    15.-Anonimato                     16.-Criptografia
    
    17.-Analisis De Malware           18.- Salir\n

\033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m

\033[1;91mEscoge una opción:\033[1;m\n
    \033[1;m
    '''
            hacking = raw_input("\033[1;91m> \033[1;m")
            if hacking == "1":
                def tools1hacking():
                    logo()
                    print '''
\033[1;91m#########################################################\033[1;m
\033[1;91m# \t\tRecoleccion De Informacion\t\t#\033[1;m
\033[1;91m#########################################################\033[1;m
\033[1;36m
1.- acccheck					30.- lbd
2.- ace-voip					31.- Maltego Teeth
3.- Amap					    32.- masscan
4.- Automater					33.- Metagoofil
5.- bing-ip2hosts				34.- Miranda
6.- braa					    35.- Nmap
7.- CaseFile					36.- p0f
8.- CDPSnarf					37.- Parsero
9.- cisco-torch				    38.- Recon-ng
10.- Cookie Cadger				39.- SET
11.- copy-router-config		    40.- smtp-user-enum		
12.- DMitry					    41.- snmpcheck
13.- dnmap					    42.- sslcaudit
14.- dnsenum				    43.- SSLsplit	
15.- dnsmap					    44.- sslstrip
16.- DNSRecon					45.- SSLyze
17.- dnstracer					46.- THC-IPV6
18.- dnswalk					47.- theHarvester
19.- DotDotPwn					48.- TLSSLed
20.- enum4linux					49.- twofi
21.- enumIAX					50.- URLCrazy
22.- exploitdb				    51.- Wireshark	
23.- Fierce					    52.- WOL-E
24.- Firewalk					53.- Xplico
25.- fragroute					54.- iSMTP
26.- fragrouter					55.- InTrace
27.- Ghost Phisher				56.- hping3
28.- GoLismero					
29.- goofile
\033[1;m
\033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
\033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m			 
        						'''
                    print "\033[1;93m¿Qué Herramienta Desea Instalar?\033[1;m"
                    hackingop = raw_input("\033[1;92m> \033[1;m")
                    if hackingop == "1":
                        cmd = os.system("sudo apt-get install acccheck")
                        tools1hacking()
                    elif hackingop == "back":
                        mistools()
                    elif hackingop == "2":
                        cmd = os.system("sudo apt-get install ace-voip")
                        tools1hacking()
                    elif hackingop == "3":
                        cmd = os.system("sudo apt-get install amap")
                        tools1hacking()
                    elif hackingop == "4":
                		cmd = os.system("sudo apt-get install automater")
                    elif hackingop == "5":
        				cmd = os.system("sudo wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                    elif hackingop == "6":
            			cmd = os.system("sudo apt-get install braa")
                    elif hackingop == "7":
                        cmd = os.system("sudo apt-get install casefile")
                        tools1hacking()
                    elif hackingop == "8":
            		    cmd = os.system("sudo apt-get install cdpsnarf")
                    elif hackingop == "9":
        				cmd = os.system("sudo apt-get install cisco-torch")
                    elif hackingop == "10":
            			cmd = os.system("sudo apt-get install cookie-cadger")
                    elif hackingop == "11":
                		cmd = os.system("sudo apt-get install copy-router-config")
                    elif hackingop == "12":
                        cmd = os.system("sudo apt-get install dmitry")
                        tools1hacking()
                    elif hackingop == "13":
                        cmd = os.system("sudo apt-get install dnmap")
                        tools1hacking()
                    elif hackingop == "14":
                        cmd = os.system("sudo apt-get install dnsenum")
                        tools1hacking()
                    elif hackingop == "15":
                        cmd = os.system("sudo apt-get install dnsmap")
                        tools1hacking()
                    elif hackingop == "16":
                        cmd = os.system("sudo apt-get install dnsrecon")
                        tools1hacking()
                    elif hackingop == "17":
                        cmd = os.system("sudo apt-get install dnstracer")
                        tools1hacking()
                    elif hackingop == "18":
                        cmd = os.system("sudo apt-get install dnswalk")
                        tools1hacking()
                    elif hackingop == "19":
                        cmd = os.system("sudo apt-get install dotdotpwn")
                        tools1hacking()
                    elif hackingop == "20":
                        cmd = os.system("sudo apt-get install enum4linux")
                        tools1hacking()
                    elif hackingop == "21":
                        cmd = os.system("sudo apt-get install enumiax")
                        tools1hacking()
                    elif hackingop == "22":
                        cmd = os.system("sudo apt-get install exploitdb")
                        tools1hacking()
                    elif hackingop == "23":
                        cmd = os.system("sudo apt-get install fierce")
                        tools1hacking()
                    elif hackingop == "24":
                        cmd = os.system("sudo apt-get install firewalk")
                        tools1hacking()
                    elif hackingop == "25":
                        cmd = os.system("sudo apt-get install fragroute")
                        tools1hacking()
                    elif hackingop == "26":
                        cmd = os.system("sudo apt-get install fragrouter")
                        tools1hacking()
                    elif hackingop == "27":
                        cmd = os.system("sudo apt-get install ghost-phisher")
                        tools1hacking()
                    elif hackingop == "28":
                        cmd = os.system("sudo apt-get install golismero")
                        tools1hacking()
                    elif hackingop == "29":
                        cmd = os.system("sudo apt-get install goofile")
                        tools1hacking()
                    elif hackingop == "30":
                        cmd = os.system("sudo apt-get install lbd")
                        tools1hacking()
                    elif hackingop == "31":
                        cmd = os.system("sudo apt-get install maltego-teeth")
                        tools1hacking()
                    elif hackingop == "32":
                        cmd = os.system("sudo apt-get install masscan")
                        tools1hacking()
                    elif hackingop == "33":
                        cmd = os.system("sudo apt-get install metagoofil")
                        tools1hacking()
                    elif hackingop == "34":
                        cmd = os.system("sudo apt-get install miranda")
                        tools1hacking()
                    elif hackingop == "35":
                        cmd = os.system("sudo apt-get install nmap")
                        tools1hacking()
                    elif hackingop == "36":
                        cmd = os.system("sudo apt-get install p0f")
                        tools1hacking()
                    elif hackingop == "37":
                        cmd = os.system("sudo apt-get install parsero")
                        tools1hacking()
                    elif hackingop == "38":
                        cmd = os.system("sudo apt-get install recon-ng")
                        tools1hacking()
                    elif hackingop == "39":
                        cmd = os.system("sudo apt-get install set")
                        tools1hacking()
                    elif hackingop == "40":
                        cmd = os.system("sudo apt-get install smtp-user-enum")
                        tools1hacking()
                    elif hackingop == "41":
                        cmd = os.system("sudo apt-get install snmpcheck")
                        tools1hacking()
                    elif hackingop == "42":
                        cmd = os.system("sudo apt-get install sslcaudit")
                        tools1hacking()
                    elif hackingop == "43":
                        cmd = os.system("sudo apt-get install sslsplit")
                        tools1hacking()
                    elif hackingop == "44":
                        cmd = os.system("sudo apt-get install sslstrip")
                        tools1hacking()
                    elif hackingop == "45":
                        cmd = os.system("sudo apt-get install sslyze")
                        tools1hacking()
                    elif hackingop == "46":
                        cmd = os.system("sudo apt-get install thc-ipv6")
                        tools1hacking()
                    elif hackingop == "47":
                        cmd = os.system("sudo apt-get install theharvester")
                        tools1hacking()
                    elif hackingop == "48":
                        cmd = os.system("sudo apt-get install tlssled")
                        tools1hacking()
                    elif hackingop == "49":
                        cmd = os.system("sudo apt-get install twofi")
                        tools1hacking()
                    elif hackingop == "50":
                        cmd = os.system("sudo apt-get install urlcrazy")
                        tools1hacking()
                    elif hackingop == "51":
                        cmd = os.system("sudo apt-get install wireshark")
                        tools1hacking()
                    elif hackingop == "52":
                        cmd = os.system("sudo apt-get install wol-e")
                        tools1hacking()
                    elif hackingop == "53":
                        cmd = os.system("sudo apt-get install xplico")
                        tools1hacking()
                    elif hackingop == "54":
                        cmd = os.system("sudo apt-get install ismtp")
                        tools1hacking()
                    elif hackingop == "55":
                        cmd = os.system("sudo apt-get install intrace")
                        tools1hacking()
                    elif hackingop == "56":
                        cmd = os.system("sudo apt-get install hping3")
                        tools1hacking()
                    elif hackingop == "0":
                        cmd = os.system("sudo apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                tools1hacking()
                mistools()
            elif hacking == "2":
                def tools2():
                    logo()
                    print '''
        \033[1;91m#########################################################\033[1;m
        \033[1;91m# \t\tAnalisis De Vulnerabilidades\t\t#\033[1;m
        \033[1;91m#########################################################\033[1;m
        \033[1;36m
         1.- BBQSQL                       18.- Nmap
         2.- BED                          19.- ohrwurm
         3.- cisco-auditing-tool          20.- openvas-administrator
         4.- cisco-global-exploiter       21.- openvas-cli
         5.- cisco-ocs                    22.- openvas-manager
         6.- cisco-torch                  23.- openvas-scanner
         7.- copy-router-config           24.- Oscanner
         8.- commix                       25.- Powerfuzzer
         9.- DBPwAudit                    26.- sfuzz
        10.- DoonaDot                     27.- SidGuesser
        11.- DotPwn                       28.- SIPArmyKnife
        12.- Greenbone Security Assistant 29.- sqlmap
        13.- GSD                          30.- Sqlninja
        14.- HexorBase                    31.- sqlsus
        15.- Inguma                       32.- THC-IPV6
        16.- jSQL                         33.- tnscmd10g
        17.- Lynis                        34.- unix-privesc-check
                                         35.- Yersinia

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m                 
                                '''
                    hackingop2 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop2 == "1":
                        cmd = os.system("sudo apt-get install bbqsql")
                        tools2()
                    elif hackingop2 == "back":
                        mistools()
                    elif hackingop2 == "2":
                        cmd = os.system("sudo apt-get install bed")
                        tools2()
                    elif hackingop2 == "3":
                        cmd = os.system("sudo apt-get install cisco-auditing-tool")
                        tools2()
                    elif hackingop2 == "4":
                        cmd = os.system("sudo apt-get install cisco-global-exploiter")
                        tools2()
                    elif hackingop2 == "5":
                        cmd = os.system("sudo apt-get install cisco-ocs")
                        tools2()
                    elif hackingop2 == "6":
                        cmd = os.system("sudo apt-get install cisco-torch")
                        tools2()
                    elif hackingop2 == "7":
                        cmd = os.system("sudo apt-get install copy-router-config")
                        tools2()
                    elif hackingop2 == "8":
                        cmd = os.system("sudo apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
                        tools2()
                    elif hackingop2 == "9":
                        md = os.system("sudo echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
                        tools2()
                    elif hackingop2 == "10":
                        cmd = os.system("sudo apt-get install doona")
                        tools2()
                    elif hackingop2 == "11":
                        cmd = os.system("sudo apt-get install dotdotpwn")
                        tools2()
                    elif hackingop2 == "12":
                        cmd = os.system("sudo apt-get install greenbone-security-assistant")
                        tools2()
                    elif hackingop2 == "13":
                        cmd = os.system("sudo apt-get install git && git clone git://git.kali.org/packages/gsd.git")
                        tools2()
                    elif hackingop2 == "14":
                        cmd = os.system("sudo apt-get install hexorbase")
                        tools2()
                    elif hackingop2 == "15":
                        cmd = os.system("sudo apt-get install inguma")
                        tools2()
                    elif hackingop2 == "16":
                        cmd = os.system("sudo apt-get install jsql")
                        tools2()
                    elif hackingop2 == "17":
                        cmd = os.system("sudo apt-get install lynis")
                        tools2()
                    elif hackingop2 == "18":
                        cmd = os.system("sudo apt-get install nmap")
                        tools2()
                    elif hackingop2 == "19":
                        cmd = os.system("sudo apt-get install ohrwurm")
                        tools2()
                    elif hackingop2 == "20":
                        cmd = os.system("sudo apt-get install openvas-administrator")
                        tools2()
                    elif hackingop2 == "21":
                        cmd = os.system("sudo apt-get install openvas-cli")
                        tools2()
                    elif hackingop2 == "22":
                        cmd = os.system("sudo apt-get install openvas-manager")
                        tools2()
                    elif hackingop2 == "23":
                        cmd = os.system("sudo apt-get install openvas-scanner")
                        tools2()
                    elif hackingop2 == "24":
                        cmd = os.system("sudo apt-get install oscanner")
                        tools2()
                    elif hackingop2 == "25":
                        cmd = os.system("sudo apt-get install powerfuzzer")
                        tools2()
                    elif hackingop2 == "26":
                        cmd = os.system("sudo apt-get install sfuzz")
                        tools2()
                    elif hackingop2 == "27":
                        cmd = os.system("sudo apt-get install sidguesser")
                        tools2()
                    elif hackingop2 == "28":
                        cmd = os.system("sudo apt-get install siparmyknife")
                        tools2()
                    elif hackingop2 == "29":
                        cmd = os.system("sudo apt-get install sqlmap")
                        tools2()
                    elif hackingop2 == "30":
                        cmd = os.system("sudo apt-get install sqlninja")
                        tools2()
                    elif hackingop2 == "31":
                        cmd = os.system("sudo apt-get install sqlsus")
                        tools2()
                    elif hackingop2 == "32":
                        cmd = os.system("sudo apt-get install thc-ipv6")
                        tools2()
                    elif hackingop2 == "33":
                        cmd = os.system("sudo apt-get install tnscmd10g")
                        tools2()
                    elif hackingop2 == "34":
                        cmd = os.system("sudo apt-get install unix-privesc-check")
                        tools2()
                    elif hackingop2 == "35":
                        cmd = os.system("sudo apt-get install yersinia")
                        tools2()
                    elif hackingop2 == "0":
                        cmd = os.system("sudo apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools2()
            elif hacking == "3":
                def tools3():
                    logo()
                    print '''
        \033[1;91m#################################################\033[1;m
        \033[1;91m# \t\tAplicaciones Web\t\t#\033[1;m
        \033[1;91m#################################################\033[1;m
        \033[1;36m
         1.- apache-users        21.- Parsero
         2.- Arachni             22.- plecost
         3.- BBQSQL              23.- Powerfuzzer
         4.- BlindElephant       24.- ProxyStrike
         5.- Burp Suite          25.- Recon-ng
         6.- commix              26.- Skipfish
         7.- CutyCapt            27.- sqlmap
         8.- DAVTest             28.- Sqlninja
         9.- deblaze             29.- sqlsus
        10.- DIRB                30.- ua-tester
        11.- DirBuster           31.- Uniscan
        12.- fimap               32.- Vega
        13.- FunkLoad            33.- WebScarab
        14.- Grabber             34.- WebSploit
        15.- jboss-autopwn       35.- Wfuzz
        16.- joomscan            36.- WPScan
        17.- jSQL                37.- XSSer
        18.- Maltego Teeth       38.- zaproxy
        19.- PadBuster           
        20.- Paros               
                                

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m                 
                                '''

                    hackingop3 = raw_input("\033[1;92m> \033[1;m")

                    if hackingop3 == "1":
                        cmd = os.system("sudo apt-get install apache-users")
                        tools3()
                    elif hackingop3 == "back":
                        mistools()
                    elif hackingop3 == "2":
                        cmd = os.system("sudo apt-get install arachni")
                        tools3()
                    elif hackingop3 == "3":
                        cmd = os.system("sudo apt-get install bbqsql")
                        tools3()
                    elif hackingop3 == "4":
                        cmd = os.system("sudo apt-get install blindelephant")
                        tools3()
                    elif hackingop3 == "5":
                        cmd = os.system("sudo apt-get install burpsuite")
                        tools3()
                    elif hackingop3 == "6":
                        cmd = os.system("sudo apt-get install cutycapt")
                        tools3()
                    elif hackingop3 == "7":
                        cmd = os.system("sudo apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
                        tools3()
                    elif hackingop3 == "8":
                        cmd = os.system("sudo apt-get install davtest")
                        tools3()
                    elif hackingop3 == "9":
                        cmd = os.system("sudo apt-get install deblaze")
                        tools3()
                    elif hackingop3 == "10":
                        cmd = os.system("sudo apt-get install dirb")
                        tools3()
                    elif hackingop3 == "11":
                        cmd = os.system("sudo apt-get install dirbuster")
                        tools3()
                    elif hackingop3 == "12":
                        cmd = os.system("sudo apt-get install fimap")
                        tools3()
                    elif hackingop3 == "13":
                        cmd = os.system("sudo apt-get install funkload")
                        tools3()
                    elif hackingop3 == "14":
                        cmd = os.system("sudo apt-get install grabber")
                        tools3()
                    elif hackingop3 == "15":
                        cmd = os.system("sudo apt-get install jboss-autopwn")
                        tools3()
                    elif hackingop3 == "16":
                        cmd = os.system("sudo apt-get install joomscan")
                        tools3()
                    elif hackingop3 == "17":
                        cmd = os.system("sudo apt-get install jsql")
                        tools3()
                    elif hackingop3 == "18":
                        cmd = os.system("sudo apt-get install maltego-teeth")
                        tools3()
                    elif hackingop3 == "19":
                        cmd = os.system("sudo apt-get install padbuster")
                        tools3()
                    elif hackingop3 == "20":
                        cmd = os.system("sudo apt-get install paros")
                        tools3()
                    elif hackingop3 == "21":
                        cmd = os.system("sudo apt-get install parsero")
                        tools3()
                    elif hackingop3 == "22":
                        cmd = os.system("sudo apt-get install plecost")
                        tools3()
                    elif hackingop3 == "23":
                        cmd = os.system("sudo apt-get install powerfuzzer")
                        tools3()
                    elif hackingop3 == "24":
                        cmd = os.system("sudo apt-get install proxystrike")
                        tools3()
                    elif hackingop3 == "25":
                        cmd = os.system("sudo apt-get install recon-ng")
                        tools3()
                    elif hackingop3 == "26":
                        cmd = os.system("sudo apt-get install skipfish")
                        tools3()
                    elif hackingop3 == "27":
                        cmd = os.system("sudo apt-get install sqlmap")
                        tools3()
                    elif hackingop3 == "28":
                        cmd = os.system("sudo apt-get install sqlninja")
                        tools3()
                    elif hackingop3 == "29":
                        cmd = os.system("sudo apt-get install sqlsus")
                        tools3()
                    elif hackingop3 == "30":
                        cmd = os.system("sudo apt-get install ua-tester")
                        tools3()
                    elif hackingop3 == "31":
                        cmd = os.system("sudo apt-get install uniscan")
                        tools3()
                    elif hackingop3 == "32":
                        cmd = os.system("sudo apt-get install vega")
                        tools3()
                    elif hackingop3 == "33":
                        cmd = os.system("sudo apt-get install webscarab")
                        tools3()
                    elif hackingop3 == "34":
                        cmd = os.system("sudo apt-get install websploit")
                        tools3()
                    elif hackingop3 == "35":
                        cmd = os.system("sudo apt-get install wfuzz")
                        tools3()
                    elif hackingop3 == "36":
                        cmd = os.system("sudo apt-get install wpscan")
                        tools3()
                    elif hackingop3 == "37":
                        cmd = os.system("sudo apt-get install xsser")
                        tools3()
                    elif hackingop3 == "38":
                        cmd = os.system("sudo apt-get install zaproxy")
                        tools3()
                    elif hackingop3 == "0":
                        cmd = os.system("sudo apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega webscarab websploit wfuzz wpscan xsser zaproxy")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools3()
            elif hacking == "4":
                def tools4():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \t\tBases De Datos\t\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m
         1.- bbqsql
         2.- hexorbase
         3.- Jsql
         4.- sqlmap
         5.- sqlninja
         6.- sqlsus

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m
                    '''
                    hackingop4 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop4 == "1":
                        cmd = os.system("sudo apt-get install bbqsql")
                        tools4()
                    elif hackingop4 == "back":
                        mistools()
                    elif hackingop4 == "2":
                        cmd = os.system("sudo apt-get install hexorbase")
                        tools4()
                    elif hackingop4 == "3":
                        cmd = os.system("sudo apt-get install jsql")
                        tools4()
                    elif hackingop4 == "4":
                        cmd = os.system("sudo apt-get install sqlmap")
                        tools4()
                    elif hackingop4 == "5":
                        cmd = os.system("sudo apt-get install sqlninja")
                        tools4()
                    elif hackingop4 == "6":
                        cmd = os.system("sudo apt-get install sqlsus")
                        tools4()
                    elif hackingop4 == "0":
                        cmd = os.system("sudo apt-get install -y bbqsql hexorbase jsql sqlmap sqlninja sqlsus")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools4()
            elif hacking == "5":
                def tools5():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tAtaques A Contraseñas\t\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

        1.- acccheck             18.- Maskprocessor
        2.- Burp Suite           19.- Ncrack
        3.- CeWL                 20.- oclgausscrack
        4.- chntpw               21.- PACK
        5.- cisco-auditing-tool  22.- patator 
        6.- CmosPwd              23.- polenum
        7.- creddump             24.- RainbowCrack
        8.- crunch               25.- rcracki-mt
        9.- DBPwAudit            26.- RSMangler
        10.- findmyhash          27.- SQLdict
        11.- gpp-decrypt         28.- Statsprocessor
        12.- hash-identifier     29.- THC-pptp-bruter
        13.- HexorBase           30.- TrueCrack 
        14.- John the Ripper     31.- WebScarab
        15.- Johnny              32.- wordlists     
        16.- keimpx              33.- zaproxy
        17.- Maltego Teeth            
                                 

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m
                    '''
                    hackingop5 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop5 == "1":
                        cmd = os.system("sudo apt-get install acccheck")
                        tools5()
                    elif hackingop5 == "back":
                        mistools()
                    elif hackingop5 == "2":
                        cmd = os.system("sudo apt-get install burpsuite")
                        tools5()
                    elif hackingop5 == "3":
                        cmd = os.system("sudo apt-get install cewl")
                        tools5()
                    elif hackingop5 == "4":
                        cmd = os.system("sudo apt-get install chntpw")
                        tools5()
                    elif hackingop5 == "5":
                        cmd = os.system("sudo apt-get install cisco-auditing-tool")
                        tools5()
                    elif hackingop5 == "6":
                        cmd = os.system("sudo apt-get install cmospwd")
                        tools5()
                    elif hackingop5 == "7":
                        cmd = os.system("sudo apt-get install creddump")
                        tools5()
                    elif hackingop5 == "8":
                        cmd = os.system("sudo apt-get install crunch")
                        tools5()
                    elif hackingop5 == "9":
                        cmd = os.system("sudo apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
                        tools5()
                    elif hackingop5 == "10":
                        cmd = os.system("sudo apt-get install findmyhash")
                        tools5()
                    elif hackingop5 == "11":
                        cmd = os.system("sudo apt-get install gpp-decrypt")
                        tools5()
                    elif hackingop5 == "12":
                        cmd = os.system("sudo apt-get install hash-identifier")
                        tools5()
                    elif hackingop5 == "13":
                        cmd = os.system("sudo apt-get install hexorbase")
                        tools5()
                    elif hackingop5 == "14":
                        cmd = os.system("sudo apt-get install john")
                        tools5()
                    elif hackingop5 == "15":
                        cmd = os.system("sudo apt-get install johnny")
                        tools5()
                    elif hackingop5 == "16":
                        cmd = os.system("sudo apt-get install keimpx")
                        tools5()
                    elif hackingop5 == "17":
                        cmd = os.system("sudo apt-get install maltego-teeth")
                        tools5()
                    elif hackingop5 == "18":
                        cmd = os.system("sudo apt-get install maskprocessor")
                        tools5()
                    elif hackingop5 == "19":
                        cmd = os.system("sudo apt-get install ncrack")
                        tools5()
                    elif hackingop5 == "20":
                        cmd = os.system("sudo apt-get install oclgausscrack")
                        tools5()
                    elif hackingop5 == "21":
                        cmd = os.system("sudo apt-get install pack")
                        tools5()
                    elif hackingop5 == "22":
                        cmd = os.system("sudo apt-get install patator")
                        tools5()
                    elif hackingop5 == "23":
                        cmd = os.system("sudo apt-get install polenum")
                        tools5()
                    elif hackingop5 == "24":
                        cmd = os.system("sudo apt-get install rainbowcrack")
                        tools5()
                    elif hackingop5 == "25":
                        cmd = os.system("sudo apt-get install rcracki-mt")
                        tools5()
                    elif hackingop5 == "26":
                        cmd = os.system("sudo apt-get install rsmangler")
                        tools5()
                    elif hackingop5 == "27":
                        cmd = os.system("sudo apt-get install sqldict")
                        tools5()
                    elif hackingop5 == "28":
                        cmd = os.system("sudo apt-get install statsprocessor")
                        tools5()
                    elif hackingop5 == "29":
                        cmd = os.system("sudo apt-get install thc-pptp-bruter")
                        tools5()
                    elif hackingop5 == "30":
                        cmd = os.system("sudo apt-get install truecrack")
                        tools5()
                    elif hackingop5 == "31":
                        cmd = os.system("sudo apt-get install webscarab")
                        tools5()
                    elif hackingop5 == "32":
                        cmd = os.system("sudo apt-get install wordlists")
                        tools5()
                    elif hackingop5 == "33":
                        cmd = os.system("sudo apt-get install zaproxy")
                        tools5()
                    elif hackingop5 == "0":
                        cmd = os.system("sudo apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor ncrack oclgausscrack sqldict pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools5()
            elif hacking == "6":
                def tools6():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tAtaques Wireless\t\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

         1) Aircrack-ng         16) kalibrate-rtl      31) Wifitap
         2) Asleap              17) KillerBee
         3) Bluelog             18) Kismet
         4) BlueMaho            19) mdk3
         5) Bluepot             20) mfcuk
         6) BlueRanger          21) mfoc
         7) Bluesnarfer         22) mfterm
         8) Bully               23) Multimon-NG
         9) coWPAtty            24) PixieWPS
        10) crackle             25) Reaver
        11) eapmd5pass          26) redfang
        12) Fern Wifi Cracker   27) RTLSDR Scanner
        13) Ghost Phisher       28) Spooftooph
        14) GISKismet           29) Wifi Honey              
        15) gr-scan             30) Wifite 

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m
                                '''
                    hackingop6 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop6 == "1":
                        cmd = os.system("sudo apt-get install aircrack-ng")
                        tools6()
                    elif hackingop6 == "back":
                        mistools()
                    elif hackingop6 == "2":
                        cmd = os.system("sudo apt-get install asleap")
                        tools6()
                    elif hackingop6 == "3":
                        cmd = os.system("sudo apt-get install bluelog")
                        tools6()
                    elif hackingop6 == "4":
                        cmd = os.system("sudo apt-get install git && git clone git://git.kali.org/packages/bluemaho.git")
                        tools6()
                    elif hackingop6 == "5":
                        cmd = os.system("sudo apt-get install git && git clone git://git.kali.org/packages/bluepot.git")
                        tools6()
                    elif hackingop6 == "6":
                        cmd = os.system("sudo apt-get install blueranger")
                        tools6()
                    elif hackingop6 == "7":
                        cmd = os.system("sudo apt-get install bluesnarfer")
                        tools6()
                    elif hackingop6 == "8":
                        cmd = os.system("sudo apt-get install bully")
                        tools6()
                    elif hackingop6 == "9":
                        cmd = os.system("sudo apt-get install cowpatty")
                        tools6()
                    elif hackingop6 == "10":
                        cmd = os.system("sudo apt-get install crackle")
                        tools6()
                    elif hackingop6 == "11":
                        cmd = os.system("sudo apt-get install eapmd5pass")
                        tools6()
                    elif hackingop6 == "12":
                        cmd = os.system("sudo apt-get install fern-wifi-cracker")
                        tools6()
                    elif hackingop6 == "13":
                        cmd = os.system("sudo apt-get install ghost-phisher")
                        tools6()
                    elif hackingop6 == "14":
                        cmd = os.system("sudo apt-get install giskismet")
                        tools6()
                    elif hackingop6 == "15":
                        cmd = os.system("sudo apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
                        tools6()
                    elif hackingop6 == "16":
                        cmd = os.system("sudo apt-get install kalibrate-rtl")
                        tools6()
                    elif hackingop6 == "17":
                        cmd = os.system("sudo apt-get install killerbee")
                        tools6()
                    elif hackingop6 == "18":
                        cmd = os.system("sudo apt-get install kismet")
                        tools6()
                    elif hackingop6 == "19":
                        cmd = os.system("sudo apt-get install mdk3")
                        tools6()
                    elif hackingop6 == "20":
                        cmd = os.system("sudo apt-get install mfcuk")
                        tools6()
                    elif hackingop6 == "21":
                        cmd = os.system("sudo apt-get install mfoc")
                        tools6()
                    elif hackingop6 == "22":
                        cmd = os.system("sudo apt-get install mfterm")
                        tools6()
                    elif hackingop6 == "23":
                        cmd = os.system("sudo apt-get install multimon-ng")
                        tools6()
                    elif hackingop6 == "24":
                        cmd = os.system("sudo apt-get install pixiewps")
                        tools6()
                    elif hackingop6 == "25":
                        cmd = os.system("sudo apt-get install reaver")
                        tools6()
                    elif hackingop6 == "26":
                        cmd = os.system("sudo apt-get install redfang")
                        tools6()
                    elif hackingop6 == "27":
                        cmd = os.system("sudo apt-get install rtlsdr-scanner")
                        tools6()
                    elif hackingop6 == "28":
                        cmd = os.system("sudo apt-get install spooftooph")
                        tools6()
                    elif hackingop6 == "29":
                        cmd = os.system("sudo apt-get install wifi-honey")
                        tools6()
                    elif hackingop6 == "30":
                        cmd = os.system("sudo apt-get install wifitap")
                        tools6()
                    elif hackingop6 == "31":
                        cmd = os.system("sudo apt-get install wifite")
                        tools6()
                    elif hackingop6 == "0":
                        cmd = os.system("sudo apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools6()
            elif hacking == "7":
                def tools7():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tIngenieria Inversa\t\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

         1.- apktool
         2.- dex2jar
         3.- diStorm3
         4.- edb-debugger
         5.- jad 
         6.- javasnoop
         7.- JD-GUI
         8.- OllyDbg
         9.- smali
        10.- Valgrind
        11.- YARA

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m                
                    '''
                    hackingop7 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop7 == "1":
                        cmd = os.system("sudo apt-get install apktool")
                        tools7()
                    elif hackingop7 == "back":
                        mistools()
                    elif hackingop7 == "2":
                        cmd = os.system("sudo apt-get install dex2jar")
                        tools7()
                    elif hackingop7 == "3":
                        cmd = os.system("sudo apt-get install python-diStorm3")
                        tools7()
                    elif hackingop7 == "4":
                        cmd = os.system("sudo apt-get install edb-debugger")
                        tools7()
                    elif hackingop7 == "5":
                        cmd = os.system("sudo apt-get install jad")
                        tools7()
                    elif hackingop7 == "6":
                        cmd = os.system("sudo apt-get install javasnoop")
                        tools7()
                    elif hackingop7 == "7":
                        cmd = os.system("sudo apt-get install JD")
                        tools7()
                    elif hackingop7 == "8":
                        cmd = os.system("sudo apt-get install OllyDbg")
                        tools7()
                    elif hackingop7 == "9":
                        cmd = os.system("sudo apt-get install smali")
                        tools7()
                    elif hackingop7 == "10":
                        cmd = os.system("sudo apt-get install Valgrind")
                        tools7()
                    elif hackingop7 == "11":
                        cmd = os.system("sudo apt-get install YARA")
                        tools7()
                    elif hackingop7 == "0":
                        cmd = os.system("sudo apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools7()
            elif hacking == "8":
                def tools8():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tHerramientas De Explotacion\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

         1.- Armitage
         2.- Backdoor Factory
         3.- BeEF
         4.- cisco-auditing-tool
         5.- cisco-global-exploiter  
         6.- cisco-ocs
         7.- cisco-torch
         8.- commix
         9.- crackle
        10.- jboss-autopwn
        11.- Linux Exploit Suggester
        12.- Maltego Teeth
        13.- SET
        14.- ShellNoob
        15.- sqlmap
        16.- THC-IPV6
        17.- Yersinia

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m        
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m      
                          '''
                    hackingop8 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop8 == "1":
                        cmd = os.system("sudo apt-get install armitage")
                        tools8()
                    elif hackingop8 == "back":
                        mistools()
                    elif hackingop8 == "2":
                        cmd = os.system("sudo apt-get install backdoor-factory")
                        tools8()
                    elif hackingop8 == "3":
                        cmd = os.system("sudo apt-get install beef-xss")
                        tools8()
                    elif hackingop8 == "4":
                        cmd = os.system("sudo apt-get install cisco-auditing-tool")
                        tools8()
                    elif hackingop8 == "5":
                        cmd = os.system("sudo apt-get install cisco-global-exploiter")
                        tools8()
                    elif hackingop8 == "6":
                        cmd = os.system("sudo apt-get install cisco-ocs")
                        tools8()
                    elif hackingop8 == "7":
                        cmd = os.system("sudo apt-get install cisco-torch")
                        tools8()
                    elif hackingop8 == "8":
                        cmd = os.system("sudo apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
                        tools8()
                    elif hackingop8 == "9":
                        cmd = os.system("sudo apt-get install crackle")
                        tools8()
                    elif hackingop8 == "10":
                        cmd = os.system("sudo apt-get install jboss-autopwn")
                        tools8()
                    elif hackingop8 == "11":
                        cmd = os.system("sudo apt-get install linux-exploit-suggester")
                        tools8()
                    elif hackingop8 == "12":
                        cmd = os.system("sudo apt-get install maltego-teeth")
                        tools8()
                    elif hackingop8 == "13":
                        cmd = os.system("sudo apt-get install set")
                        tools8()
                    elif hackingop8 == "14":
                        cmd = os.system("sudo apt-get install shellnoob")
                        tools8()
                    elif hackingop8 == "15":
                        cmd = os.system("sudo apt-get install sqlmap")
                        tools8()
                    elif hackingop8 == "16":
                        cmd = os.system("sudo apt-get install thc-ipv6")
                        tools8()
                    elif hackingop8 == "17":
                        cmd = os.system("sudo apt-get install yersinia")
                        tools8()
                    elif hackingop8 == "0":
                        cmd = os.system("sudo apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools8()
            elif hacking == "9":
                def tools9():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \t    Husmeando Envenenando\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

         1.- Burp Suite              17.- rtpmixsound
         2.- DNSChef                 18.- sctpscan
         3.- fiked                   19.- SIPArmyKnife
         4.- hamster-sidejack        20.- SIPp
         5.- HexInject               21.- SIPVicious
         6.- iaxflood                22.- SniffJoke
         7.- inviteflood             23.- SSLsplit
         8.- iSMTP                   24.- sslstrip
         9.- isr-evilgrade           25.- THC-IPV6
        10.- mitmproxy               26.- VoIPHopper
        11.- ohrwurm                 27.- WebScarab
        12.- protos-sip              28.- Wifi Honey
        13.- rebind                  29.- Wireshark
        14.- responder               30.- xspy
        15.- rtpbreak                31.- Yersinia
        16.- rtpinsertsound          32.- zaproxy 

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m

                                '''
                    hackingop9 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop9 == "1":
                        cmd = os.system("sudo apt-get install burpsuite")
                        tools9()
                    elif hackingop9 == "back":
                        mistools()
                    elif hackingop9 == "2":
                        cmd = os.system("sudo apt-get install dnschef")
                        tools9()
                    elif hackingop9 == "3":
                        cmd = os.system("sudo apt-get install fiked")
                        tools9()
                    elif hackingop9 == "4":
                        cmd = os.system("sudo apt-get install hamster-sidejack")
                        tools9()
                    elif hackingop9 == "5":
                        cmd = os.system("sudo apt-get install hexinject")
                        tools9()
                    elif hackingop9 == "6":
                        cmd = os.system("sudo apt-get install iaxflood")
                        tools9()
                    elif hackingop9 == "7":
                        cmd = os.system("sudo apt-get install inviteflood")
                        tools9()
                    elif hackingop9 == "8":
                        cmd = os.system("sudo apt-get install ismtp")
                        tools9()
                    elif hackingop9 == "9":
                        cmd = os.system("sudo apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
                        tools9()
                    elif hackingop9 == "10":
                        cmd = os.system("sudo apt-get install mitmproxy")
                        tools9()
                    elif hackingop9 == "11":
                        cmd = os.system("sudo apt-get install ohrwurm")
                        tools9()
                    elif hackingop9 == "12":
                        cmd = os.system("sudo apt-get install protos-sip")
                        tools9()
                    elif hackingop9 == "13":
                        cmd = os.system("sudo apt-get install rebind")
                        tools9()
                    elif hackingop9 == "14":
                        cmd = os.system("sudo apt-get install responder")
                        tools9()
                    elif hackingop9 == "15":
                        cmd = os.system("sudo apt-get install rtpbreak")
                        tools9()
                    elif hackingop9 == "16":
                        cmd = os.system("sudo apt-get install rtpinsertsound")
                        tools9()
                    elif hackingop9 == "17":
                        cmd = os.system("sudo apt-get install rtpmixsound")
                        tools9()
                    elif hackingop9 == "18":
                        cmd = os.system("sudo apt-get install sctpscan")
                        tools9()
                    elif hackingop9 == "19":
                        cmd = os.system("sudo apt-get install siparmyknife")
                        tools9()
                    elif hackingop9 == "20":
                        cmd = os.system("sudo apt-get install sipp")
                        tools9()
                    elif hackingop9 == "21":
                        cmd = os.system("sudo apt-get install sipvicious")
                        tools9()
                    elif hackingop9 == "22":
                        cmd = os.system("sudo apt-get install sniffjoke")
                        tools9()
                    elif hackingop9 == "23":
                        cmd = os.system("sudo apt-get install sslsplit")
                        tools9()
                    elif hackingop9 == "24":
                        cmd = os.system("sudo apt-get install sslstrip")
                        tools9()
                    elif hackingop9 == "25":
                        cmd = os.system("sudo apt-get install thc-ipv6")
                        tools9()
                    elif hackingop9 == "26":
                        cmd = os.system("sudo apt-get install voiphopper")
                        tools9()
                    elif hackingop9 == "27":
                        cmd = os.system("sudo apt-get install webscarab")
                        tools9()
                    elif hackingop9 == "28":
                        cmd = os.system("sudo apt-get install wifi-honey")
                        tools9()
                    elif hackingop9 == "29":
                        cmd = os.system("sudo apt-get install wireshark")
                        tools9()
                    elif hackingop9 == "30":
                        cmd = os.system("sudo apt-get install xspy")
                        tools9()
                    elif hackingop9 == "31":
                        cmd = os.system("sudo apt-get install yersinia")
                        tools9()
                    elif hackingop9 == "32":
                        cmd = os.system("sudo apt-get install zaproxy")
                        tools9()
                    elif hackingop9 == "0":
                        cmd = os.system("apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools9()
            elif hacking == "10":
                def tools10():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tMateniendo Acceso\t        #\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m
         1.- CryptCat
         2.- Cymothoa
         3.- dbd
         4.- dns2tcp
         5.- http-tunnel 
         6.- HTTPTunnel
         7.- Intersect
         8.- Nishang
         9.- polenum
        10.- PowerSploit
        11.- pwnat
        12.- RidEnum
        13.- sbd
        14.- U3-Pwn
        15.- Webshells
        16.- Weevely

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m

                    '''
                    hackingop10 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop10 == "1":
                        cmd = os.system("sudo apt-get install cryptcat")
                        tools10()
                    elif hackingop10 == "back":
                        mistools()
                    elif hackingop10 == "2":
                        cmd = os.system("sudo apt-get install cymothoa")
                        tools10()
                    elif hackingop10 == "3":
                        cmd = os.system("sudo apt-get install dbd")
                        tools10()
                    elif hackingop10 == "4":
                        cmd = os.system("sudo apt-get install dns2tcp")
                        tools10()
                    elif hackingop10 == "5":
                        cmd = os.system("sudo apt-get install http-tunnel")
                        tools10()
                    elif hackingop10 == "6":
                        cmd = os.system("sudo apt-get install httptunnel")
                        tools10()
                    elif hackingop10 == "7":
                        cmd = os.system("sudo apt-get install intersect")
                        tools10()
                    elif hackingop10 == "8":
                        cmd = os.system("sudo apt-get install nishang")
                        tools10()
                    elif hackingop10 == "9":
                        cmd = os.system("sudo apt-get install polenum")
                        tools10()
                    elif hackingop10 == "10":
                        cmd = os.system("sudo apt-get install powersploit")
                        tools10()
                    elif hackingop10 == "11":
                        cmd = os.system("sudo apt-get install pwnat")
                        tools10()
                    elif hackingop10 == "12":
                        cmd = os.system("sudo apt-get install ridenum")
                        tools10()
                    elif hackingop10 == "13":
                        cmd = os.system("sudo apt-get install sbd")
                        tools10()
                    elif hackingop10 == "14":
                        cmd = os.system("sudo apt-get install u3-pwn")
                        tools10()
                    elif hackingop10 == "15":
                        cmd = os.system("sudo apt-get install webshells")
                        tools10()
                    elif hackingop10 == "16":
                        cmd = os.system("sudo apt-get install weevely")
                        tools10()
                    elif hackingop10 == "0":
                        cmd = os.system("sudo apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools10()
            elif hacking == "11":
                def tools11():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tAnalisis Forense\t\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

         1.- Binwalk             14.- iPhone Backup Analyzer
         2.- bulk-extractor      15.- p0f
         3.- Capstone            16.- pdf-parser
         4.- chntpw              17.- pdfid
         5.- Cuckoo              18.- pdgmail
         6.- dc3dd               19.- peepdf
         7.- ddrescue            20.- RegRipper
         8.- diStorm3            21.- Volatility
         9.- Dumpzilla           22.- Xplico            
        10.- extundelete         
        11.- Foremost                        
        12.- Galleta                         
        13.- Guymager                         

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m

                    '''
                    hackingop11 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop11 == "1":
                        cmd = os.system("sudo apt-get install binwalk")
                        tools11()
                    elif hackingop11 == "back":
                        mistools()
                    elif hackingop11 == "2":
                        cmd = os.system("sudo apt-get install bulk-extractor")
                        tools11()
                    elif hackingop11 == "3":
                        cmd = os.system("sudo apt-get install git && git clone git://git.kali.org/packages/capstone.git")
                        tools11()
                    elif hackingop11 == "4":
                        cmd = os.system("sudo apt-get install chntpw")
                        tools11()
                    elif hackingop11 == "5":
                        cmd = os.system("sudo apt-get install cuckoo")
                        tools11()
                    elif hackingop11 == "6":
                        cmd = os.system("sudo apt-get install dc3dd")
                        tools11()
                    elif hackingop11 == "7":
                        cmd = os.system("sudo apt-get install ddrescue")
                        tools11()
                    elif hackingop11 == "8":
                        cmd = os.system("sudo apt-get install git && git clone git://git.kali.org/packages/distorm3.git")
                        tools11()
                    elif hackingop11 == "9":
                        cmd = os.system("sudo apt-get install dumpzilla")
                        tools11()
                    elif hackingop11 == "10":
                        cmd = os.system("sudo apt-get install extundelete")
                        tools11()
                    elif hackingop11 == "11":
                        cmd = os.system("sudo apt-get install foremost")
                        tools11()
                    elif hackingop11 == "12":
                        cmd = os.system("sudo apt-get install galleta")
                        tools11()
                    elif hackingop11 == "13":
                        cmd = os.system("sudo apt-get install guymager")
                        tools11()
                    elif hackingop11 == "14":
                        cmd = os.system("sudo apt-get install iphone-backup-analyzer")
                        tools11()
                    elif hackingop11 == "15":
                        cmd = os.system("sudo apt-get install p0f")
                        tools11()
                    elif hackingop11 == "16":
                        cmd = os.system("sudo apt-get install pdf-parser")
                        tools11()
                    elif hackingop11 == "17":
                        cmd = os.system("sudo apt-get install pdfid")
                        tools11()
                    elif hackingop11 == "18":
                        cmd = os.system("sudo apt-get install pdgmail")
                        tools11()
                    elif hackingop11 == "19":
                        cmd = os.system("sudo apt-get install peepdf")
                        tools11()
                    elif hackingop11 == "20":
                        cmd = os.system("sudo apt-get install regripper")
                        tools11()
                    elif hackingop11 == "21":
                        cmd = os.system("sudo apt-get install volatility")
                        tools11()
                    elif hackingop11 == "22":
                        cmd = os.system("sudo apt-get install xplico")
                        tools11()
                    elif hackingop11 == "0":
                        cmd = os.system("sudo apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue regripper dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools11()
            elif hacking == "12":
                def tools12():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tHerramientas De Reporte\t\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

        1.- CaseFile
        2.- CutyCapt
        3.- dos2unix
        4.- Dradis
        5.- KeepNote 
        6.- MagicTree
        7.- Metagoofil
        8.- Nipper-ng
        9.- pipal

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m                 
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m                        
                    '''
                    hackingop12 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop12 == "1":
                        cmd = os.system("sudo apt-get install casefile")
                        tools12()
                    elif hackingop12 == "back":
                        mistools()
                    elif hackingop12 == "2":
                        cmd = os.system("sudo apt-get install cutycapt")
                        tools12()
                    elif hackingop12 == "3":
                        cmd = os.system("sudo apt-get install dos2unix")
                        tools12()
                    elif hackingop12 == "4":
                        cmd = os.system("sudo apt-get install dradis")
                        tools12()
                    elif hackingop12 == "5":
                        cmd = os.system("sudo apt-get install keepnote")
                        tools12()
                    elif hackingop12 == "6":
                        cmd = os.system("sudo apt-get install magictree")
                        tools12()
                    elif hackingop12 == "7":
                        cmd = os.system("sudo apt-get install metagoofil")
                        tools12()
                    elif hackingop12 == "8":
                        cmd = os.system("sudo apt-get install nipper-ng")
                        tools12()
                    elif hackingop12 == "9":
                        cmd = os.system("sudo apt-get install pipal")
                        tools12()
                    elif hackingop12 == "0":
                        cmd = os.system("sudo apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools12()
            elif hacking == "13":
                def tools13():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tIngenieria Social\t\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

        1.- Backdoor Factory
        2.- Beef XSS
        3.- Ghost Phisher
        4.- Maltegoce
        5.- SET
        6.- u3-pwn

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m 
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m

                    '''
                    hackingop13 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop13 == "1":
                        cmd = os.system("sudo apt-get install backdoor-factory")
                        tools13()
                    elif hackingop13 == "back":
                        mistools()
                    elif hackingop13 == "2":
                        cmd = os.system("sudo apt-get install beef-xss")
                        tools13()
                    elif hackingop13 == "3":
                        cmd = os.system("sudo apt-get install ghost-phisher")
                        tools13()
                    elif hackingop13 == "4":
                        cmd = os.system("sudo apt-get install maltego-teeth")
                        tools13()
                    elif hackingop13 == "5":
                        cmd = os.system("sudo apt-get install set")
                        tools13()
                    elif hackingop13 == "6":
                        cmd = os.system("sudo apt-get install u3-pwn")
                        tools13()
                    elif hackingop13 == "0":
                        cmd = os.system("apt-get install -y backdoor-factory beef-xss ghost-phisher maltego-teeth set u3-pwn")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools13()
            elif hacking == "14":
                def tools14():
                    logo()
                    print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tProgramacion\t\t    #\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

        1.- Geany
        2.- Eclipse
        3.- Lazarus
        4.- Netbeans
        5.- QtCreator
        6.- GNUStep
        7.- Emacs
        8.- Kate
        9.- Kdevelop
        10.- Glade
        11.- Anjunta
        12.- Bluefish
        13.- CodeBlocks

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m 
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m

                    '''
                    hackingop14 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop14 == "1":
                        cmd = os.system("sudo apt-get install geany geany-plugins")
                        tools14()
                    elif hackingop14 == "back":
                        mistools()
                    elif hackingop14 == "2":
                        cmd = os.system("sudo apt-get install eclipse")
                        tools14()
                    elif hackingop14 == "3":
                        cmd = os.system("sudo apt-get install lazarus")
                        tools14()
                    elif hackingop14 == "4":
                        cmd = os.system("sudo apt-get install netbeans")
                        tools14()
                    elif hackingop14 == "5":
                        cmd = os.system("sudo apt-get install qtcreator")
                        tools14()
                    elif hackingop14 == "6":
                        cmd = os.system("sudo apt-get install gnustep")
                        tools14()
                    elif hackingop14 == "7":
                        cmd = os.system("sudo apt-get install emacs")
                        tools14()
                    elif hackingop14 == "8":
                        cmd = os.system("sudo apt-get install kate")
                        tools14()
                    elif hackingop14 == "9":
                        cmd = os.system("sudo apt-get install kdevelop")
                        tools14()
                    elif hackingop14 == "10":
                        cmd = os.system("sudo apt-get install glade")
                        tools14()
                    elif hackingop14 == "11":
                        cmd = os.system("sudo apt-get install anjuta")
                        tools14()
                    elif hackingop14 == "12":
                        cmd = os.system("sudo apt-get install bluefish")
                        tools14()
                    elif hackingop14 == "13":
                        cmd = os.system("sudo apt-get install codeblocks")
                        tools14()
                    elif hackingop14 == "0":
                        cmd = os.system("sudo apt-get -y install geany geany-plugins eclipse lazarus netbeans qtcreator gnustep emacs kate kdevelop glade anjuta bluefish codeblocks")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools() 
                tools14()
            elif hacking == "back":
                cuatro()
            elif hacking == "15":
                def tools15():
                    logo()
                    print '''
    \033[1;91m#########################################\033[1;m
    \033[1;91m# \tAnonimato \t\t\t    #\033[1;m
    \033[1;91m#########################################\033[1;m
    \033[1;36m

    1.-Hexchat
    2.-Privoxy
    3.-Polipo
    4.-Vidalia
    5.-Torchat
    6.-Proxychains
    7.-Anonsurf

    \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m 
    \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m

                    '''
                    hackingop15 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop15 == "1":
                        cmd = os.system("sudo apt-get install hexchat")
                        tools15()
                    elif hackingop15 == "back":
                        mistools()
                    elif hackingop15 == "2":
                        cmd = os.system("sudo apt-get install privoxy")
                        tools15()
                    elif hackingop15 == "3":
                        cmd = os.system("sudo apt-get install polipo")
                        tools15()
                    elif hackingop15 == "4":
                        cmd = os.system("sudo apt-get install vidalia")
                        tools15()
                    elif hackingop15 == "5":
                        cmd = os.system("sudo apt-get install torchat")
                        tools15()
                    elif hackingop15 == "6":
                        cmd = os.system("sudo apt-get install proxychains")
                        tools15()
                    elif hackingop15 == "7":
                        cmd = os.system("sudo git clone https://github.com/Und3rf10w/kali-anonsurf && cd kali-anonsurf/ && ./installer.sh && cd .. && rm -r kali-anonsurf")
                        tools15()
                    elif hackingop15 == "0":
                        cmd = os.system("sudo apt-get -y install hexchat privoxy polipo vidalia torchat proxychains")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools15()
            elif hacking == "16":
                def tools16():
                    print '''
    \033[1;91m#########################################\033[1;m
    \033[1;91m# \tCriptografía \t\t\t    #\033[1;m
    \033[1;91m#########################################\033[1;m
    \033[1;36m

    1.- TrueCrypt
    2.- Gnupg
    3.- EncFS

    \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m 
    \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m
                     '''
                    hackingop16 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop16 == "1":
                        cmd = os.system("sudo apt-get install truecrypt")
                        tools16()
                    elif hackingop16 == "back":
                        mistools()
                    elif hackingop16 == "2":
                        cmd = os.system("sudo apt-get install gnupg")
                        tools16()
                    elif hackingop16 == "3":
                        cmd = os.system("sudo apt-get install encfs")
                        tools16()
                    elif hackingop16 == "0":
                        cmd = os.system("sudo apt-get -y install truecrypt gnupg encfs")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools16()
            elif hacking == "17":
                def tools17():
                    print '''
    \033[1;91m#########################################\033[1;m
    \033[1;91m# \tAnalisis De Malware \t\t    #\033[1;m
    \033[1;91m#########################################\033[1;m
    \033[1;36m

    1.- Chkrootkit
    2.- Rkhunter
    3.- Lynis
    4.- Debsums
    5.- LMD

    \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m

    \033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m
    
    \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m

                    '''
                    hackingop17 = raw_input("\033[1;92m> \033[1;m")
                    if hackingop17 == "1":
                        cmd = os.system("sudo apt-get install chkrootkit")
                        tools17()
                    elif hackingop17 == "back":
                        mistools()
                    elif hackingop17 == "2":
                        cmd = os.system("sudo apt-get install rkhunter")
                        tools17()
                    elif hackingop17 == "3":
                        cmd = os.system("sudo apt-get install lynis")
                        tools17()
                    elif hackingop17 == "4":
                        cmd = os.system("sudo apt-get install debsums")
                        tools17()
                    elif hackingop17 == "5":
                        cmd = os.system("sudo git clone https://github.com/rfxn/linux-malware-detect && cd linux-malware-detect-master && ./install.sh && cd .. && rm -r linux-malware-detect-master")
                        tools17()
                    elif hackingop17 == "0":
                        cmd = os.system("sudo apt-get -y install chkrootkit rkhunter lynis debsums")
                        mistools()
                    else:
                        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Herramienta\033[1;m"
                        mistools()
                tools17()
            elif hacking == "18":
                exit()
            else:
                print "\033[1;91mPor Favor Teclee Unicamente El Numero Correspondiente A La Seccion\033[1;m"
                mistools()
        mistools()
    elif cuatroop == "2":
        def Acees():
            logo()
            print '''
    \033[1;91m#########################################\033[1;m
    \033[1;91m# \tAccesorios \t\t\t#\033[1;m
    \033[1;91m#########################################\033[1;m
    \033[1;36m
    1.- VirtualBox
    2.- Bleachbit
    3.- Google Chrome
    4.- Java
    5.- Pinta
    6.- RecordMyDesktop
    7.- Firefox
    8.- Flash
    9.- Kali Menu
    10.- Shutter
    11.- Gparted
    12.- Okular
    13.- Clementine

    \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m

            '''
            Accesorios = raw_input("\033[1;92m> \033[1;m")
            if Accesorios == "1":
                cmd = os.system("sudo apt-get install -y virtualbox-guest-x11 virtualbox virtualbox-ext-pack linux-headers* && usermod -a -G vboxusers ddos")
                Acees()
            elif Accesorios == "2":
                cmd = os.system("sudo apt-get -y install bleachbit")
                Acees()
            elif Accesorios == "3":
                print "\033[1;93m¿Para Que Arquitectura?: \033[1;m"
                print "\033[1;91m(POR FAVOR ESCRIBA 32 O 64 PARA INDICAR LA ARQUITECTURA)\033[1;m"
                arquitectura = raw_input("\033[1;92m> \033[1;m")
                if arquitectura == "32":
                    cmd = os.system("sudo wget https://archive.org/download/google-chrome-stable_48.0.2564.116-1_i386/google-chrome-stable_48.0.2564.116-1_i386.deb && dpkg -i google-chrome-stable_48.0.2564.116-1_i386.deb && rm google-chrome-stable_48.0.2564.116-1_i386.deb")
                    cmd1 = os.system("apt-get -f install")
                    print "\033[1;91mLa Instalacion Se Completo Con Exito, Para Ejecutar \nGoogle Chrome Por Favor Escriba El Comando\n\n /usr/bin/google-chrome-stable --no-sandbox --user-data-dir\033[1;m"
                    Acees()
                elif arquitectura == "64":
                    cmd = os.system("sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && dpkg -i google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb")
                    cmd1 = os.system("apt-get -f install")
                    print "\033[1;91mLa Instalacion Se Completo Con Exito, Para Ejecutar \nGoogle Chrome Por Favor Escriba El Comando\n\n /usr/bin/google-chrome-stable --no-sandbox --user-data-dir\033[1;m"
                    Acees()
                else:
                    print "\033[1;91mPor Favor Seleccione Una Opcion Valida\033[1;m"
                    Acees()
            elif Accesorios == "4":
                cmd = os.system('sudo echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list && echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list')
                cmd1 = os.system("sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886")
                cmd2 = os.system("sudo apt-get update")
                cmd3 = os.system("sudo apt-get -y install oracle-java8-installer")
                Acees()
            elif Accesorios == "5":
                cmd = os.system("sudo apt-get -y install pinta")
                Acees()
            elif Accesorios == "6":
                cmd = os.system("sudo apt-get -y install gtk-recordmydesktop")
                Acees()
            elif Accesorios == "7":
                cmd = os.system("sudo apt-get -y remove iceweasel")
                cmd1 = os.system("sudo echo -e deb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main | tee -a /etc/apt/sources.list > /dev/null")
                cmd2 = os.system("sudo apt-key adv –recv-keys –keyserver keyserver.ubuntu.com C1289A29")
                cmd3 = os.system("sudo apt-get update")
                cmd4 = os.system("sudo apt-get --force-yes install firefox-mozilla-build")
                Acees()
            elif Accesorios == "8":
                cmd = os.system("sudo apt-get -y install flashplugin-nonfree")
                cmd1 = os.system("sudo update-flashplugin-nonfree --install")
                Acees()
            elif Accesorios == "9":
                cmd = os.system("sudo apt-get install kali-menu")
                Acees()
            elif Accesorios == "10":
                cmd = os.system("sudo apt-get install shutter")
                Acees()
            elif Accesorios == "11":
                cmd = os.system("sudo apt-get install gparted")
                Acees()
            elif Accesorios == "12":
                cmd = os.system("sudo apt-get install okular")
                Acees()
            elif Accesorios == "13":
                cmd = os.system("sudo apt-get install clementine")
                Acees()
            elif Accesorios == "back":
                logo()
                cuatro()
            else:
                print "\033[1;91mPor Favor Seleccione Una Opcion Valida\033[1;m"
                Acees()
        Acees()
    elif cuatroop == "3":
        print "1.- Mostrar Estado De Todos Los Servicios"
        cmd = os.system("sudo service --status-all")
    elif cuatroop == "5":
        def aceesentorno():
            print '''
        \033[1;91m#############################################\033[1;m
        \033[1;91m#\tRemover Entorno Escritorio\t    #\033[1;m
        \033[1;91m#############################################\033[1;m
        \033[1;36m  
        
        1.- Mate
        2.- LXDE
        3.- XFCE
        4.- GNOME
        5.- Cinnamon
        6.- KDE
        
        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m
            '''
            reEntornos = raw_input("\033[1;92m> \033[1;m")
            if reEntornos == "1":
                cmd = os.system("apt-get remove mate-core mate-desktop-environment mate-notification-daemon && apt-get purge mate-core mate-desktop-environment mate-notification-daemon")
                aceesentorno()
            elif reEntornos == "2":
                cmd = os.system("apt-get remove lxde-core lxde && apt-get purge lxde-core lxde")
                aceesentorno()
            elif reEntornos == "3":
                cmd = os.system("apt-get remove xfce4 xfce4-places-plugin xfce4-goodies && apt-get purge xfce4 xfce4-places-plugin xfce4-goodies")
                aceesentorno()
            elif reEntornos == "4":
                cmd = os.system("apt-get remove gnome-core && apt-get purge gnome-core")
                aceesentorno()
            elif reEntornos == "5":
                cmd = os.system("apt-get remove cinnamon && apt-get purge cinnamon")
                aceesentorno()
            elif reEntornos == "6":
                cmd = os.system("apt-get remove kde-plasma-desktop && apt-get purge kde-plasma-desktop")
                aceesentorno()
            elif reEntornos == "back":
                cuatro()
            else:
                print "\033[1;91mPor Favor Seleccione Una Opcion Valida\033[1;m"
                aceesentorno()
        aceesentorno()    
    elif cuatroop == "4":
        def acces():
            logo()
            print '''
        \033[1;91m#########################################\033[1;m
        \033[1;91m# \tEntornos De Escritorio \t\t#\033[1;m
        \033[1;91m#########################################\033[1;m
        \033[1;36m

        1.- Mate
        2.- LXDE
        3.- XFCE
        4.- GNOME
        5.- Cinnamon
        6.- KDE

        \033[1;91mPuedes Presionar La Tecla '0' Para Instalar Todas Las Herramientas :D\033[1;m

        \033[1;91mO Puedes Escribir 'back' Sin Comillas Para Regresar Al Menu Anterior :D\033[1;m
                        '''
            Entornos = raw_input("\033[1;92m> \033[1;m")
            if Entornos == "1":
                cmd = os.system("sudo apt-get install mate-core mate-desktop-environment mate-notification-daemon")
                print  "\033[1;91mLa Instalacion Ha Finalizado, Por Favor Vuelva A Iniciar Sesion Y Escoga Mate Desktop Para Continuar\033[1;m"
                acces()
            elif Entornos == "back":
                logo()
                cuatro()
            elif Entornos == "2":
                cmd = os.system("sudo apt --fix-broken install && apt-get install lxde-core lxde desktop-base")
                acces()
            elif Entornos == "3":
                cmd = os.system("sudo apt-get install desktop-base xfce4 xfce4-places-plugin xfce4-goodies")
                acces()
            elif Entornos == "4":
                cmd = os.system("sudo apt-get install gnome-core desktop-base")
                acces()
            elif Entornos == "5":
                cmd = os.system("sudo apt-get install desktop-base cinnamon")
                acces()
            elif Entornos == "6":
                cmd = os.system("sudo apt-get install desktop-base kde-plasma-desktop")
                acces()
            elif Entornos == "0":
                cmd = os.system("sudo apt --fix-broken install && apt-get install lxde-core lxde desktop-base desktop-base xfce4 xfce4-places-plugin xfce4-goodies gnome-core desktop-base desktop-base cinnamon desktop-base kde-plasma-desktop")
                mistools()
            else:
                print "\033[1;91mPor Favor Seleccione Una Opcion Valida\033[1;m"
                acces()
        acces()         
    elif cuatroop == "6":
        cmd2 = os.system("sudo echo '# skriptedSEC\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
        cmd3 = os.system("sudo echo '# skriptedSEC\ndeb http://old.kali.org/kali sana main non-free contrib' >> /etc/apt/sources.list")
        cmd4 = os.system("sudo echo '# skriptedSEC\ndeb http://old.kali.org/kali moto main non-free contrib' >> /etc/apt/sources.list")
    elif cuatroop == "7":
        infile = "/etc/apt/sources.list"
        outfile = "/etc/apt/sources.list"
        repos = ["# skriptedSEC\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n", "# skriptedSEC\n", "deb http://old.kali.org/kali moto main non-free contrib\n", "# skriptedSEC\n", "deb http://old.kali.org/kali sana main non-free contrib\n"]
        c = open(infile)
        os.remove("/etc/apt/sources.list")
        xd = open(outfile, "w+")
        for borra in c:
            for i in repos:
                borra = borra.replace(i, "")
            xd.write(borra)
        c.close()
        xd.close()
    elif cuatroop == "back":
        todo()
    elif cuatroop == "8":
        exit()
    else:
        print "\033[1;91mPor Favor Teclee Unicamente El Numero De La Sección\033[1;m"
        logo()
        cuatro()
def cinco():
    exit()

def todo():
    try:
        create_launcher()
        inicio()
        opcion = raw_input("\033[1;92m> \033[1;m")

        if opcion == "1":
            uno()

        elif opcion == "2":
            dos()

        elif opcion == "3":
            tres()

        elif opcion == "4":
            cuatro()

        elif opcion == "5":
            cinco()
        else:
            print "\033[1;91mLa opción que escogiste no es valida\033[1;m"
            logo()
            todo()
    except KeyboardInterrupt:
        print("\n")
        print("\033[1;91m[!]Saliendo, God Bye ;)...\n\nGracias Por Usar sktools :)\033[1;m")
        sys.exit()
         
logo()       
todo()
