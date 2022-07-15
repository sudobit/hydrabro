

class Player:
    CONST_DARKNESS = 0
    CONST_LIGHT = 1
    CONST_WATER = 2
    CONST_WIND = 3
    CONST_EARTH = 4
    CONST_FIRE = 5

    element_map = {0: "Darkness",
                   1: "Light",
                   2: "Water",
                   3: "Wind",
                   4: "Earth",
                   5: "Fire"}

    type_map = {"Ancient": 3,
                "Dreadful": 4,
                "Legendary": 5}

    def __init__(self, name):
        self.name = name
        self.ancient = {self.CONST_DARKNESS: 0,
                        self.CONST_LIGHT: 0,
                        self.CONST_WATER: 0,
                        self.CONST_WIND: 0,
                        self.CONST_EARTH: 0,
                        self.CONST_FIRE: 0}
        self.dreadful = {self.CONST_DARKNESS: 0,
                        self.CONST_LIGHT: 0,
                        self.CONST_WATER: 0,
                        self.CONST_WIND: 0,
                        self.CONST_EARTH: 0,
                        self.CONST_FIRE: 0}
        self.legendary = {self.CONST_DARKNESS: 0,
                        self.CONST_LIGHT: 0,
                        self.CONST_WATER: 0,
                        self.CONST_WIND: 0,
                        self.CONST_EARTH: 0,
                        self.CONST_FIRE: 0}

        self.heads = {"Legendary": self.legendary,
                      "Dreadful": self.dreadful,
                      "Ancient": self.ancient}
        self.attacks = 3
        self.assigned = []

    def add_head(self, head, element, damage):
        if damage:
            self.heads[head][element] = damage

    def __str__(self):
        print("-----"+str(self.name)+"-----")
        for head in self.heads:
            print("---"+str(head)+"---")
            for element in self.heads[head]:
                print(self.element_map[element]+":"+str(self.heads[head][element]))

    def assign(self, type, head):
        self.assigned.append(type + "(" + str(self.type_map[type]) + ") " + self.element_map[head])

    def unassign(self, type, head):
        self.assigned.remove(type + "(" + str(self.type_map[type]) + ") " + self.element_map[head])

