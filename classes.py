import utils

class donjonInstance:
    
    def __init__(self, counter=0, key='', owner='', time=''):

        self.count = counter
        self.key = key
        self.owner = owner
        self.time = time

        self.tanks = []
        self.heals = []
        self.dps = []        
    
    def add_player(self, role, pseudo, classe, ilvl):
        if pseudo in (utils.dictListToList(self.tanks) + utils.dictListToList(self.heals) + utils.dictListToList(self.dps)):
            return 2
        if role == "tank":
            self.tanks.append({'pseudo' : pseudo, 'class' : classe, 'ilvl' : ilvl })
            return 0
        elif role == "heal":
            self.heals.append({'pseudo' : pseudo, 'class' : classe, 'ilvl' : ilvl })
            return 0
        elif role == "dps":
            self.dps.append({'pseudo' : pseudo, 'class' : classe, 'ilvl' : ilvl })
            return 0

    def remove_player(self, pseudo):
        for i in self.tanks:
            if i['pseudo'] == pseudo:
                self.tanks.remove(i)
        for i in self.heals:
            if i['pseudo'] == pseudo:
                self.heals.remove(i)
        for i in self.dps:
            if i['pseudo'] == pseudo:
                self.dps.remove(i)

    
    def print_full(self):
        tanks = utils.userDictToString(self.tanks)
        heals = utils.userDictToString(self.heals)
        dps = utils.userDictToString(self.dps)

        waitingTanks = utils.userStringToString(tanks[1:])
        waitingHeals = utils.userStringToString(heals[1:])
        waitingDps = utils.userStringToString(dps[3:])

        full =  '''__**Informations**__ 
**ID du Donjon :** {}
**Clé :** {}
**Propriétaire :** {}
**Heure :** {}

__**Composition**__
**Tank :** {}
**Heal :** {}
**DPS :** {}
**DPS :** {}
**DPS :** {}

__**Files d'attente**__
Tank : {}
Heal : {}
DPS : {}
'''.format(self.count, self.key, self.owner, self.time, tanks[0], heals[0], dps[0], dps[1] , dps[2], waitingTanks, waitingHeals, waitingDps)

        full = full.replace('\t', '')
        return full     

     