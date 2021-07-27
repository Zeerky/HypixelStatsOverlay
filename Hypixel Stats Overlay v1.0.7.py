#REALLY IMPORTANT PLEASE READ
#FIRST YOU MUST INSTALL THE LATEST VERSION OF PYTHON FROM python.org
#YOU NEED TO EITHER RUN THE modules.bat FILE OR DO THE FOLLOWING
#OPEN COMMAND PROMPT AND TYPE
#pip install requests
#pip install 



#PLACE YOUR UUID (WITH DASHES) INBETWEEN THE QUOTES IN THE NEXT LINE
uuid = "4aa19464-3860-42eb-8af9-63ff4114d377" 


#PLACE YOUR API KEY INBETWEEN THE QUOTES IN THE NEXT LINE
key = "60dc9492-3ebc-4657-8cc4-dfe171018353"

#HOW TO GET YOUR UUID AND API KEY
#STEP 1: GOTO NAMEMC.COM AND LOOK UP YOUR IGN (OR WHOEVER'S STATS YOUR PULLING)
#STEP 2: COPY YOUR UUID (WITH THE DASHES) AND PASTE IT IN THE 2ND LINE
#STEP 3: LOG ONTO HYPIXEL.NET AND TYPE /api new IN THE CHAT
#STEP 4: COPY THE KEY IT GIVES YOU AND PASTE IT IN THE 6TH LINE

#IF YOU WANT TO CHANGE THE SIZE OF THE TEXT MESS AROUND WITH THIS NUMBER
textSize = 40

#YOU CNA CHANGE THE COlOR OF THE TEXT BY EITHER PUTTING A HEX VALUE OR JUST TYPING "red"
textColor = "#09d2f6"

#DO NOT CHANGE ANYTHING UNDER THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING
#IF YOU HAVE ANY QUESTIONS/SUGGESTIONS COME JOIN AT discord.gg/Bu86veVgjT





from tkinter import *
import requests
import json
from pprint import pprint
import time



windowWidth = 500
windowHeight = 400


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
    print("\n" * 27)
    print("                    **KEEP THIS WINDOW OPEN**                             **KEEP THIS WINDOW OPEN**")
    print("            **CLOSING THIS WINDOW CLOSES THE OVERLAY**            **CLOSING THIS WINDOW CLOSES THE OVERLAY**")
    print("\n" * 5)
    print("                  ******************************                      ******************************")
    print("                **YOU CAN MOVE THE WINDOW AROUND**                  **YOU CAN MOVE THE WINDOW AROUND**")
    print("             **BY CLICKING AND DRAGGING ON THE TEXT**             **BY CLICKING AND DRAGGING ON THE TEXT**")
    print("              **LOOK IN THE CODE TO CHANGE TEXT SIZE**            **LOOK IN THE CODE TO CHANGE TEXT SIZE**")
    print("                **********************************                  **********************************")
    print("\n" * 5)
    print("                    **KEEP THIS WINDOW OPEN**                             **KEEP THIS WINDOW OPEN**")
    print("           **CLOSING THIS WINDOW CLOSES THE OVERLAY**             **CLOSING THIS WINDOW CLOSES THE OVERLAY**")
    print("\n" * 5)

def statsCallMain():
    print("1: Duels")
    print("2: Bedwars")
    print("3: Skywars")
    userGame = input()

    if userGame == "duels" or userGame == "Duels" or userGame == "1":
        print("\n" * 27)
        statsCallDuels()
    elif userGame == "bedwars" or userGame == "Bedwars" or userGame == "2" or userGame == "bw" or userGame == "BW":
        warnUser()
        statsCallBedwars()
    elif userGame == "skywars" or userGame == "Skywars" or userGame == "3" or userGame == "sw" or userGame == "SW":
        warnUser()
        statsCallSkywars()    
    else:
        print("\n" * 27)
        print('Please try again')
        statsCallMain()

    #BEDWARS

