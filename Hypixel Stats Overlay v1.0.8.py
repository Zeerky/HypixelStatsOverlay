#REALLY IMPORTANT PLEASE READ
#FIRST YOU MUST INSTALL THE LATEST VERSION OF PYTHON FROM python.org
#YOU NEED TO EITHER RUN THE modules.bat FILE OR DO THE FOLLOWING
#OPEN COMMAND PROMPT AND TYPE
#pip install requests
#pip install



#PLACE YOUR UUID (WITH DASHES) INBETWEEN THE QUOTES IN THE NEXT LINE
uuid = "462baa14-fc68-46d6-a87b-4dc1fa070f21"


#PLACE YOUR API KEY INBETWEEN THE QUOTES IN THE NEXT LINE
key = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

#HOW TO GET YOUR UUID AND API KEY
#STEP 1: GOTO NAMEMC.COM AND LOOK UP YOUR IGN (OR WHOEVER'S STATS YOUR PULLING)
#STEP 2: COPY YOUR UUID (WITH THE DASHES) AND PASTE IT IN THE 2ND LINE
#STEP 3: LOG ONTO HYPIXEL.NET AND TYPE /api new IN THE CHAT
#STEP 4: COPY THE KEY IT GIVES YOU AND PASTE IT IN THE 6TH LINE

#IF YOU WANT TO CHANGE THE SIZE OF THE TEXT MESS AROUND WITH THIS NUMBER
textSize = int(40.2)

#YOU CNA CHANGE THE COlOR OF THE TEXT BY EITHER PUTTING A HEX VALUE OR JUST TYPING "red"
textColor = "#09d2f6"

#DO NOT CHANGE ANYTHING UNDER THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING
#IF YOU HAVE ANY QUESTIONS/SUGGESTIONS COME JOIN AT discord.gg/Bu86veVgjT





from tkinter import *
import requests
import json
from pprint import pprint
import time



windowWidth = textSize * 12
windowHeight = textSize * 8



print("\n" * 27)


#while True:
#    try:
#        if "Win32Window" in str(gw.getWindowsWithTitle('Lunar')[0]):
#            print("Found Lunar!")
#            time.sleep(1)
#            break
#    except IndexError:
#        print("Cannot find Lunar!")
#        input("Press enter to exit")
#        exit()
#
#lunarWindow = gw.getWindowsWithTitle('Lunar')[0]
def warnUser():

    print("\n"*27,"""
                        **KEEP THIS WINDOW OPEN**                             **KEEP THIS WINDOW OPEN**
                **CLOSING THIS WINDOW CLOSES THE OVERLAY**            **CLOSING THIS WINDOW CLOSES THE OVERLAY**""",
    "\n" * 5,
        """           ******************************                      ******************************
                    **YOU CAN MOVE THE WINDOW AROUND**                  **YOU CAN MOVE THE WINDOW AROUND**
                 **BY CLICKING AND DRAGGING ON THE TEXT**             **BY CLICKING AND DRAGGING ON THE TEXT**
                  **LOOK IN THE CODE TO CHANGE TEXT SIZE**            **LOOK IN THE CODE TO CHANGE TEXT SIZE**
                    **********************************                  **********************************""",
    "\n" * 5,
        """             **KEEP THIS WINDOW OPEN**                             **KEEP THIS WINDOW OPEN**
               **CLOSING THIS WINDOW CLOSES THE OVERLAY**             **CLOSING THIS WINDOW CLOSES THE OVERLAY**""",
    "\n" * 5)

def statsCallMain():
    print("""1: Duels
    2: Bedwars
    3: Skywars
    """)
    user_game = input().lower()

    # Duels selection
    if (user_game in ["duels", '1']):
        warnUser()
        statsCallDuels()

    # Bedwars selection
    elif (user_game in ["bedwars", "bw", '2']):
        warnUser()
        statsCallBedwars()

    # Skywars selection
    elif (user_game in ["skywars", "sw", '3']):
        warnUser()
        statsCallSkywars()

    # Invalid choice
    else:
        print(f"""{"\n" * 27}
        Please try again""")
        statsCallMain()

