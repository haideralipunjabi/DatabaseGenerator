# Author: Haider Ali Punjabi <haiderali@cyberservices.com>
# App: Database Generator for Evolve CP Calc.
# Description: Scrapes data from PokemonGO-Hub, and generates a .db database file

import src.databaseManager
import src.webManager

class DatabaseGenerator:

    database = src.databaseManager.DatabaseManager()
    webmanager = src.webManager.WebManager()

    for name in webmanager.pokemonNames:
        Name = name
        DexID = webmanager.getid(name)
        MaxLimit = webmanager.getmaxcp(DexID)
        if(DexID in webmanager.multDexID):          #Gets the following data for the Pokemon that can evolve
            Avg = webmanager.getmultavg(DexID)
            AmzCP = webmanager.getmultamzcp(DexID)
            GoodCP = webmanager.getmultgoodcp(DexID)
            EvoName = webmanager.getmultevoname(DexID)
            EvoDex = webmanager.getid(EvoName)
            EvoMaxLimit = webmanager.getmaxcp(EvoDex)
            print(Name + "-" + DexID + "-" + Avg + "-" + MaxLimit + "-" + AmzCP + "-" + GoodCP + "-" + EvoName + "-" + EvoDex + "-" + EvoMaxLimit)

