#REALLY IMPORTANT PLEASE READ
#FIRST YOU MUST INSTALL THE LATEST VERSION OF PYTHON FROM python.org
#YOU NEED TO EITHER RUN THE modules.bat FILE *OR* DO THE FOLLOWING
#OPEN COMMAND PROMPT AND TYPE
#pip install requests
#pip install pyglet
#YOU ONLY NEED TO DO THIS ONCE




#HOW TO GET YOUR UUID AND API KEY
#STEP 1: GOTO NAMEMC.COM AND LOOK UP YOUR IGN (OR WHOEVER'S STATS YOUR PULLING)
#STEP 2: COPY YOUR UUID (WITH THE DASHES) AND PASTE IT IN THE 2ND LINE
#STEP 3: LOG ONTO HYPIXEL.NET AND TYPE /api new IN THE CHAT
#STEP 4: COPY THE KEY IT GIVES YOU AND PASTE IT IN THE 6TH LINE

#PLACE YOUR UUID (WITH DASHES) INBETWEEN THE QUOTES IN THE NEXT LINE
uuid = "xxx"

#PLACE YOUR API KEY INBETWEEN THE QUOTES IN THE NEXT LINE
key = "xxx"

#IF YOU WANT TO CHANGE THE SIZE OF THE TEXT MESS AROUND WITH THIS NUMBER
textSize = int(35)

#DELAY TO UPDATE THE STATS ON THE OVERLAY (dont put this too low)
refreshTime = 2000 #will refresh overlay every 2 seconds. if its laggy, try turning this to 5000

#YOU CAN CHANGE THE COlOR OF THE TEXT BY EITHER PUTTING A HEX VALUE OR JUST TYPING "red"
textColor = "#09d2f6"

#FONT SETTINGS
import pyglet
pyglet.font.add_file('Minecraft.ttf')
textFont = "MinecraftCHMC"

#    ------------------------------------------------------------------------
#   |DO NOT CHANGE ANYTHING UNDER THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING |
#   |IF YOU HAVE ANY QUESTIONS/SUGGESTIONS COME JOIN AT discord.gg/Bu86veVgjT |
#    ------------------------------------------------------------------------

from tkinter import *
import requests
import json
from pprint import pprint
import time



url = f"https://api.hypixel.net/player?key={key}&uuid={uuid}"


windowWidth = textSize * 17
windowHeight = textSize * 11

def openBW():
	closeOverlay()
	global gameMode
	gameMode = "bw"
	openOverlay()

def openSkywars():
	closeOverlay()
	global gameMode
	gameMode = "skywars"
	openOverlay()

def openBridge():
	closeOverlay()
	global gameMode
	gameMode = "bridge"
	openOverlay()

def openUHC():
	closeOverlay()
	global gameMode
	gameMode = "uhc"
	openOverlay()

def openOP():
	closeOverlay()
	global gameMode
	gameMode = "op"
	openOverlay()

def openClassic():
	closeOverlay()
	global gameMode
	gameMode = "classic"
	openOverlay()

def openSW():
	closeOverlay()
	global gameMode
	gameMode = "sw"
	openOverlay()

def openSumo():
	closeOverlay()
	global gameMode
	gameMode = "sumo"
	openOverlay()

def openBow():
	closeOverlay()
	global gameMode
	gameMode = "bow"
	openOverlay()

def openTNT():
	closeOverlay()
	global gameMode
	gameMode = "tnt"
	openOverlay()

def openPotion():
	closeOverlay()
	global gameMode
	gameMode = "potion"
	openOverlay()

def openCombo():
	closeOverlay()
	global gameMode
	gameMode = "combo"
	openOverlay()

def openBlitz():
	closeOverlay()
	global gameMode
	gameMode = "blitz"
	openOverlay()

def openMW():
	closeOverlay()
	global gameMode
	gameMode = "mw"
	openOverlay()


