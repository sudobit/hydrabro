import csv

from player import Player
from hydra import Hydra
import random

CONST_PLAYERNAME = 0
CONST_ELEMENT = 1
CONST_ANCIENT = 2
CONST_DREADFUL = 3
CONST_LEGENDARY = 4


class Configuration:
    element_map = {"Darkness": 0,
                   "Light": 1,
                   "Water": 2,
                   "Wind": 3,
                   "Earth": 4,
                   "Fire": 5}

    def __init__(self, csv_file):
        self.Hydras = {2: Hydra("Legendary"),
                      1: Hydra("Dreadful"),
                      0: Hydra("Ancient")}

        self.guild = self.import_csv(csv_file)
        self.current_reward = [0, 0]

    def import_csv(self, filename):
        players = []
        with open(filename, newline='') as csvfile:
            hero_reader = csv.reader(csvfile, delimiter=';', quotechar="|")
            # Skips headlines
            next(hero_reader)
            for row in hero_reader:
                name = row[CONST_PLAYERNAME]
                if name == "" or name == "NA":
                    continue
                p = [p for p in players if p.name == name]
                if len(p) == 0:
                    p = Player(name)
                    players.append(p)
                else:
                    p = p[0]
                element = self.element_map[row[CONST_ELEMENT]]
                p.add_head("Ancient", element, row[CONST_ANCIENT])
                p.add_head("Dreadful", element, row[CONST_DREADFUL])
                p.add_head("Legendary", element, row[CONST_LEGENDARY])
        return players

    def close_gap(self, hydra, players):
        type = hydra.type
        rng_heads = list(range(0, 6))
        #rng_heads = [4] + [x for x in rng_heads if x != 4]
        random.shuffle(rng_heads)
        for head in rng_heads:
            gap = hydra.heads[head]
            while gap > 0:
                # Create a list of players who deal more than 0 damage and have attacks left
                player_element = [x for x in players if x.heads[type][head] != 0 and x.attacks > 0]
                # Sort players ny damage
                player_element = sorted(player_element, key=lambda x: int(x.heads[type][head]), reverse=True)
                # If no players left, end the loop
                if len(player_element) == 0:
                    break
                chosen = None
                # Find the player who just kills the hydra
                for x in player_element:
                    if gap < int(x.heads[type][head]):
                        chosen = x
                    else:
                        break
                if not chosen:
                    # If no player can kill the hydra, choose a random one
                    chosen = player_element[random.randint(0, len(player_element) - 1)]

                # Assign the player to the head
                damage = chosen.heads[type][head]
                hydra.heads[head] = hydra.heads[head] - int(damage)
                hydra.assigned[head].append(chosen.name)
                chosen.attacks = chosen.attacks - 1
                chosen.assign(type, head)
                gap = hydra.heads[head]
        return hydra

    def clean_unkilled(self, hydra, players):
        type = hydra.type
        # Go through Hydra heads
        #print("Remaing heads")
        for head in hydra.heads:
            # If HP are above 0, remove all assigned player from it.
            if hydra.heads[head] > 0:
                #print("Remain HP "+ str(hydra.heads[head])+ " on Hydra "+ str(head))
                for assigned_player in hydra.assigned[head]:
                    unassign_player = [x for x in players if x.name == assigned_player][0]
                    unassign_player.attacks = unassign_player.attacks + 1
                    unassign_player.unassign(type, head)
                hydra.assigned[head] = []
            else:
                continue

    def add_rewards(self, rewards):
        self.current_reward[0] = self.current_reward[0]+rewards[0]
        self.current_reward[1] = self.current_reward[1]+rewards[1]

    def print_players(self):
        return [[player.name, player.assigned] for player in self.guild]

    def create_assignment(self, current_head):
        assign = self.Hydras[current_head]
        current_rewards = assign.get_rewards()
        failures = 14
        while not assign.is_dead():
            assign = self.close_gap(assign, self.guild)
            new_rewards = assign.get_rewards()
            # Compare if rewards are the same, if so no improvement was made.
            # Break after 5 times no improvement was made.
            if current_rewards == new_rewards:
                failures = failures - 1
                if failures <= 0:
                    break
            else:
                current_rewards = new_rewards
                failures = 5

        if failures == 0:
            self.clean_unkilled(assign, self.guild)

        self.add_rewards(current_rewards)
        return assign

    def get_attacks(self):
        attacks = sum([x.attacks for x in self.guild])
        return attacks

    def create_proposal(self):
        proposal = []
        current_head = random.randint(0, 2)
        proposal.append(self.create_assignment(current_head))
        proposal.append(self.create_assignment((current_head + 1) % 3))
        proposal.append(self.create_assignment((current_head + 2) % 3))
        proposal.append(self.current_reward)
        proposal.append(self.get_attacks())
        proposal.append(self.print_players())
        return proposal

    def create_single_head(self, type):
        proposal = []
        proposal.append(self.create_assignment(type))
        proposal.append(None)
        proposal.append(None)
        proposal.append(self.current_reward)
        proposal.append(self.get_attacks())
        proposal.append(self.print_players())
        return proposal
