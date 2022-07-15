

class Hydra:

    head_hp = {"Ancient": 54,
               "Dreadful": 107,
               "Legendary": 221}

    element_map = {0: "Darkness",
                   1: "Light",
                   2: "Water",
                   3: "Wind",
                   4: "Earth",
                   5: "Fire"}

    type_map = {"Ancient": 3,
                "Dreadful": 4,
                "Legendary": 5}

    reward_ancient = {1: [0,70],
               2: [0,85],
               3: [0,110],
               4: [1,140],
               5: [1,170],
               6: [2,210]}

    reward_dreadful = {1: [0,150],
               2: [0,190],
               3: [1,240],
               4: [1,300],
               5: [2,370],
               6: [3,470]}

    reward_legendary = {1: [0,360],
               2: [1,450],
               3: [2,570],
               4: [3,710],
               5: [4,890],
               6: [6,1110]}

    rewards = {"Legendary": reward_legendary,
                "Dreadful": reward_dreadful,
                "Ancient": reward_ancient}

    CONST_DARKNESS = 0
    CONST_LIGHT = 1
    CONST_WATER = 2
    CONST_WIND = 3
    CONST_EARTH = 4
    CONST_FIRE = 5

    def __init__(self, type):
        self.type = type
        self.heads = {self.CONST_DARKNESS: self.head_hp[type],
                        self.CONST_LIGHT: self.head_hp[type],
                        self.CONST_WATER: self.head_hp[type],
                        self.CONST_WIND: self.head_hp[type],
                        self.CONST_EARTH: self.head_hp[type],
                        self.CONST_FIRE: self.head_hp[type]}
        self.assigned = {self.CONST_DARKNESS: [],
                        self.CONST_LIGHT: [],
                        self.CONST_WATER:[],
                        self.CONST_WIND: [],
                        self.CONST_EARTH: [],
                        self.CONST_FIRE: []}

    def is_dead(self):
        dead = True
        for head in self.heads:
            dead = self.heads[head] <= 0 and dead
        return dead

    def get_rewards(self):
        total = [0, 0]
        dead = 0
        for head in self.heads:
            if self.heads[head] <= 0:
                dead = dead + 1
                total[0] = total[0] + self.rewards[self.type][dead][0]
                total[1] = total[1] + self.rewards[self.type][dead][1]

        return total

    def __str__(self):
        string = "--- "+self.type+" Hydra ---\n"
        for head in self.heads:
            string = string + str(self.element_map[head])+ ": "+ str(self.assigned[head]) + "\n"
        return string

    def pretty_ptint(self):
        string = "--- " + self.type + " Hydra ---\n"
        for head in self.heads:
            string = string + str(self.element_map[head]) + ": "
            total_assigned = self.assigned[head]
            assigned_players = set(self.assigned[head])
            for player in assigned_players:
                times = len([x for x in total_assigned if x == player])
                string = string + str(times) + "x @"+str(player) + ", "
            string = string + "\n"
        return string