def statsCallBedwars():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Bedwars"]["wins_bedwars"]) > 0:
            bedwarsWins = data["player"]["stats"]["Bedwars"]["wins_bedwars"]
    except KeyError:
        bedwarsWins = 0
    try:    
        if int(data["player"]["stats"]["Bedwars"]["losses_bedwars"]) > 0:
            bedwarsLosses = data["player"]["stats"]["Bedwars"]["losses_bedwars"]
    except KeyError:
        bedwarsLosses = 0
    try:    
        if int(data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]) > 0:
            bedwarsFinals = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
    except KeyError:
        bedwarsFinals = 0
    my_label.config(text="Bedwars Wins: " + str(bedwarsWins) + "\nBedwars Losses: " + str(bedwarsLosses) + "\n Bedwars Finals: " + str(bedwarsFinals))
    root.after(30000,statsCallBedwars)

    #SKYWARS

def statsCallSkywars():
    data = requests.get(url).json()
    print(data["player"]["stats"]["SkyWars"]["wins"])
    try:
        if int(data["player"]["stats"]["SkyWars"]["wins"]) > 0:
            skywarsWins = data["player"]["stats"]["SkyWars"]["wins"]
    except KeyError:
        skywarsWins = 0
    try:    
        if int(data["player"]["stats"]["SkyWars"]["losses"]) > 0:
            skywarsLosses = data["player"]["stats"]["SkyWars"]["losses"]
    except KeyError:
        skywarsLosses = 0
    try:    
        if int(data["player"]["stats"]["SkyWars"]["kills"]) > 0:
            skywarsKills = data["player"]["stats"]["SkyWars"]["kills"]
    except KeyError:
        skywarsKills = 0
    try:    
        if int(data["player"]["stats"]["SkyWars"]["deaths"]) > 0:
            skywarsDeaths = data["player"]["stats"]["SkyWars"]["deaths"]
    except KeyError:
        skywarsDeaths = 0
    my_label.config(text="Skywars Wins: " + str(skywarsWins) + "\nSkywars Losses: " + str(skywarsLosses) + "\n Skywars Kills: " + str(skywarsKills) + "\nSkywars Deaths: " + str(skywarsDeaths))
    root.after(30000,statsCallSkywars)



