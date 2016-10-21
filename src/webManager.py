#Web Manager
from lxml import html
import requests
import sys
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
xpathFamily = "/html/body/table[2]/tr[2]/td[2]/font/table[2]/tr[%d]/td[6]/text()"
xpathFamilyName = "/html/body/table[2]/tr[2]/td[2]/font/table[2]/tr[%d]/td[3]/a/text()"
class WebManager:


    def __init__(self):
        self.loadstuff()


    def storenames(self):           #Stores All Pokemon Names
        self.pokemonNames = []
        i = 1
        while i <= 151:
            if((self.treeData.xpath(xpathDataName %(i))[0]).replace(" ", "") == "Nidoran♀"):
                self.pokemonNames.append("Nidoran F")
            elif((self.treeData.xpath(xpathDataName %(i))[0]).replace(" ", "") == "Nidoran♂"):
                self.pokemonNames.append("Nidoran M")
            else:
                self.pokemonNames.append((self.treeData.xpath(xpathDataName %(i))[0]).replace(" ", ""))
            i += 1


    def storedexid(self):           #Stores all Pokemon Dex IDs
        self.pokemonDexID = []
        i = 1
        while i <= 151:
            self.pokemonDexID.append((self.treeData.xpath(xpathDataDexID %(i))[0]).replace(" ", ""))
            i += 1


    def storemaxcp(self):           #Stores MaxCP data for all pokemon
        self.pokemonMaxCP = []
        i = 1
        while i <= 151:
            self.pokemonMaxCP.append((self.treeData.xpath(xpathDataMaxCP %(i))[0]).replace(" ", ""))
            i += 1

    def storemultdexid(self):       #Stores DexID for Pokemon that can evolve
        self.multDexID = []
        i = 1
        while i <= 72:
            self.multDexID.append(((self.treeMult.xpath(xpathMultDexID %(i)))[0]).replace(" ", ""))
            i += 1

    def storemultavg(self):         #Stores Multiplying Factor
        self.multAvg = []
        i = 1
        while i <= 72:
            self.multAvg.append(((self.treeMult.xpath(xpathMultAvg %(i)))[0]).replace(" ", ""))
            i += 1


    def storemultamzcp(self):       #Stores Amazing CP Data
        self.multAmzCP = []
        i = 1
        while i <= 72:
            self.multAmzCP.append(((self.treeMult.xpath(xpathMultAmzCP %(i)))[0]).replace(" ", ""))
            i += 1


    def storemultgoodcp(self):      #Stores Good CP Data
        self.multGoodCP = []
        i = 1
        while i <= 72:
            self.multGoodCP.append(((self.treeMult.xpath(xpathMultGoodCP %(i)))[0]).replace(" ", ""))
            i += 1


    def storemultevoname(self):     #Stores Names of Evolutions
        self.multEvoName = []
        i = 1
        while i <= 72:
            if(self.treeMult.xpath(xpathMultEvoName %(i))[0] == "Globat"):                  #Required due to typing error on the database source
                self.multEvoName.append("Golbat")
            elif (self.treeMult.xpath(xpathMultEvoName % (i))[0].replace(" ", "") == "Victreebell"):    #Required due to typing error on the database source
                self.multEvoName.append("Victreebel")
            else:
                self.multEvoName.append(((self.treeMult.xpath(xpathMultEvoName %(i)))[0]).replace(" ", ""))
            i += 1

    def storefamily(self):
        self.candies = []
        self.family = []
        i = 2
        while i <= 152:
            requirement = self.treeFamily.xpath(xpathFamily %(i))[0].strip()
            pokename = self.treeFamily.xpath(xpathFamilyName %(i))[0].strip()
            if(pokename != 'Jolteon' and pokename != 'Vaporeon'):
                if(requirement != "None"):
                 split = requirement.split(" ")[0].split(" ")
                 self.candies.append(split[0])
                 if (split[1] == "Nidoran♀"):
                     self.family.append("Nidoran F")
                 elif (split[1] == "Nidoran♂"):
                     self.family.append("Nidoran M")
                 else:
                     self.family.append(split[1])
            else:
                self.candies.append('25')
                self.family.append('Eevee')
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

    def getcandy(self, dexid):         #Returns the Candy Requirement for a DexID
        index = self.multDexID.index(dexid)
        return self.candies[index]

    def getfamily(self, dexid):         #Returns the Pokemon Name for a DexID
        index = self.multDexID.index(dexid)
        return self.family[index]


    def loadstuff(self):
        print("Fetching Data...")
        self.pageData = requests.get(urlData)
        self.pageMult = requests.get(urlMultiplier)
        self.pageFamily = requests.get(urlFamily)
        self.treeData = html.fromstring(self.pageData.content)
        self.treeMult = html.fromstring(self.pageMult.content)
        self.treeFamily = html.fromstring(self.pageFamily.content)
        print("Storing Data...")
        self.storenames()
        self.storedexid()
        self.storemaxcp()
        self.storemultamzcp()
        self.storemultavg()
        self.storemultdexid()
        self.storemultevoname()
        self.storemultgoodcp()
        self.storefamily()

class Connection:

    def isserveravailable(self):
        try:
            print("Establishing connection to server...")
            requests.get(urlData)
            print("Connection Established!")
            return True
        except requests.ConnectionError as err: pass
        print("Connection Failed")
        return False