def openOverlay():
	global overlay
	global statText
	overlay = Toplevel()
	overlay.title('Overlay')
	overlay.geometry(str(windowWidth) + "x" + str(windowHeight))
	overlay.wm_attributes("-topmost", 1)
	overlay.wm_attributes('-transparentcolor', overlay['bg'])
	overlay.overrideredirect(1)

	
	#shitty click and drag function
	def move(event):
	    x, y = overlay.winfo_pointerxy()
	    overlay.geometry(f"+{x-275}+{y-100}")
	overlay.bind('<B1-Motion>',move)

	my_frame = Frame(overlay, width=550, height=370)
	my_frame.pack()
	statText = Label(my_frame, font=(textFont, textSize), fg=textColor)
	statText.pack()
	#textbox = Text(overlay, height=1, width=25).pack()
	data = requests.get(url).json()
	if gameMode == "bw":
		openOverlay.bwStartFinals = int(data['player']['stats']['Bedwars'].get('final_kills_bedwars', 0))
		openOverlay.bwStartWins = int(data['player']['stats']['Bedwars'].get('wins_bedwars', 0))
		refreshBW()
	elif gameMode == "skywars":
		openOverlay.skywarsStartKills = int(data['player']['stats']['SkyWars'].get('kills', 0))
		openOverlay.skywarsStartWins = int(data['player']['stats']['SkyWars'].get('wins', 0))
		refreshSkywars()
	elif gameMode == "bridge":
		openOverlay.bridgeStartWins = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_duel_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_doubles_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_four_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_2v2v2v2_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_3v3v3v3_wins"]),
        ] )
		openOverlay.bridgeStartLosses = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_duel_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_doubles_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_four_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_2v2v2v2_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "bridge_3v3v3v3_losses"]),
     ] )
		refreshBridge()	
	elif gameMode == "uhc":
		openOverlay.uhcStartWins = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "uhc_duel_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "uhc_doubles_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "uhc_four_wins"]),
    ] )
		openOverlay.uhcStartLosses = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "uhc_duel_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "uhc_doubles_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "uhc_four_losses"]),
    ] )
		refreshUHC()
	elif gameMode == "op":
		openOverlay.opStartWins = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "op_duel_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "op_doubles_wins"]),
    ] )
		openOverlay.opStartLosses = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "op_duel_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "op_doubles_losses"]),
    ] )
		refreshOP()
	elif gameMode == "classic":
		openOverlay.classicStartWins = data["player"]["stats"]["Duels"].get("classic_duel_wins", 0)
		openOverlay.classicStartLosses = data["player"]["stats"]["Duels"].get("classic_duel_losses", 0)
		refreshClassic()
	elif gameMode == "sw":
		openOverlay.swStartWins = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "sw_duel_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "sw_doubles_wins"]),
    ] )
		openOverlay.swStartLosses = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "sw_duel_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "sw_doubles_losses"]),
    ] )
		refreshSW()
	elif gameMode == "sumo":
		openOverlay.sumoStartWins = data["player"]["stats"]["Duels"].get("sumo_duel_wins", 0)
		openOverlay.sumoStartLosses = data["player"]["stats"]["Duels"].get("sumo_duel_losses", 0)
		refreshSumo()
	elif gameMode == "bow":
		openOverlay.bowStartWins = data["player"]["stats"]["Duels"].get("bow_duel_wins", 0)
		openOverlay.bowStartLosses = data["player"]["stats"]["Duels"].get("bow_duel_losses", 0)
		refreshBow()
	elif gameMode == "tnt":
		openOverlay.tntStartWins = data["player"]["stats"]["Duels"].get("bowspleef_duel_wins", 0)
		openOverlay.tntStartLosses = data["player"]["stats"]["Duels"].get("bowspleef_duel_losses", 0)
		refreshTNT()
	elif gameMode == "potion":
		openOverlay.potionStartWins = data["player"]["stats"]["Duels"].get("no_debuff_duel_wins", 0)
		openOverlay.potionStartLosses = data["player"]["stats"]["Duels"].get("no_debuff_duel_losses", 0)
		refreshPotion()
	elif gameMode == "combo":
		openOverlay.comboStartWins = data["player"]["stats"]["Duels"].get("combo_duel_wins", 0)
		openOverlay.comboStartLosses = data["player"]["stats"]["Duels"].get("combo_duel_losses", 0)
		refreshCombo()
	elif gameMode == "blitz":
		openOverlay.blitzStartWins = data["player"]["stats"]["Duels"].get("blitz_duel_wins", 0)
		openOverlay.blitzStartLosses = data["player"]["stats"]["Duels"].get("blitz_duel_losses", 0)
		refreshBlitz()
	elif gameMode == "mw":
		openOverlay.mwStartWins = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "mw_duel_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "mw_doubles_wins"]),
    ] )
		openOverlay.mwStartLosses = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "mw_duel_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "mw_doubles_losses"]),
    ] )
		refreshMW()
	else:
		print("invalid mode")
		openOverlay()



