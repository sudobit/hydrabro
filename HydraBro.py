import argparse
from datetime import time, datetime
from configuration import Configuration

parser = argparse.ArgumentParser(description='Run HydraBro to optimize your hydra gains.')
parser.add_argument('--players', action='store', dest='csv_file', help="Path to csv file which holds player numbers")
parser.add_argument('--amount', action='store', dest='amount', type=int, default=50000, help="Amount of configurations"
                                                                                             " to create, default to "
                                                                                             "50.000")

print("""
 _   _           _          ______           
| | | |         | |         | ___ \          
| |_| |_   _  __| |_ __ __ _| |_/ /_ __ ___  
|  _  | | | |/ _` | '__/ _` | ___ \ '__/ _ \ 
| | | | |_| | (_| | | | (_| | |_/ / | | (_) |
\_| |_/\__, |\__,_|_|  \__,_\____/|_|  \___/ 
        __/ |                                
       |___/                             """)
print("Hero Wars Hydra Optimizer")


def pretty_print(proposal):
    print("\n\n----- Configuration created on " + datetime.today().strftime('%Y-%m-%d') + "-----")
    print(proposal[0].pretty_ptint())
    if proposal[1]:
        print(proposal[1].pretty_ptint())
    if proposal[2]:
        print(proposal[2].pretty_ptint())
    print("Rewards earned: " + str(proposal[3][0]) + " Spheres and " + str(proposal[3][1]) + " dust.")
    print("Remaining Attacks: " + str(proposal[4]))
    print("Player assignment print: ")
    for player in proposal[5]:
        string = "@" + player[0] + ": "
        for e in player[1]:
            string = string + e + ", \t"
        print(string)


configurations = []
top_reward = [0, 0]

args = parser.parse_args()
csv_file = ""
if args.csv_file:
    csv_file = args.csv_file
else:
    print("[!] No player data provided. Exiting!")
    exit(-1)

for i in range(0, args.amount):
    new_configuration = Configuration(csv_file)
    proposal = new_configuration.create_proposal()
    if i % 1000 == 0:
        print("Proposal "+str(i)+" generated. Current top reward: "+str(top_reward))
    if top_reward[0] <= proposal[3][0] and top_reward[1] <= proposal[3][1]:
        top_reward = proposal[3]
    configurations.append(proposal)

sorted_config = [s for s in configurations if s[3] == top_reward]
sorted_config = sorted(sorted_config, key=lambda c: c[4], reverse=True)

for c in sorted_config[0:3]:
    pretty_print(c)

print("All done, have fun with your gains!")