def statsCallDuels():
    print("1: Bridge")
    print("2: UHC")
    print("3: OP")
    print("4: Classic")
    print("5: Skywars")
    print("6: Sumo")
    print("7: Bow")
    print("8: BowSpleef")
    #print("9: Nodebuff")
    #print("10: Combo")
    #print("11: Blitz")
    #print("12: MegaWalls")

    userChoice = input()

    #BRIDGE DUELS

    if userChoice == "bridge" or userChoice == "Bridge" or userChoice == "1":
        data = requests.get(url).json()
        try:
            if int(data["player"]["stats"]["Duels"]["bridge_duel_wins"]) > 0:
                bridgeWins = data["player"]["stats"]["Duels"]["bridge_duel_wins"]
        except KeyError:
            bridgeWins = 0
        try:    
            if int(data["player"]["stats"]["Duels"]["bridge_duel_losses"]) > 0:
                bridgeLosses = data["player"]["stats"]["Duels"]["bridge_duel_losses"]
        except KeyError:
            bridgeLosses = 0
        warnUser()
        my_label.config(text="Bridge Wins: " + str(bridgeWins) + "\nBridge Losses: " + str(bridgeLosses))
        root.after(30000,statsCallBridge)

    #UHC DUELS

    elif userChoice == "uhc" or userChoice == "UHC" or userChoice == "2":
        data = requests.get(url).json()
        try:
            if int(data["player"]["stats"]["Duels"]["uhc_duel_wins"]) > 0:
                uhcWins = data["player"]["stats"]["Duels"]["uhc_duel_wins"]
        except KeyError:
            uhcWins = 0
        try:    
            if int(data["player"]["stats"]["Duels"]["uhc_duel_losses"]) > 0:
                uhcLosses = data["player"]["stats"]["Duels"]["uhc_duel_losses"]
        except KeyError:
            uhcLosses = 0
        my_label.config(text="UHC Wins: " + str(uhcWins) + "\nUHC Losses: " + str(uhcLosses))
        root.after(30000,statsCallUHC)

    #OP DUELS

    elif userChoice == "op" or userChoice == "OP" or userChoice == "3":
        data = requests.get(url).json()
        try:
            if int(data["player"]["stats"]["Duels"]["op_duel_wins"]) > 0:
                opWins = data["player"]["stats"]["Duels"]["op_duel_wins"]
        except KeyError:
            opWins = 0
        try:    
            if int(data["player"]["stats"]["Duels"]["op_duel_losses"]) > 0:
                opLosses = data["player"]["stats"]["Duels"]["op_duel_losses"]
        except KeyError:
            opLosses = 0
        my_label.config(text="OP Wins: " + str(opWins) + "\nOP Losses: " + str(opLosses))
        root.after(30000,statsCallOP)

    #CLASSIC DUELS

    elif userChoice == "classic" or userChoice == "Classic" or userChoice == "4":
        data = requests.get(url).json()
        try:
            if int(data["player"]["stats"]["Duels"]["classic_duel_wins"]) > 0:
                classicWins = data["player"]["stats"]["Duels"]["classic_duel_wins"]
        except KeyError:
            classicWins = 0
        try:    
            if int(data["player"]["stats"]["Duels"]["classic_duel_losses"]) > 0:
                classicLosses = data["player"]["stats"]["Duels"]["classic_duel_losses"]
        except KeyError:
            classicLosses = 0
        my_label.config(text="Classic Wins: " + str(classicWins) + "\nClassic Losses: " + str(classicLosses))
        root.after(30000,statsCallClassic)

    #SKYWARS DUELS

    elif userChoice == "skywars" or userChoice == "Skywars" or userChoice == "5" or userChoice == "sw" or userChoice == "SW":
        data = requests.get(url).json()
        try:
            if int(data["player"]["stats"]["Duels"]["sw_duel_wins"]) > 0:
                swWins = data["player"]["stats"]["Duels"]["sw_duel_wins"]
        except KeyError:
            swWins = 0
        try:    
            if int(data["player"]["stats"]["Duels"]["sw_duel_losses"]) > 0:
                swLosses = data["player"]["stats"]["Duels"]["sw_duel_losses"]
        except KeyError:
            swLosses = 0
        my_label.config(text="SW Wins: " + str(swWins) + "\nSW Losses: " + str(swLosses))
        root.after(30000,statsCallSW)

    #SUMO DUELS

    elif userChoice == "sumo" or userChoice == "Sumo" or userChoice == "6":
        data = requests.get(url).json()
        try:
            if int(data["player"]["stats"]["Duels"]["sumo_duel_wins"]) > 0:
                sumoWins = data["player"]["stats"]["Duels"]["sumo_duel_wins"]
        except KeyError:
            sumoWins = 0
        try:    
            if int(data["player"]["stats"]["Duels"]["sumo_duel_losses"]) > 0:
                sumoLosses = data["player"]["stats"]["Duels"]["sumo_duel_losses"]
        except KeyError:
            sumoLosses = 0
        my_label.config(text="Sumo Wins: " + str(sumoWins) + "\nSumo Losses: " + str(sumoLosses))
        root.after(30000,statsCallSumo)

    #BOW DUELS

    elif userChoice == "bow" or userChoice == "Bow" or userChoice == "7":
        data = requests.get(url).json()
        try:
            if int(data["player"]["stats"]["Duels"]["bow_duel_wins"]) > 0:
                bowWins = data["player"]["stats"]["Duels"]["bow_duel_wins"]
        except KeyError:
            bowWins = 0
        try:    
            if int(data["player"]["stats"]["Duels"]["bow_duel_losses"]) > 0:
                bowLosses = data["player"]["stats"]["Duels"]["bow_duel_losses"]
        except KeyError:
            bowLosses = 0
        my_label.config(text="Bow Wins: " + str(bowWins) + "\nBow Losses: " + str(bowLosses))
        root.after(30000,statsCallBow)     

    #BowSpleef

    elif userChoice == "bowspleef" or userChoice == "BowSpleef" or userChoice == "8" or userChoice == "Bowspleef":
        data = requests.get(url).json()
        try:
            if int(data["player"]["stats"]["Duels"]["bowspleef_duel_wins"]) > 0:
                bowSpleefWins = data["player"]["stats"]["Duels"]["bowspleef_duel_wins"]
        except KeyError:
            bowSpleefWins = 0
        try:    
            if int(data["player"]["stats"]["Duels"]["bowspleef_duel_losses"]) > 0:
                bowSpleefLosses = data["player"]["stats"]["Duels"]["bowspleef_duel_losses"]
        except KeyError:
            bowSpleefLosses = 0
        my_label.config(text="BowSpleef Wins: " + str(bowSpleefWins) + "\nBowSpleef Losses: " + str(bowSpleefLosses))
        root.after(30000,statsCallBowSpleef) 

