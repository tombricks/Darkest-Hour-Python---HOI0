from nationClass import *
import os

colours = {}
with open("history/colours.txt", 'r') as temptext:
    text = temptext.readlines()
    for x in text:
        line = x.split(' ')
        colours[line[0]] = int(line[1]), int(line[2]), int(line[3]), int(line[4])

print(colours)

def createLeader(file):
    with open("history/leaders/"+file, 'r') as temptext:
        text = temptext.readlines()
        id = ""
        ideology = ""
        for x in text:
            line = x.split()
            if line[0] == "id":
                id = line[1]
            elif line[0] == "ideology":
                ideology = line[1]
        leaders[id] = leader(id, ideology)

def createNation(file):
    with open("history/countries/"+file, 'r') as temptext:
        text = temptext.readlines()
        tag = ""
        ideology = ""
        culture = ""
        colour = ""
        communist_leader = ""
        communist_popularity = ""
        fascist_leader = ""
        fascist_popularity = ""
        democratic_leader = ""
        democratic_popularity = ""
        neutrality_leader = ""
        neutrality_popularity = ""
        for x in text:
            line = x.split()
            if line[0] == "tag": tag = line[1]
            elif line[0] == "ideology": ideology = line[1]
            elif line[0] == "culture": culture = line[1]
            elif line[0] == "colour": colour = colours[line[1]]
            elif line[0] == "communist_leader": communist_leader = leaders[line[1]]
            elif line[0] == "communist_popularity": communist_popularity = int(line[1])
            elif line[0] == "fascist_leader": fascist_leader = leaders[line[1]]
            elif line[0] == "fascist_popularity": fascist_popularity = int(line[1])
            elif line[0] == "democratic_leader": democratic_leader = leaders[line[1]]
            elif line[0] == "democratic_popularity": democratic_popularity = int(line[1])
            elif line[0] == "neutrality_leader": neutrality_leader = leaders[line[1]]
            elif line[0] == "neutrality_popularity": neutrality_popularity = int(line[1])
        nations[tag] = nation(tag, ideology, culture, communist_popularity, fascist_popularity, democratic_popularity, neutrality_popularity, colour, communist_leader, fascist_leader, democratic_leader, neutrality_leader)

#Leaders
leaders = {}
nations = {}
for filename in os.listdir('history/leaders/'):
    createLeader(filename)
for filename in os.listdir('history/countries/'):
    createNation(filename)