# Duels stats
def statsCallDuels():
    print("1: Bridge")
    print("2: UHC")
    print("3: OP")
    print("4: Classic")
    print("5: Skywars")
    print("6: Sumo")
    print("7: Bow")
    print("8: BowSpleef")
    print("9: Nodebuff")
    print("10: Combo")
    print("11: Blitz")
    print("12: MegaWalls")

    userChoice = input()

    #BRIDGE DUELS
    if userChoice == "bridge" or userChoice == "Bridge" or userChoice == "1":
        statsCallBridge()

    #UHC DUELS
    elif userChoice == "uhc" or userChoice == "UHC" or userChoice == "2":
        statsCallUHC()

    #OP DUELS
    elif userChoice == "op" or userChoice == "OP" or userChoice == "3":
        statsCallOP()

    #CLASSIC DUELS
    elif userChoice == "classic" or userChoice == "Classic" or userChoice == "4":
        statsCallClassic()

    #SKYWARS DUELS
    elif userChoice == "skywars" or userChoice == "Skywars" or userChoice == "5" or userChoice == "sw" or userChoice == "SW":
        statsCallSkywars

    #SUMO DUELS
    elif userChoice == "sumo" or userChoice == "Sumo" or userChoice == "6":
        statsCallSumo()

    #BOW DUELS
    elif userChoice == "bow" or userChoice == "Bow" or userChoice == "7":
        statsCallBow()

    #BOWSPLEEF DUELS
    elif userChoice == "bowspleef" or userChoice == "BowSpleef" or userChoice == "8" or userChoice == "Bowspleef":
        statsCallBowSpleef()

    #NODEBUFF DUELS
    elif userChoice == "nodebuff" or userChoice == "Nodebuff" or userChoice == "9" or userChoice == "NoDebuff":
        statsCallNodebuff()

    #COMBO DUELS
    elif userChoice == "combo" or userChoice == "Combo" or userChoice == "10":
        statsCallCombo()

    #BLITZ DUELS
    elif userChoice == "blitz" or userChoice == "Blitz" or userChoice == "11":
        statsCallBlitz()

    #MEGAWALLS DUELS
    elif userChoice == "megawalls" or userChoice == "Megawalls" or userChoice == "12" or userChoice == "MegaWalls":
        statsCallMegawalls()

    else:
        print("\n" * 27)
        print("Please make sure you spelt the game correctly!")
        statsCallMain()

def statsCallBedwars():
    data = requests.get(url).json()

    bedwars_wins = int(data['player']['stats']['Bedwars'].get('wins_bedwars', 0))
    bedwars_losses = int(data['player']['stats']['Bedwars'].get('losses_bedwars', 0))
    bedwars_finals = int(data['player']['stats']['Bedwars'].get('final_kills_bedwars', 0))

    my_label.config(text=f"Bedwars Wins: {bedwars_wins}\nBedwars Losses: {bedwars_losses}\nBedwars Finals: {bedwars_finals}")
    root.after(5000, statsCallBedwars)

def statsCallSkywars():
    data = requests.get(url).json()

    skywars_wins = int(data['player']['stats']['Skywars'].get('wins', 0))
    skywars_losses = int(data['player']['stats']['Skywars'].get('losses', 0))
    skywars_kills = int(data['player']['stats']['Skywars'].get('kills', 0))
    skywars_deaths = int(data['player']['stats']['Skywars'].get('deaths', 0))

    my_label.config(text=f"Skywars Wins: {skywars_wins}\nSkywars Losses: {skywars_losses}\nSkywars Kills: {skywars_kills}\nSkywars Deaths: {skywars_deaths}")
    root.after(5000, statsCallSkywars)

def statsCallBridge():
    root.lift()
    data = requests.get(url).json()
    bridgeWins = data["player"]["stats"]["Duels"].get("bridge_duel_wins", 0)
    bridgeLosses = data["player"]["stats"]["Duels"].get("bridge_duel_losses", 0)
    warnUser()
    root.wm_attributes("-topmost", 1)
    my_label.config(text="Bridge Wins: " + str(bridgeWins) + "\nBridge Losses: " + str(bridgeLosses))
    root.after(5000,statsCallBridge)

def statsCallUHC():
    data = requests.get(url).json()
    uhcWins = data["player"]["stats"]["Duels"].get("uhc_duel_wins", 0)
    uhcLosses = data["player"]["stats"]["Duels"].get("uhc_duel_losses", 0)
    warnUser()
    my_label.config(text="UHC Wins: " + str(uhcWins) + "\nUHC Losses: " + str(uhcLosses))
    root.after(5000,statsCallUHC)

def statsCallOP():
    data = requests.get(url).json()
    opWins = data["player"]["stats"]["Duels"].get("op_duel_wins", 0)
    opLosses = data["player"]["stats"]["Duels"].get("op_duel_losses", 0)
    warnUser()
    my_label.config(text="OP Wins: " + str(opWins) + "\nOP Losses: " + str(opLosses))
    root.after(5000,statsCallOP)

def statsCallClassic():
    data = requests.get(url).json()
    classicWins = data["player"]["stats"]["Duels"].get("classic_duel_wins", 0)
    classicLosses = data["player"]["stats"]["Duels"].get("classic_duel_losses", 0)
    warnUser()
    my_label.config(text="Classic Wins: " + str(classicWins) + "\nClassic Losses: " + str(classicLosses))
    root.after(5000,statsCallClassic)