def closeOverlay():
	try:
		overlay.destroy()
	except NameError:
		pass


def getValueFromPath(dict, path):
    for el in path:
        if(el == path[-1]):
            return int(dict.get(el, 0))
        else:
            dict = dict.get(el, {})
    return 0


def refreshBW():
	data = requests.get(url).json()
	bwWins = int(data['player']['stats']['Bedwars'].get('wins_bedwars', 0))
	bwLosses = int(data['player']['stats']['Bedwars'].get('losses_bedwars', 0))
	bwFinals = int(data['player']['stats']['Bedwars'].get('final_kills_bedwars', 0))
	bwFinalDeaths = int(data['player']['stats']['Bedwars'].get('final_deaths_bedwars', 0))
	bwSessionFinals = bwFinals - openOverlay.bwStartFinals
	bwSessionWins = bwWins - openOverlay.bwStartWins
	try:
		bedwarsFkdr = round(bwFinals / bwFinalDeaths, 2)
	except ZeroDivisionError:
		bedwarsFkdr = "INF"
	statText.config(text=("BW Wins: " + str(bwWins) + "\nBW Losses: " + str(bwLosses) + "\nFinal Kills: " + str(bwFinals) + "\nFinal Deaths: " + str(bwFinalDeaths) + "\nFKDR: ") + str(bedwarsFkdr) + "\nSession Finals: " + str(bwSessionFinals) + "\nSession Wins: " + str(bwSessionWins))
	statText.pack()
	overlay.after(refreshTime, refreshBW)

def refreshSkywars():
	data = requests.get(url).json()
	skywarsWins = int(data['player']['stats']['SkyWars'].get('wins', 0))
	skywarsLosses = int(data['player']['stats']['SkyWars'].get('losses', 0))
	skywarsKills = int(data['player']['stats']['SkyWars'].get('kills', 0))
	skywarsDeaths = int(data['player']['stats']['SkyWars'].get('deaths', 0))
	skywarsSessionKills = skywarsKills - openOverlay.skywarsStartKills
	skywarsSessionWins = skywarsWins - openOverlay.skywarsStartWins
	try:
		skywarsKDR = round(skywarsKills / skywarsDeaths, 2)
	except ZeroDivisionError:
		skywarsKDR = "INF"
	statText.config(text=("SW Wins: " + str(skywarsWins) + "\nSW Losses: " + str(skywarsLosses) + "\nKills: " + str(skywarsKills) + "\nDeaths: " + str(skywarsDeaths) + "\nKDR: " + str(skywarsKDR) + "\n Session Kills: " + str(skywarsSessionKills) + "\n Session Wins: " + str(skywarsSessionWins)))
	statText.pack()
	overlay.after(refreshTime, refreshSkywars)

