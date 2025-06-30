import json
import os
import time
import re

tf2Path = "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf"
consoleOutputPath = f"{tf2Path}/console.txt"
playerClasses = {}

#               Open the weapons.json file
with open('./weapons.json', 'r') as file:
    weaponClasses = json.load(file)


#               Gets the weapon of a player; if there is no weapon it returns none
def checkPlayerWeapon(msg):
    match = re.match(r"(.+?) killed (.+?) with", msg)
    if match:
        player = match.group(1).strip()
    else:
        player = None
    playerClass = None

    if "killed" in msg:
        keyword = str(msg).split()[-1].rstrip('.')
        for cls, weapon in weaponClasses.items():
            if keyword in weapon:
                playerClass = cls
                break
    return(player, playerClass)

def updateClass(player, newClass):
    if player not in playerClasses:
        playerClasses[player] = newClass
        print(f"{player} is now a {newClass}")
        
    elif playerClasses[player] != newClass:
        playerClasses[player] = newClass
        print(f"{player} is now a {newClass}")

if __name__ == "__main__":

    last_modified_time = 0
    outputLines = []
    while True:
        try:
#               Check if the file has been modified
            current_modified_time = os.path.getmtime(consoleOutputPath)
            if current_modified_time > last_modified_time:
                last_modified_time = current_modified_time

                with open(consoleOutputPath, 'r', encoding='utf-8', errors="ignore") as file:
                    lines = file.readlines()
                for line in lines:
                    outputLines.append(line)

#               Process all new lines
                for line in outputLines:
                    result = checkPlayerWeapon(line)
                    if result[1] != None:
                        updateClass(result[0], result[1])

#               Clear the file only after processing all new lines
                with open(consoleOutputPath, 'w', encoding='utf-8', errors="ignore") as file:
                    pass
                outputLines.clear()

        except FileNotFoundError:
            print("ERROR: File not found!")
            time.sleep(1)
            continue
        except Exception as e:
            print(f"ERROR: {e}")
            time.sleep(1)
            continue
        time.sleep(0.5)
