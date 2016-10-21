# Author: Haider Ali Punjabi <haiderali@cyberservices.com>
# App: Database Generator for Evolve CP Calc.
# Description: Scrapes data from PokemonGO-Hub, and generates a .db database file

import src.databaseManager
import src.webManager

class DatabaseGenerator:

    def __init__(self):
        self.eeveeindex = 1

        database = src.databaseManager.DatabaseManager()
        webmanager = src.webManager.WebManager()
        print("Inserting Data into Database...")
        for id in webmanager.multDexID:
            self.Name = webmanager.getname(id)
            DexID = id
            self.MaxLimit = webmanager.getmaxcp(DexID)
            #if(DexID in webmanager.multDexID):          #Gets the following data for the Pokemon that can evolve
            self.Avg = webmanager.getmultavg(DexID)
            self.AmzCP = webmanager.getmultamzcp(DexID)
            self.GoodCP = webmanager.getmultgoodcp(DexID)
            self.EvoName = webmanager.getmultevoname(DexID)
            self.EvoDex = webmanager.getid(self.EvoName)
            self.EvoMaxLimit = webmanager.getmaxcp(self.EvoDex)
            Candy = webmanager.getcandy(DexID)
            Family = webmanager.getfamily(DexID)
            if(self.Name == "Eevee"):
                self.eevee(self.eeveeindex)
            #print(Name + "-" + DexID + "-" + Avg + "-" + MaxLimit + "-" + AmzCP + "-" + GoodCP + "-" + EvoName + "-" + EvoDex + "-" + EvoMaxLimit + "-" + Candy + "-" + Family)
            database.update_database(DexID,self.Name,self.Avg,self.MaxLimit,self.AmzCP,self.GoodCP,self.EvoName,self.EvoDex,self.EvoMaxLimit,Family,Candy)
        database.end()

    def eevee(self, index):
        if(index == 1):
            self.Name = "Eevee - Flareon"
            self.Avg = '2.56'
            self.MaxLimit = '1077'
            self.AmzCP = '801'
            self.GoodCP = '528'
            self.EvoName = "Flareon"
            self.EvoDex = "136"
            self.EvoMaxLimit = " 2643"
        elif(index == 2):
            self.Name = "Eevee - Jolteon"
            self.Avg = '2.14'
            self.MaxLimit = '1077'
            self.AmzCP = '803'
            self.GoodCP = '528'
            self.EvoName = "Jolteon"
            self.EvoDex = "135"
            self.EvoMaxLimit = " 2140"
        else:
            self.Name = "Eevee - Vaporeon"
            self.Avg = '2.77'
            self.MaxLimit = '1077'
            self.AmzCP = '808'
            self.GoodCP = '525'
            self.EvoName = "Vaporeon"
            self.EvoDex = "134"
            self.EvoMaxLimit = " 2816"
        self.eeveeindex += 1


