#Web Manager
from lxml import html
import requests

#Required URLs
urlMultiplier = "http://pokemongohub.net/pokemon-go-evolution-multiplier-chart/"        #Contains Multiplier data
urlData = "http://pokemongohub.net/pokemon-go-max-cp-per-level-chart/"                  #Contains DexID and Pokemon Names
urlFamily = "http://www.serebii.net/pokemongo/pokemon.shtml"                            #Contains Candy Requirements
#Required XPaths
xpathDataName = "/html/body/div[6]/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[%d]/td[2]/strong/text()"
xpathDataDexID = "/html/body/div[6]/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[%d]/td[1]/span/text()"
xpathDataMaxCP = "/html/body/div[6]/div[2]/div/div[2]/div/div/div/div/table/tbody/tr[%d]/td[3]/text()"
xpathMultDexID = "/html/body/div[6]/article/div[2]/div/div/div/div[2]/table/tbody/tr[%d]/td[1]/span/text()"
xpathMultAvg = "/html/body/div[6]/article/div[2]/div/div/div/div[2]/table/tbody/tr[%d]/td[3]/strong/text()"
xpathMultAmzCP = "/html/body/div[6]/article/div[2]/div/div/div/div[2]/table/tbody/tr[%d]/td[5]/text()"
xpathMultGoodCP = "/html/body/div[6]/article/div[2]/div/div/div/div[2]/table/tbody/tr[%d]/td[6]/strong/text()"
xpathMultEvoName = "/html/body/div[6]/article/div[2]/div/div/div/div[2]/table/tbody/tr[%d]/td[7]/span/text()"

class WebManager:


    def __init__(self):
        self.pageData = requests.get(urlData)
        self.pageMult = requests.get(urlMultiplier)
        self.treeData = html.fromstring(self.pageData.content)
        self.treeMult = html.fromstring(self.pageMult.content)
        self.storenames()
        self.storedexid()
        self.storemaxcp()
        self.storemultamzcp()
        self.storemultavg()
        self.storemultdexid()
        self.storemultevoname()
        self.storemultgoodcp()


    def storenames(self):           #Stores All Pokemon Names
        self.pokemonNames = []
        i = 3
        while i <= 153:
            if((self.treeData.xpath(xpathDataName %(i))[0]).replace(" ", "") == "Nidoran♀"):
                self.pokemonNames.append("Nidoran F")
            elif((self.treeData.xpath(xpathDataName %(i))[0]).replace(" ", "") == "Nidoran♂"):
                self.pokemonNames.append("Nidoran M")
            else:
                self.pokemonNames.append((self.treeData.xpath(xpathDataName %(i))[0]).replace(" ", ""))
            i += 1


    def storedexid(self):           #Stores all Pokemon Dex IDs
        self.pokemonDexID = []
        i = 3
        while i <= 153:
            self.pokemonDexID.append((self.treeData.xpath(xpathDataDexID %(i))[0]).replace(" ", ""))
            i += 1


    def storemaxcp(self):           #Stores MaxCP data for all pokemon
        self.pokemonMaxCP = []
        i = 3
        while i <= 153:
            self.pokemonMaxCP.append((self.treeData.xpath(xpathDataMaxCP %(i))[0]).replace(" ", ""))
            i += 1

    def storemultdexid(self):       #Stores DexID for Pokemon that can evolve
        self.multDexID = []
        i = 2
        while i <= 73:
            self.multDexID.append(((self.treeMult.xpath(xpathMultDexID %(i)))[0]).replace(" ", ""))
            i += 1

    def storemultavg(self):         #Stores Multiplying Factor
        self.multAvg = []
        i = 2
        while i <= 73:
            self.multAvg.append(((self.treeMult.xpath(xpathMultAvg %(i)))[0]).replace(" ", ""))
            i += 1


    def storemultamzcp(self):       #Stores Amazing CP Data
        self.multAmzCP = []
        i = 2
        while i <= 73:
            self.multAmzCP.append(((self.treeMult.xpath(xpathMultAmzCP %(i)))[0]).replace(" ", ""))
            i += 1


    def storemultgoodcp(self):      #Stores Good CP Data
        self.multGoodCP = []
        i = 2
        while i <= 73:
            self.multGoodCP.append(((self.treeMult.xpath(xpathMultGoodCP %(i)))[0]).replace(" ", ""))
            i += 1


    def storemultevoname(self):     #Stores Names of Evolutions
        self.multEvoName = []
        i = 2
        while i <= 73:
            if(self.treeMult.xpath(xpathMultEvoName %(i))[0] == "Globat"):                  #Required due to typing error on the database source
                self.multEvoName.append("Golbat")
            elif (self.treeMult.xpath(xpathMultEvoName % (i))[0].replace(" ", "") == "Victreebell"):    #Required due to typing error on the database source
                self.multEvoName.append("Victreebel")
            else:
                self.multEvoName.append(((self.treeMult.xpath(xpathMultEvoName %(i)))[0]).replace(" ", ""))
            i += 1

    def getname(self, dexid):         #Returns the Pokemon Name for a DexID
        index = self.pokemonDexID.index(dexid)
        return self.pokemonNames[index]


    def getid(self, name):          #Returns the DexID for a Pokemon Name
        index = self.pokemonNames.index(name)
        return self.pokemonDexID[index]

    def getmaxcp(self, dexid):      #Returns the MaxCP for a DexID
        index = self.pokemonDexID.index(dexid)
        return self.pokemonMaxCP[index]

    def getmultavg(self, dexid):     #Returns Multiplying factor for a DexID
        index = self.multDexID.index(dexid)
        return  self.multAvg[index]

    def getmultgoodcp(self, dexid):     #Returns Good CP for a DexID
        index = self.multDexID.index(dexid)
        return self.multGoodCP[index]

    def getmultamzcp(self, dexid):      #Returns Amazing CP for a DexID
        index = self.multDexID.index(dexid)
        return self.multAmzCP[index]

    def getmultevoname(self, dexid):    #Returns Evolution Name for a DexID
        index = self.multDexID.index(dexid)
        return self.multEvoName[index]