def statsCallSW():
    data = requests.get(url).json()
    swWins = data["player"]["stats"]["Duels"].get("sw_duel_wins", 0)
    swLosses = data["player"]["stats"]["Duels"].get("sw_duel_losses", 0)
    warnUser()
    my_label.config(text="SW Wins: " + str(swWins) + "\nSW Losses: " + str(swLosses))
    root.after(5000,statsCallSW)

def statsCallSumo():
    data = requests.get(url).json()
    #Tries to get Sumo wins/losses if there aren't any set to 0
    sumoWins = data["player"]["stats"]["Duels"].get("sumo_duel_wins", 0)
    sumoLosses = data["player"]["stats"]["Duels"].get("sumo_duel_losses", 0)
    warnUser()
    #Changes the text on the overlay
    my_label.config(text="Sumo Wins: " + str(sumoWins) + "\nSumo Losses: " + str(sumoLosses))
    #Updates the text every 5s
    root.after(5000,statsCallSumo)

def statsCallBow():
    data = requests.get(url).json()
    bowWins = data["player"]["stats"]["Duels"].get("bow_duel_wins", 0)
    bowLosses = data["player"]["stats"]["Duels"].get("bow_duel_losses", 0)
    warnUser()
    my_label.config(text="Bow Wins: " + str(bowWins) + "\nBow Losses: " + str(bowLosses))
    root.after(5000,statsCallBow)

def statsCallBowSpleef():
    data = requests.get(url).json()
    bowSpleefWins = data["player"]["stats"]["Duels"].get("bowspleef_duel_wins", 0)
    bowSpleefLosses = data["player"]["stats"]["Duels"].get("bowspleef_duel_losses", 0)
    warnUser()
    my_label.config(text="BowSpleef Wins: " + str(bowSpleefWins) + "\nBowSpleef Losses: " + str(bowSpleefLosses))
    root.after(5000,statsCallBowSpleef)

def statsCallNodebuff():
    data = requests.get(url).json()
    nodebuffWins = data["player"]["stats"]["Duels"].get("no_debuff_duel_wins", 0)
    nodebuffLosses = data["player"]["stats"]["Duels"].get("no_debuff_duel_losses", 0)
    warnUser()
    my_label.config(text="Nodebuff Wins: " + str(nodebuffWins) + "\nNodebuff Losses: " + str(nodebuffLosses))
    root.after(5000,statsCallNodebuff)

def statsCallCombo():
    data = requests.get(url).json()
    comboWins = data["player"]["stats"]["Duels"].get("combo_duel_wins", 0)
    comboLosses = data["player"]["stats"]["Duels"].get("combo_duel_losses", 0)
    warnUser()
    my_label.config(text="Combo Wins: " + str(comboWins) + "\nCombo Losses: " + str(comboLosses))
    root.after(5000,statsCallCombo)

def statsCallBlitz():
    data = requests.get(url).json()
    blitzWins = data["player"]["stats"]["Duels"].get("blitz_duel_wins", 0)
    blitzLosses = data["player"]["stats"]["Duels"].get("blitz_duel_losses", 0)
    warnUser()
    my_label.config(text="Blitz Wins: " + str(blitzWins) + "\nBlitz Losses: " + str(blitzLosses))
    root.after(5000,statsCallBlitz)

def statsCallMegawalls():
    data = requests.get(url).json()
    megawallsWins = data["player"]["stats"]["Duels"].get("mega_walls_duel_wins", 0)
    megawallsLosses = data["player"]["stats"]["Duels"].get("mega_walls_duel_losses", 0)
    warnUser()
    my_label.config(text="Megawalls Wins: " + str(megawallsWins) + "\nMegawalls Losses: " + str(megawallsLosses))
    root.after(5000,statsCallMegawalls)



#MAIN WINDOW
root = Tk()
root.title('Test Title')
root.geometry(str(windowWidth) + "x" + str(windowHeight))
#MAKE TRANSPARENT
root.wm_attributes('-transparentcolor', root['bg'])
root.wm_attributes("-topmost", 1)
#REMOVES TITLE BAR
root.overrideredirect(1)



#shitty click and drag function
def move(event):
    x, y = root.winfo_pointerxy()
    root.geometry(f"+{x}+{y}")

root.bind('<B1-Motion>',move)

#the window (i think?)
my_frame = Frame(root, width=windowWidth, height=windowHeight)
my_frame.pack(pady=20, ipady=20, ipadx=20)

#label that draws text
my_label = Label(my_frame, font=("Rockwell", textSize), fg=textColor)
my_label.pack(pady=20)

#hypixel api url
url = f"https://api.hypixel.net/player?key={key}&uuid={uuid}"
data = statsCallMain()

root.mainloop()
