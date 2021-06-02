
from mojang import MojangAPI
from colorama import Fore
import requests








def mojang_user(name):
    
    uuid = MojangAPI.get_uuid(name)
    
    if not uuid:
        print(Fore.YELLOW +"Pas de compte a ce nom ")
        print("")
    else:
        profile = MojangAPI.get_profile(uuid)
        legacy = MojangAPI.get_name_history(uuid)


        name_history = requests.get(f"https://api.mojang.com/user/profiles/{uuid}/names").json()
        history = ""
        name_data = list()
        for data in name_history:
            name_data.append(data["name"])

        print(Fore.CYAN + "UUID = " + Fore.RESET + uuid )
        print("")
        print(Fore.CYAN + "NAME = " + Fore.RESET + name )
        print("")
        print(Fore.CYAN + "SKIN = " + Fore.RESET + profile.skin_url)
        print("")

    
        for i in range(len(name_data)):
            history += name_data[i] + " | "
        
        print(Fore.CYAN + "NAME_CHANGE = " + Fore.RESET + history)
        print("")
