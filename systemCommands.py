import os
import yaml
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def pause():
    os.system("pause")
def repeatLine(num, string=""):
    for x in range(0, num):
        print(string)        
def doesFileExist(file):
    return os.path.exists(file)

with open('localisation.yml') as f:
    localisation = yaml.load(f, Loader=yaml.FullLoader)