#    print("9: Nodebuff")
#    print("10: Combo")
#    print("11: Blitz")
#    print("12: MegaWalls")

    else:
        print("\n" * 27)
        print("Please make sure you spelt the game correctly!")
        statsCallMain()
def statsCallBridge():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["bridge_duel_wins"]) > 0:
            bridgeWins = data["player"]["stats"]["Duels"]["bridge_duel_wins"]
    except KeyError:
        bridgeWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["bridge_duel_losses"]) > 0:
            bridgeLosses = data["player"]["stats"]["Duels"]["bridge_duel_losses"]
    except KeyError:
        bridgeLosses = 0
    warnUser()
    my_label.config(text="Bridge Wins: " + str(bridgeWins) + "\nBridge Losses: " + str(bridgeLosses))
    root.after(30000,statsCallBridge)

def statsCallUHC():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["uhc_duel_wins"]) > 0:
            uhcWins = data["player"]["stats"]["Duels"]["uhc_duel_wins"]
    except KeyError:
        uhcWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["uhc_duel_losses"]) > 0:
            uhcLosses = data["player"]["stats"]["Duels"]["uhc_duel_losses"]
    except KeyError:
        uhcLosses = 0
    my_label.config(text="UHC Wins: " + str(uhcWins) + "\nUHC Losses: " + str(uhcLosses))
    root.after(30000,statsCallUHC)

def statsCallOP():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["op_duel_wins"]) > 0:
            opWins = data["player"]["stats"]["Duels"]["op_duel_wins"]
    except KeyError:
        opWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["op_duel_losses"]) > 0:
            opLosses = data["player"]["stats"]["Duels"]["op_duel_losses"]
    except KeyError:
        opLosses = 0
    my_label.config(text="OP Wins: " + str(opWins) + "\nOP Losses: " + str(opLosses))
    root.after(30000,statsCallOP)

def statsCallClassic():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["classic_duel_wins"]) > 0:
            classicWins = data["player"]["stats"]["Duels"]["classic_duel_wins"]
    except KeyError:
        classicWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["classic_duel_losses"]) > 0:
            classicLosses = data["player"]["stats"]["Duels"]["classic_duel_losses"]
    except KeyError:
        classicLosses = 0
    my_label.config(text="Classic Wins: " + str(classicWins) + "\nClassic Losses: " + str(classicLosses))
    root.after(30000,statsCallClassic)

def statsCallSW():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["sw_duel_wins"]) > 0:
            swWins = data["player"]["stats"]["Duels"]["sw_duel_wins"]
    except KeyError:
        swWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["sw_duel_losses"]) > 0:
            swLosses = data["player"]["stats"]["Duels"]["sw_duel_losses"]
    except KeyError:
        swLosses = 0
    my_label.config(text="SW Wins: " + str(swWins) + "\nSW Losses: " + str(swLosses))
    root.after(30000,statsCallSW)

def statsCallBow():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["bow_duel_wins"]) > 0:
            bowWins = data["player"]["stats"]["Duels"]["bow_duel_wins"]
    except KeyError:
        bowWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["bow_duel_losses"]) > 0:
            bowLosses = data["player"]["stats"]["Duels"]["bow_duel_losses"]
    except KeyError:
        bowLosses = 0
    my_label.config(text="Bow Wins: " + str(bowWins) + "\nBow Losses: " + str(bowLosses))
    root.after(30000,statsCallBow) 

def statsCallBowSpleef():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["bowspleef_duel_wins"]) > 0:
            bowSpleefWins = data["player"]["stats"]["Duels"]["bowspleef_duel_wins"]
    except KeyError:
        bowSpleefWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["bowspleef_duel_losses"]) > 0:
            bowSpleefLosses = data["player"]["stats"]["Duels"]["bowspleef_duel_losses"]
    except KeyError:
        bowSpleefLosses = 0
    my_label.config(text="BowSpleef Wins: " + str(bowSpleefWins) + "\nBowSpleef Losses: " + str(bowSpleefLosses))
    root.after(30000,statsCallBowSpleef) 

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
