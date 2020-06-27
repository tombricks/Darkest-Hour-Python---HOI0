class cultures:
    european = "european"

class ideologies:
    fascism = "fascism"
    communism = "communism"
    democratic = "democratic"
    neutrality = "neutrality"
    def name(ideology):
        return localisation["ideology_"+ideology+"_name"]

class subideologies:
    imperialism = "imperialism"
    socialist_fascism = "socialist_fascism"
    marxism_leninism = "marxism_leninism"
    conservatism = "conservatism"
    def name(subideology):
        return localisation["subideology_"+subideology+"_name"]

from systemCommands import *
class leader:
    def __init__(self, tag, ideology, portrait=""):
        self.tag = tag
        self.name = localisation["leader_"+tag+"_name"]
        self.title = localisation["leader_"+tag+"_title"]
        self.party = localisation["leader_"+tag+"_party"]
        self.ideology = ideology
        if portrait == "":
            self.portrait = str("gfx/leaders/"+tag+".png")
        else:
            self.portrait = portrait
            

class nation:
    def __init__(self, tag, ideology, culture, commPop, fascPop, demoPop, neutPop, colour, commLeader, fascLeader, demoLeader, neutLeader):
        self.tag = tag
        self.ideology = ideology
        self.culture = culture
        self.commName = localisation["nation_"+tag+"_commName"]
        self.fascName = localisation["nation_"+tag+"_fascName"]
        self.demoName = localisation["nation_"+tag+"_demoName"]
        self.neutName = localisation["nation_"+tag+"_neutName"]
        self.fallName = localisation["nation_"+tag+"_fallName"]
        self.adjective = localisation["nation_"+tag+"_adjective"]
        self.commPop = commPop
        self.fascPop = fascPop
        self.demoPop = demoPop
        self.neutPop = neutPop
        self.popularities = [commPop, fascPop, demoPop, neutPop]
        self.colour = colour
        self.commLeader = commLeader
        self.fascLeader = fascLeader
        self.demoLeader = demoLeader
        self.neutLeader = neutLeader
        self.monarchy = ""
        if self.ideology == ideologies.communism:
            self.name = self.commName
            self.leader = self.commLeader
            if not doesFileExist(str("gfx/flags/" + self.tag + "_communism.tga")):
                self.flag = str("gfx/flags/" + self.tag + "_communism.tga")
            else:
                self.flag = str("gfx/flags/" + self.tag + ".tga")
        elif self.ideology == ideologies.fascism:
            self.name = self.fascName
            self.leader = self.fascLeader
            if doesFileExist(str("gfx/flags/" + self.tag + "_fascism.tga")):
                self.flag = str("gfx/flags/" + self.tag + "_fascism.tga")
            else:
                self.flag = str("gfx/flags/" + self.tag + ".tga")
        elif self.ideology == ideologies.democratic:
            self.name = self.demoName
            self.leader = self.demoLeader
            if doesFileExist(str("gfx/flags/" + self.tag + "_democratic.tga")):
                self.flag = str("gfx/flags/" + self.tag + "_democratic.tga")
            else:
                self.flag = str("gfx/flags/" + self.tag + ".tga")
        elif self.ideology == ideologies.neutrality:
            self.name = self.neutName
            self.leader = self.neutLeader
            if doesFileExist(str("gfx/flags/" + self.tag + "_neutrality.tga")):
                self.flag = str("gfx/flags/" + self.tag + "_neutrality.tga")
            else:
                self.flag = str("gfx/flags/" + self.tag + ".tga")
        else:
            self.name = self.fallName
        
    
    def isCountryLeader(self, name):
        if self.leader.name == name or self.leader.tag == name:
            return True
        else:
            return False
    
    def updateNames(self):
        if self.ideology == ideologies.communism:
            self.name = self.commName
            self.leader = self.commLeader
            if doesFileExist(str("gfx/flags/" + self.tag + "_communism.tga")):
                self.flag = str("gfx/flags/" + self.tag + "_communism.tga")
            else:
                self.flag = str("gfx/flags/" + self.tag + ".tga")
        elif self.ideology == ideologies.fascism:
            self.name = self.fascName
            self.leader = self.fascLeader
            if doesFileExist(str("gfx/flags/" + self.tag + "_fascism.tga")):
                self.flag = str("gfx/flags/" + self.tag + "_fascism.tga")
            else:
                self.flag = str("gfx/flags/" + self.tag + ".tga")
        elif self.ideology == ideologies.democratic:
            self.name = self.demoName
            self.leader = self.demoLeader
            if doesFileExist(str("gfx/flags/" + self.tag + "_democratic.tga")):
                self.flag = str("gfx/flags/" + self.tag + "_democratic.tga")
            else:
                self.flag = str("gfx/flags/" + self.tag + ".tga")
        elif self.ideology == ideologies.neutrality:
            self.name = self.neutName
            self.leader = self.neutLeader
            if doesFileExist(str("gfx/flags/" + self.tag + "_neutrality.tga")):
                self.flag = str("gfx/flags/" + self.tag + "_neutrality.tga")
            else:
                self.flag = str("gfx/flags/" + self.tag + ".tga")
        else:
            self.name = self.fallName
        
    def debug(self):
        print(self.tag)
        print(self.ideology)
        print(self.culture)
        print(self.commName)
        print(self.fascName)
        print(self.demoName)
        print(self.neutName)
        print(self.fallName)
        self.updateNames()
        print(self.name)
        print(self.adjective)
        print(self.commPop)
        print(self.fascPop)
        print(self.demoPop)
        print(self.neutPop)
        print(self.popularities)
        print(self.flag)
        print(self.colour)

    def currentPopularity(self):
         if self.ideology == ideologies.communism:
             return self.commPop
         elif self.ideology == ideologies.fascism:
             return self.fascPop
         elif self.ideology == ideologies.democratic:
             return self.demoPop
         elif self.ideology == ideologies.neutrality:
             return self.neutPop