def refreshBridge():
	data = requests.get(url).json()
	bridgeWins = sum( [
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_duel_wins"]),
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_doubles_wins"]),
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_four_wins"]),
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_2v2v2v2_wins"]),
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_3v3v3v3_wins"]),
        ] )
	bridgeLosses = sum( [
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_duel_losses"]),
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_doubles_losses"]),
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_four_losses"]),
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_2v2v2v2_losses"]),
		getValueFromPath(data, ["player", "stats", "Duels", "bridge_3v3v3v3_losses"]),
     ] )
	bridgeSessionWins = bridgeWins - openOverlay.bridgeStartWins
	bridgeSessionLosses = bridgeLosses - openOverlay.bridgeStartLosses
	try:
		bridgeWLR = round(bridgeWins / bridgeLosses, 2)
	except ZeroDivisionError:
		bridgeWLR = "INF"
	try:
		bridgeSessionWLR = round(bridgeSessionWins / bridgeSessionLosses, 2)
	except ZeroDivisionError:
		bridgeSessionWLR = "INF"

	statText.config(text=("Bridge Wins: " + str(bridgeWins) + "\nBridge Losses: " + str(bridgeLosses) + "\nBridge WLR: " + str(bridgeWLR) + "\nSession W: " + str(bridgeSessionWins) + "\nSession L: " + str(bridgeSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshBridge)

def refreshUHC():
	data = requests.get(url).json()
	uhcWins = sum( [
		getValueFromPath(data, ["player", "stats", "Duels", "uhc_duel_wins"]),
		getValueFromPath(data, ["player", "stats", "Duels", "uhc_doubles_wins"]),
		getValueFromPath(data, ["player", "stats", "Duels", "uhc_four_wins"]),
    ] )
	uhcLosses = sum( [
		getValueFromPath(data, ["player", "stats", "Duels", "uhc_duel_losses"]),
		getValueFromPath(data, ["player", "stats", "Duels", "uhc_doubles_losses"]),
		getValueFromPath(data, ["player", "stats", "Duels", "uhc_four_losses"]),
    ] )
	uhcSessionWins = uhcWins - openOverlay.uhcStartWins
	uhcSessionLosses = uhcLosses - openOverlay.uhcStartLosses
	try:
		uhcWLR = round(uhcWins / uhcLosses, 2)
	except ZeroDivisionError:
		uhcWLR = "INF"
	statText.config(text=("UHC Wins: " + str(uhcWins) + "\nUHC Losses: " + str(uhcLosses) + "\nUHC WLR: " + str(uhcWLR) + "\nSession W: " + str(uhcSessionWins) + "\nSession L: " + str(uhcSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshUHC)

def refreshOP():
	data = requests.get(url).json()
	opWins = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "op_duel_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "op_doubles_wins"]),
    ] )
	opLosses = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "op_duel_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "op_doubles_losses"]),
    ] )
	opSessionWins = opWins - openOverlay.opStartWins
	opSessionLosses = opLosses - openOverlay.opStartLosses
	try:
		opWLR = round(opWins / opLosses, 2)
	except ZeroDivisionError:
		opWLR = "INF"
	statText.config(text=("OP Wins: " + str(opWins) + "\nOP Losses: " + str(opLosses) + "\nOP WLR: " + str(opWLR) + "\nSession W: " + str(opSessionWins) + "\nSession L: " + str(opSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshOP)

def refreshClassic():
	data = requests.get(url).json()
	classicWins = data["player"]["stats"]["Duels"].get("classic_duel_wins", 0)
	classicLosses = data["player"]["stats"]["Duels"].get("classic_duel_losses", 0)
	classicSessionWins = classicWins - openOverlay.classicStartWins
	classicSessionLosses = classicLosses - openOverlay.classicStartLosses
	try:
		classicWLR = round(classicWins / classicLosses, 2)
	except ZeroDivisionError:
		classicWLR = "INF"
	statText.config(text=("Classic Wins: " + str(classicWins) + "\nClassic Losses: " + str(classicLosses) + "\nClassic WLR: " + str(classicWLR) + "\nSession W: " + str(classicSessionWins) + "\nSession L: " + str(classicSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshClassic)

def refreshSW():
	data = requests.get(url).json()
	swWins = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "sw_duel_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "sw_doubles_wins"]),
    ] )
	swLosses = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "sw_duel_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "sw_doubles_losses"]),
    ] )
	swSessionWins = swWins - openOverlay.swStartWins
	swSessionLosses = swLosses - openOverlay.swStartLosses
	try:
		swWLR = round(swWins / swLosses, 2)
	except ZeroDivisionError:
		swWLR = "INF"
	statText.config(text=("SW Wins: " + str(swWins) + "\nSW Losses: " + str(swLosses) + "\nSW WLR: " + str(swWLR) + "\nSession W: " + str(swSessionWins) + "\nSession L: " + str(swSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshSW)

def refreshSumo():
	data = requests.get(url).json()
	sumoWins = data["player"]["stats"]["Duels"].get("sumo_duel_wins", 0)
	sumoLosses = data["player"]["stats"]["Duels"].get("sumo_duel_losses", 0)
	sumoSessionWins = sumoWins - openOverlay.sumoStartWins
	sumoSessionLosses = sumoLosses - openOverlay.sumoStartLosses
	try:
		sumoWLR = round(sumoWins / sumoLosses, 2)
	except ZeroDivisionError:
		sumoWLR = "INF"
	statText.config(text=("Sumo Wins: " + str(sumoWins) + "\nSumo Losses: " + str(sumoLosses) + "\nSumo WLR: " + str(sumoWLR) + "\nSession W: " + str(sumoSessionWins) + "\nSession L: " + str(sumoSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshSumo)

def refreshBow():
	data = requests.get(url).json()
	bowWins = data["player"]["stats"]["Duels"].get("bow_duel_wins", 0)
	bowLosses = data["player"]["stats"]["Duels"].get("bow_duel_losses", 0)
	bowSessionWins = bowWins - openOverlay.bowStartWins
	bowSessionLosses = bowLosses - openOverlay.bowStartLosses
	try:
		bowWLR = round(bowWins / bowLosses, 2)
	except ZeroDivisionError:
		bowWLR = "INF"
	statText.config(text=("Bow Wins: " + str(bowWins) + "\nBow Losses: " + str(bowLosses) + "\nBow WLR: " + str(bowWLR) + "\nSession W: " + str(bowSessionWins) + "\nSession L: " + str(bowSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshBow)

def refreshTNT():
	data = requests.get(url).json()
	tntWins = data["player"]["stats"]["Duels"].get("bowspleef_duel_wins", 0)
	tntLosses = data["player"]["stats"]["Duels"].get("bowspleef_duel_losses", 0)
	tntSessionWins = tntWins - openOverlay.tntStartWins
	tntSessionLosses = tntLosses - openOverlay.tntStartLosses
	try:
		tntWLR = round(tntWins / tntLosses, 2)
	except ZeroDivisionError:
		tntWLR = "INF"
	statText.config(text=("TNT Wins: " + str(tntWins) + "\nTNT Losses: " + str(tntLosses) + "\nTNT WLR: " + str(tntWLR) + "\nSession W: " + str(tntSessionWins) + "\nSession L: " + str(tntSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshTNT)

def refreshPotion():
	data = requests.get(url).json()
	potionWins = data["player"]["stats"]["Duels"].get("no_debuff_duel_wins", 0)
	potionLosses = data["player"]["stats"]["Duels"].get("no_debuff_duel_losses", 0)
	potionSessionWins = potionWins - openOverlay.potionStartWins
	potionSessionLosses = potionLosses - openOverlay.potionStartLosses
	try:
		potionWLR = round(potionWins / potionLosses, 2)
	except ZeroDivisionError:
		potionWLR = "INF"
	statText.config(text=("Potion Wins: " + str(potionWins) + "\nPotion Losses: " + str(potionLosses) + "\nPotion WLR: " + str(potionWLR) + "\nSession W: " + str(potionSessionWins) + "\nSession L: " + str(potionSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshPotion)

def refreshCombo():
	data = requests.get(url).json()
	comboWins = data["player"]["stats"]["Duels"].get("combo_duel_wins", 0)
	comboLosses = data["player"]["stats"]["Duels"].get("combo_duel_losses", 0)
	comboSessionWins = comboWins - openOverlay.comboStartWins
	comboSessionLosses = comboLosses - openOverlay.comboStartLosses
	try:
		comboWLR = round(comboWins / comboLosses, 2)
	except ZeroDivisionError:
		comboWLR = "INF"
	statText.config(text=("Combo Wins: " + str(comboWins) + "\nCombo Losses: " + str(comboLosses) + "\nCombo WLR: " + str(comboWLR) + "\nSession W: " + str(comboSessionWins) + "\nSession L: " + str(comboSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshCombo)

def refreshBlitz():
	data = requests.get(url).json()
	blitzWins = data["player"]["stats"]["Duels"].get("blitz_duel_wins", 0)
	blitzLosses = data["player"]["stats"]["Duels"].get("blitz_duel_losses", 0)
	blitzSessionWins = blitzWins - openOverlay.blitzStartWins
	blitzSessionLosses = blitzLosses - openOverlay.blitzStartLosses
	try:
		blitzWLR = round(blitzWins / blitzLosses, 2)
	except ZeroDivisionError:
		blitzWLR = "INF"
	statText.config(text=("Blitz Wins: " + str(blitzWins) + "\nBlitz Losses: " + str(blitzLosses) + "\nBlitz WLR: " + str(blitzWLR) + "\nSession W: " + str(blitzSessionWins) + "\nSession L: " + str(blitzSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshBlitz)

def refreshMW():
	data = requests.get(url).json()
	mwWins = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "mw_duel_wins"]),
        getValueFromPath(data, ["player", "stats", "Duels", "mw_doubles_wins"]),
    ] )
	mwLosses = sum( [
        getValueFromPath(data, ["player", "stats", "Duels", "mw_duel_losses"]),
        getValueFromPath(data, ["player", "stats", "Duels", "mw_doubles_losses"]),
    ] )
	mwSessionWins = mwWins - openOverlay.mwStartWins
	mwSessionLosses = mwLosses - openOverlay.mwStartLosses
	try:
		mwWLR = round(mwWins / mwLosses, 2)
	except ZeroDivisionError:
		mwWLR = "INF"
	statText.config(text=("MW Wins: " + str(mwWins) + "\nMW Losses: " + str(mwLosses) + "\nMW WLR: " + str(mwWLR) + "\nSession W: " + str(mwSessionWins) + "\nSession L: " + str(mwSessionLosses)))
	statText.pack()
	overlay.after(refreshTime, refreshMW)


settings = Tk()
settings.title('Settings')
settings.geometry("260x300")

bedwarsText = Label(settings, text="Bedwars", font=("Times", 15, "bold")).grid(row=0, column=0)
bedwarsButton = Button(settings, bg="white", height=1, width=2, command=openBW).grid(row=0, column=1)
spacer1 = Label(settings, text="     ", font=("Times", 20, "bold")).grid(row=0, column=2)
skywarsText = Label(settings, text="Skywars", font=("Times", 15, "bold")).grid(row=0, column=3)
skywarsButton = Button(settings, bg="white", height=1, width=2, command=openSkywars).grid(row=0, column=4)

linebreak = Label(settings, text="Duels", font=("Times", 15, "underline")).grid(row=1, column=2)

bridgeText = Label(settings, text="Bridge", font=("Times", 15, "bold")).grid(row=2, column=0)
bridgeButton = Button(settings, bg="white", height=1, width=2, command=openBridge).grid(row=2, column=1)
spacer2 = Label(settings, text="   |  ", font=("Times", 20, "bold")).grid(row=2, column=2)
uhcText = Label(settings, text="UHC", font=("Times", 15, "bold")).grid(row=2, column=3)
uhcButton = Button(settings, bg="white", height=1, width=2, command=openUHC).grid(row=2, column=4)

opText = Label(settings, text="OP", font=("Times", 15, "bold")).grid(row=3, column=0)
opButton = Button(settings, bg="white", height=1, width=2, command=openOP).grid(row=3, column=1)
spacer3 = Label(settings, text="   |  ", font=("Times", 20, "bold")).grid(row=3, column=2)
classicText = Label(settings, text="Classic", font=("Times", 15, "bold")).grid(row=3, column=3)
classicButton = Button(settings, bg="white", height=1, width=2, command=openClassic).grid(row=3, column=4)

swText = Label(settings, text="SW", font=("Times", 15, "bold")).grid(row=4, column=0)
swButton = Button(settings, bg="white", height=1, width=2, command=openSW).grid(row=4, column=1)
spacer4 = Label(settings, text="   |  ", font=("Times", 20, "bold")).grid(row=4, column=2)
sumoText = Label(settings, text="Sumo", font=("Times", 15, "bold")).grid(row=4, column=3)
sumoButton = Button(settings, bg="white", height=1, width=2, command=openSumo).grid(row=4, column=4)

bowText = Label(settings, text="Bow", font=("Times", 15, "bold")).grid(row=5, column=0)
bowButton = Button(settings, bg="white", height=1, width=2, command=openBow).grid(row=5, column=1)
spacer5 = Label(settings, text="   |  ", font=("Times", 20, "bold")).grid(row=5, column=2)
tntText = Label(settings, text="TNT", font=("Times", 15, "bold")).grid(row=5, column=3)
tntButton = Button(settings, bg="white", height=1, width=2, command=openTNT).grid(row=5, column=4)

potionText = Label(settings, text="Potion", font=("Times", 15, "bold")).grid(row=6, column=0)
potionButton = Button(settings, bg="white", height=1, width=2, command=openPotion).grid(row=6, column=1)
spacer6 = Label(settings, text="   |  ", font=("Times", 20, "bold")).grid(row=6, column=2)
comboText = Label(settings, text="Combo", font=("Times", 15, "bold")).grid(row=6, column=3)
comboButton = Button(settings, bg="white", height=1, width=2, command=openCombo).grid(row=6, column=4)

blitzText = Label(settings, text="Blitz", font=("Times", 15, "bold")).grid(row=7, column=0)
blitzButton = Button(settings, bg="white", height=1, width=2, command=openBlitz).grid(row=7, column=1)
spacer2 = Label(settings, text="   |  ", font=("Times", 20, "bold")).grid(row=7, column=2)
mwText = Label(settings, text="MW", font=("Times", 15, "bold")).grid(row=7, column=3)
mwButton = Button(settings, bg="white", height=1, width=2, command=openMW).grid(row=7, column=4)
mainloop()
