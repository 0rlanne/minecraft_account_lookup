##################################################################################
#MIT License                                                                     #
#                                                                                #
#Copyright (c) 2021 H0xtry                                                       #
#                                                                                #
#Permission is hereby granted, free of charge, to any person obtaining a copy    #
#of this software and associated documentation files (the "Software"), to deal   #
#in the Software without restriction, including without limitation the rights    #
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       #
#copies of the Software, and to permit persons to whom the Software is           #
#furnished to do so, subject to the following conditions:                        #
#                                                                                #
#The above copyright notice and this permission notice shall be included in all  #
#copies or substantial portions of the Software.                                 #
#                                                                                #
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      #
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        #
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     #
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          #
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   #
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   #
#SOFTWARE.                                                                       #
##################################################################################





from Core.Minecraft import mojang_user
from Core.namemc import namepy
from colorama import Fore, init
import socket
import requests
import sys
from requests import get
from time import gmtime, strftime
import time
from mojang import MojangAPI
ts = time.time()
init(autoreset = True)
date = strftime('%Y/%m/%d %H:%M:%S', gmtime())   #donne la date et l'heure ou le programme se lance 
api = "http://ip-api.com/json/"

host = socket.gethostname()     #donne le nom de l'ordinateur (desktop...)
ip_host = get('https://api.ipify.org').text  #ip de l'ordinateur (ipv4 soit ip public)
data = requests.get(api+ip_host).json()
sys.stdout.flush()
pays = data['country']   #donne le pays de l'ip 

serveur = ["pvp.land", "mc.hypixel.net", "prisonfun.co", "cavepvp.org", "onlypvp.pl", "mcplayhd.net", "akumamc.net", "lunar.gg", "eu.lunar.gg", "sagepvp.org", "ghostly.live", "dynamicpvp.net", "greev.eu", "play.vipermc.net", "vipermc.net", "minemen.club", "eu.minemen.club", "introuble.de", "potion.land", "play.schoolrp.net", "play.wildprison.net", "play.ecc.eco", "fiercepvp.net", "astralmc.cc", "skywars.world", "antiac.net", "heromines.com", "bedwarspractice.club", "holypvp.net", "spieleoase.net"]




banniere = Fore.CYAN + """                  
                        !         !          
                       ! !       ! !          
                      ! . !     ! . !          
                         ^^^^^^^^^ ^            
                      ^             ^          
                    ^  (0)       (0)  ^       
                   ^        ""         ^                    __________  ____  ____  ____ 
                  ^   ***************    ^                 / ____/ __ \/ __ \/ __ \/ __ \ 
                ^   *                 *   ^               / / __/ /_/ / /_/ / /_/ / /_/ /
               ^   *   /\   /\   /\    *    ^            / /_/ / _, _/ _, _/ _, _/ _, _/ 
              ^   *                     *    ^           \____/_/ |_/_/ |_/_/ |_/_/ |_|  
             ^   *   /\   /\   /\   /\   *    ^
            ^   *                         *    ^
            ^  *                           *   ^             """ + date + """
            ^  *                           *   ^             """ + host + """
             ^ *                           *  ^              """ + ip_host + """
              ^*                           * ^               [""" + pays + """]
               ^ *                        * ^
               ^  *                      *  ^
                ^  *       ) (         * ^
                    ^^^^^^^^ ^^^^^^^^^ 

"""



Menu = Fore.MAGENTA + """★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★
|                                                  |
|    [1] Minecraft              [2] Namemc         |
|                                                  |
|    [3] Amis namemc            [4] Help           |
|                                                  |
|                   [5] Quitter                    |
★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★

"""


help = Fore.YELLOW + """A quoi sert ce programe ? 
ce programe a ete concu pour permetre a une personne de voir les uuid, pseudos, serveur les plus aimer et amis d'une personne 
l'utilisation dúne API (Namemc) permet de faire ces recherches 
choisissez ce que vous preferez (choix [1], [2], [3] ...)
entrez les informations demandées 
recevez les infos (serveur, amis ...)
enjoy ! 

"""


print(banniere)

retour = 1
while retour == 1: 
  retour = 0

  print(Menu)

  Choix = int(input("Choix : "))

  if Choix < 1 or Choix >5 :
    print(Fore.RED + "Choix invalid, choix possibles : [1], [2], [3], [4], [5]")
    print("")
    retour = 1
  
  elif Choix == 1:
    print("")
    name = input('username : ')
    print("")
    mojang_user(name)
    print("")

    retour = 1

  elif Choix == 2: 
    print("")
    name = input('username : ')
    print("")
    print(name)
    print("")
    uuid = MojangAPI.get_uuid(name)
    print(uuid)
    print("")
    print("serveur like : ")
    print("")
    for i in range(len(serveur)):
      serverlike = namepy().verifyLike(server=serveur[i], username=name)
      if serverlike == True : 
        print(serveur[i])
      else : 
        pass

    retour = 1


  elif Choix == 3: 
    #quand vous metez les pseudo verifiez que les majuscules, caracteres speciaux ou minuscules soit bien mise 
    #sinon le programme ne fonctionnera pas 
    print("")
    name = str(input(Fore.LIGHTBLUE_EX + 'username : '))
    print("")
    nametow = str(input(Fore.LIGHTBLUE_EX + 'username de la personne : '))
    print("")
    uuid = MojangAPI.get_uuid(name)
    frienduuid = MojangAPI.get_uuid(nametow)
    test = namepy().areFriends(username1= name , username2=nametow)
    print(Fore.GREEN + "Est ami :", test)
    
    input("")
    retour = 1

  elif Choix == 4:
    print(help)
    print("")
    input()
    retour = 1

  else : 
    input()
