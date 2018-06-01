import sys
h=0
c=0
l=0
b=0
bossattack=10
import random
import time
global bossh
quality=0
bossh=250

global wboss
wboss=1
global p1_name
p1_name=0
global p2_name
p2_name=0
x=0
y=0
subclass1=0
subclass2=0
bandages=0
bandages2=0
p1weapon="Sword"
p2weapon="Sword"
global attack_damagelight1
attack_damagelight1=10
global attack_damagelight2
attack_damagelight2=10
global attack_damageheavy1
attack_damageheavy1=10
global attack_damageheavy2
attack_damageheavy2=10
global p1health
p1health=100
global p2health
p2health=100
global money1
money1=random.randint(5000,20000)
global money2
money2=random.randint(5000,20000)
money1=int(money1)
money2=int(money2)
#Variable Defining

from random import randint
from time import clock

##______________________________________________________________________________

State = type("State", (object,), {})

class LightOn(State):
    def Execute(self):
        global bossattack
        print ("Passive")
        time.sleep(0.1)
        print("The boss now does only 10 damage")
        bossattack=15
        
class LightOff(State):
    def Execute(self):
        global bossattack
        print ("Enraged")
        time.sleep(0.1)
        print("The boss now does 20 damage")
        bossattack=30
        
##______________________________________________________________________________

class Transition(object):
    def __init__(self, toState):
        self.toState = toState
        
    def Execute(self):
        print ("State is Changing Soon")
        
##______________________________________________________________________________

class SimpleFSM(object):
    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None
        
    def SetState(self, stateName):
        self.curState = self.states[stateName]
        
    def Transition(self, transName):
        self.trans = self.transitions[transName]
        
    def Execute(self):
        if(self.trans):
           self.trans.Execute()
           self.SetState(self.trans.toState)
           self.trans = None
        self.curState.Execute()
          
##______________________________________________________________________________


class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.LightOn = True

        






def bloodvilla():
  print("Welcome to the Village of Bloodmist!")
  print("You both arive at the village and find thieves robbing houses.")
  print
def purgatoryone():
  global p1health
  global p2health
  print("Nice Job!")
  print("You beat the Dungeon of the Watching Mountains.")
  print("Each player gets 20 Health!")
  p1health=p1health+20
  p2health=p2health+20
  print(p1_name)
  time.sleep(0.000000000001)
  print("Hp")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p1health)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p2_name)
  time.sleep(0.000000000001)
  print("Hp")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p2health)
  time.sleep(0.000000000001)
  print("Each player also gets 5 bandages!")
  bandages=bandages+5
  bandages2=bandages2+5
  print(p1_name)
  time.sleep(0.000000000001)
  print("Bandages")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(bandages)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p2_name)
  time.sleep(0.000000000001)
  print("Bandages")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(bandages2)
  time.sleep(0.000000000001)
  des1=input("Do you want to go to A.) the Village of the Bloodmist(Easy) or B.) the Lavapool(Hard)?")
  des1=str(des1)
  if des1=="A":
    print("hi")
def firstdungeon():
  print("You beat the first dungeon!")
  purgatoryone()
def lightcast2():
  global bossh
  print("You used your Lightning Cast spell!")
  print("It did 5 damage to the boss.")
  bossh=bossh-5
  dragonfight()
def maget2():
  global p1health
  global p2health
  print("You choose to heal your teammate.")
  print("Your teammate gained 5 health.")
  p1health=p1health+5
  dragonfight()
    
  
def mageself2():
  global p2health
  print("You Choose to heal yourself.")
  print("You gained 5 health.")
  p2health=p2health+5
  dragonfight()
def fightmechanicsmage2():
  print("Player 2")
  fightop1=input("What do you do? {Heal Yourself} {Lightning Cast} {Heal Teammate}")
  if fightop1=="Heal Yourself" or "heal yourself":
    mageself2()
  if fightop1=="Lightning Cast" or fightop1=="lightning cast":
    lightcast2()
  if fightop1=="Heal Teammate" or fightop1=="heal teammate":
    maget2()
def lightcast1():
  global bossh
  print("You used your Lightning Cast spell!")
  print("It did 5 damage to the boss.")
  bossh=bossh-5
  if subclass2=="Healer" or subclass2=="healer":
    fightmechanicsmage2()
  else:
    fightmechanics2()
def maget1():
  global p2health
  print("You choose to heal your teammate.")
  print("Your teammate gained 5 health.")
  p2health=p2health+5
  if subclass2=="Healer":
    fightmechanicsmage2()
  else:
    fightmechanics2()
def mageself1():
  global p1health
  print("You choose to heal yourself.")
  print("You gained 5 health")
  p1health=p1health+5
  fightmechanicsmage2()
def fightmechanicsmage1():
  print("Player 1")
  fightop1=input("What do you do? {Heal Yourself} {Lightning Cast} {Heal Teammate}")
  if fightop1=="Heal Yourself" or "heal yourself":
    mageself1()
  if fightop1=="Lightning Cast" or fightop1=="lightning cast":
    lightcast1()
  if fightop1=="Heal Teammate" or fightop1=="heal teammate":
    maget1()
    
def playerdodge2():
  global bossh
  global p2health
  print(p2_name)
  global bossattack
  if __name__ == "__main__":
    light = Char()
    
    light.FSM.states["On"] = LightOn()
    light.FSM.states["Off"] = LightOff()
    light.FSM.transitions["On"] = Transition("On")
    light.FSM.transitions["Off"] = Transition("Off")
    
    light.FSM.SetState("On")
    a=random.randint(1,4)
    for i in range(a):
        startTime = clock()
        timeInterval = 1

        if (randint(0, 2)):
            if (light.LightOn):
                light.FSM.Transition("Off")
                light.LightOn = False
            else:
                light.FSM.Transition("On")
                light.LightOn = True
            light.FSM.Execute()
            
  print("The boss is attacking you!")
  dodgep1=input("Dodge left or right?")
  dodgep1=random.randint(1,10)
  if dodgep1>=9:
    print("You took no damage.")
    if subclass1=="Healer" or subclass1=="healer":
      fightmechanicsmage1()
    else:
      fightmechanics1()
  if dodgep1<=8:
    print("You took damage.")
    p2health=p2health-bossattack
    bossh=bossh+bossattack
    print("Health ")
    print(p2health)
    if subclass1=="Healer" or subclass1=="healer":
      fightmechanicsmage1()
    else:
      fightmechanics1()
    
def playerdodge1():
  global bossh
  global p1health
  print(p1_name)
  global bossattack
  if __name__ == "__main__":
    light = Char()
    
    light.FSM.states["On"] = LightOn()
    light.FSM.states["Off"] = LightOff()
    light.FSM.transitions["On"] = Transition("On")
    light.FSM.transitions["Off"] = Transition("Off")
    
    light.FSM.SetState("On")
    a=random.randint(1,4)
    for i in range(a):
        startTime = clock()
        timeInterval = 1

        if (randint(0, 2)):
            if (light.LightOn):
                light.FSM.Transition("Off")
                light.LightOn = False
            else:
                light.FSM.Transition("On")
                light.LightOn = True
            light.FSM.Execute()
            
  print("The boss is attacking you!")
  dodgep1=input("Dodge left or right")
  dodgep1=random.randint(1,10)
  if dodgep1>=9:
    print("You took no damage")
    if subclass1=="Healer" or subclass1=="healer":
      fightmechanicsmage1()
    else:
      fightmechanics1()
  if dodgep1<=8:
    print("You took damage.")
    p1health=p1health-bossattack
    bossh=bossh+bossattack
    print("Health ")
    print(p1health)
    if subclass1=="Healer" or subclass1=="healer":
      fightmechanicsmage1()
    else:
      fightmechanics1()

def dragonfight():
  global wboss
  if p1health==0:
    print("You Lost!")
  if p2health==0:
    print("You Lost!")
  if bossh<=1 and wboss==1:
      archerafter()
  if bossh<=1 and wboss==2:
      afterfight2()
  if bossh<=1 and wboss==3:
      almosts()
  if bossh<=1 and wboss==4:
      firstdungeon()
  print("The enemy launches its attack.")
  playerhit=random.randint(1,2)
  if playerhit==1:
    playerdodge1()
  if playerhit==2:
    playerdodge2()

def hidenheal2():
  global bossh
  global p1health
  print("You decided to hide and heal.")
  if bandages2==0:
    print("You don't have any bandages left, its the boss's turn.")
    dragonfight()
  else:
    print("You recover 5 health.")
    p2health=p2health+5
    print("Health "+p2health)
    dragonfight()
#Heal For player 2
def heavya2():
  global bossh
  global wboss
  global p2health
  print("You decide to do a heavy attack.")
  rheavy2=random.randint(1,10)
  if rheavy2>=7.5:
    print("You missed your heavy attack, you were out in the open so you took 5 damage.")
    p2health=p2health-5
    print("Player 2 Health ")
    print(p2health)
    dragonfight()
  else:
    print("Your heavy attack was successful!")
    bossh=bossh-attack_damageheavy2
    if bossh<=1 and wboss==1:
      archerafter()
    if bossh<=1 and wboss==2:
      afterfight2()
    if bossh<=1 and wboss==3:
      almosts()
    if bossh<=1 and wboss==4:
      firstdungeon()
    print("Boss Health,")
    print(bossh)
    if bossh<=1:
      print("You defeated the boss.")
    dragonfight()
def lighta2():
  global wboss
  global bossh
  global p2health
  print("You decide to do a light attack.")
  rlight2=random.randint(1,10)
  if rlight2>=9.5:
    print("You missed your light attack, you were out in the open so you took 5 damage.")
    p2health=p2health-5
    print("Player 2 Health ")
    print(p2health)
    dragonfight()
  else:
    print("Your light attack was sucessful!")
    bossh=bossh-attack_damagelight2
    print("Boss Health ")
    print(bossh)
    dragonfight()
    if bossh<=1 and wboss==1:
      archerafter()
    if bossh<=1 and wboss==2:
      afterfight2()
    if bossh<=1 and wboss==3:
      almosts()
    if bossh<=1 and wboss==4:
      firstdungeon()
    if bossh<=1 and wboss==5:
      print("You win!")

def fightmechanics2():
  global p1health
  global p2health
  
  print("Player 2")
  if p1health<=0 or p2health<=0:
    print("Game over.....")
    print("Stop the Game and run again to play more")
    time.sleep(90000000000000000000000)
  fightop1=input("What do you do? {Hide and bandage} {Light Attack} {Heavy Attack}")
  if fightop1=="Hide and Bandage" or fightop1=="hide and bandage":
    hidenheal2()
  if fightop1=="Light Attack" or fightop1=="light attack" or fightop1=="lightattack" or fightop1=="lith attack" or fightop1=="light atack":
    lighta2()
  if fightop1=="Heavy Attack" or fightop1=="heavy attack" or fightop1=="heavyattack" or fightop1=="hevy attack" or fightop1=="heavy atack":
    heavya2()


def hidenheal1():
  global subclass1
  global subclass2
  global bossh
  global p1health
  print("You decided to hide and heal.")
  time.sleep(0.000000000001)
  if bandages==0:
    print("You don't have any bandages left, it's your partners turn.")
    if subclass2=="Healer" or subclass2=="healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
  else:
    print("You recover 5 health.")
    p1health=p1health+5
    print("Health "+p1health )
    if subclass2=="Healer" or subclass2=="healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
#heal for First Player
def heavya1():
  global wboss
  global subclass1
  global subclass2
  global bossh
  global p1health
  print("You decide to do a heavy attack.")
  time.sleep(0.000000000001)
  rheavy1=random.randint(1,10)
  if rheavy1>=7.5:
    print("You missed your heavy attack, you were out in the open so you took 5 damage.")
    p1health=p1health-5
    print("Player 1 Health")
    print(p1health)
    if subclass2=="Healer" or subclass2=="healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
  else:
    print("Your heavy attack was sucessful!")
    time.sleep(0.000000000001)
    bossh=bossh-attack_damageheavy1
    if bossh<=1 and wboss==1:
      archerafter()
    if bossh<=1 and wboss==2:
      afterfight2()
    if bossh<=1 and wboss==3:
      almosts()
    if bossh<=1 and wboss==4:
      print("Boss Health,")
      print(bossh)
    if subclass2=="Healer" or subclass2=="healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
      
def lighta1():
  global subclass1
  global subclass2
  global p1health
  global wboss
  time.sleep(0.000000000001)
  print("You decide to do a light attack.")
  rlight1=random.randint(1,10)
  if rlight1>=9.5:
    time.sleep(0.000000000001)
    print("You missed your light attack, you were out in the open so you took 5 damage.")
    p1health=p1health-5
    print("Player 1 Health")
    print(p1health)
    if subclass2=="Healer" or subclass2=="healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
  else:
    time.sleep(0.000000000001)
    global bossh
    print("Your light attack was successful!")
    bossh=bossh-attack_damagelight1
    print("Boss Health,")
    print(bossh)
    if subclass2=="Healer" or subclass2=="healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
    if bossh<=1 and wboss==1:
      archerafter()
    if bossh<=1 and wboss==2:
      afterfight2()
    if bossh<=1 and wboss==3:
      almosts()
    if bossh<=1 and wboss==4:
      firstdungeon()
def fightmechanics1():
  global p1health
  global p2health
  print("Player 1")
  if p1health<=0 or p2health<=0:
    print("Game over.....")
    print("Stop the Game and run again to play more")
    time.sleep(90000000000000000000000)
  fightop1=input("What do you do? {Hide and bandage} [Light Attack} {Heavy Attack}")
  if fightop1=="Hide and Bandage" or fightop1=="hide and bandage":
    hidenheal1()
  if fightop1=="Light Attack" or fightop1=="light attack" or fightop1=="lightattack" or fightop1=="lith attack" or fightop1=="light atack":
    lighta1()
  if fightop1=="Heavy Attack" or fightop1=="heavy attack" or fightop1=="heavyattack" or fightop1=="hevy attack" or fightop1=="heavy atack":
    heavya1()
  
def dungeon1left():
  global subclass1
  global subclass2
  print("You walk for about five minutes and find that the dungeon opens up.")
  time.sleep(1)
  print("You see a dragon with a wooden chest behind him.")
  time.sleep(1)
  print("The dragon turns and looks at you..... get ready for a fight.")
  time.sleep(1)
  if subclass1=="Healer" or subclass1=="healer":
      fightmechanicsmage1()
  else:
      fightmechanics1()
def dungeon1right():
  print("You walk to the end of the right side......You seem to be going in a loop and find yourself back at the start.")
  dungeonstart1()
def dungeonstart1():
  print("You come across the entrance and you have a decision,")
  side=input("Left or Right")
  side=str(side)
  if side=="Left":
    dungeon1left()
    
  if side=="Right":
    dungeon1right()
  
def adstart():
  print("Your adventure begins in your first dungeon")
  dungeonstart1()

def moneyadd1():
  global x
  global money1
  money1=money1+x
  x=0
  print(money1)
#This is The Money Function to add money player 1.

def moneysub1():
  money1=money1-y
  y=0
  print(money1)
#This is the function to Subtract Money player 1.

def moneyadd2():
  global x
  global money2
  money2=money2+x
  x=0
  print(money2)
#This is The Money Function to add money player 2.

def moneysub2():
  global y
  money2=money2-y
  y=0
  print(money2)
#This is the function to Subtract Money player 2.

#Start of Game
def startgame():
  global subclass1
  global subclass2
  import random
  import time
  global bossh
  global wboss
  wboss=1
  bossh=250
  global p1_name
  p1_name=0
  global p2_name
  p2_name=0
  x=0
  y=0
  bandages=0
  bandages2=0
  p1weapon="Sword"
  p2weapon="Sword"
  global attack_damagelight1
  attack_damagelight1=10
  global attack_damagelight2
  attack_damagelight2=10
  global attack_damageheavy1
  attack_damageheavy1=10
  global attack_damageheavy2
  attack_damageheavy2=10
  global p1health
  p1health=100
  global p2health
  p2health=100
  global money1
  money1=random.randint(5000,20000)
  global money2
  money2=random.randint(5000,20000)
  money1=int(money1)
  money2=int(money2)
#Variable Defining
  print("Welcome to the world of Oropos! This is our two person co-operative game.")
  time.sleep(0.000000000001)
  print("The object of this game is go through the adventure and stay alive. On the way, you can earn loads of gold to help you.")
  time.sleep(0.000000000001)
  print("Let's start.")
  time.sleep(0.000000000001)
  p1_name=input("What is your name?")
  p1_name=str(p1_name)
  time.sleep(0.000000000001)
  print("Hello and welcome, "+ p1_name)
  time.sleep(0.000000000001)
  print("")
  p2_name=input("What is your name Player 2?")
  p2_name=str(p2_name)
  time.sleep(0.000000000001)
  print("Hello and welcome, "+ p2_name)
  time.sleep(0.000000000001)
  print("")
  print("You have a big decision ahead of you "+p1_name)
  time.sleep(0.000000000001)
  print("A Mage. A long range, squishy, magic attacker with decent damage.")
  time.sleep(0.000000000001)
  print("A Healer. A medic at the back who helps injured comrades survive to fight another battle.")
  time.sleep(0.000000000001)
  print("A Rogue. A full attacker with huge damage, but with extremely low health.")
  time.sleep(0.000000000001)
  print("Or a Knight. A decently healthed, all around average fighter.  ")
  subclass1=input("What class will you be?")
  time.sleep(0.000000000001)
  subclass1=str(subclass1)
  if subclass1=="Mage" or subclass1=="mage":
    attack_damagelight1=30
    attack_damageheavy1=60
    p1health=55
  if subclass1=="Healer" or subclass1=="healer":
    attack_damagelight1=5
    attack_damageheavy1=10
    p1health=150
  if subclass1=="Rogue" or subclass1=="rogue":
    attack_damagelight1=45
    attack_damageheavy1=90
    p1health=40
  if subclass1=="Knight" or subclass1=="knight":
    attack_damagelight1=20
    attack_damageheavy1=40
    p1health=80
  time.sleep(0.000000000001)
  print("Great You are a "+ subclass1+" "+ p1_name)
  print("")
  print("")
  print("You have a big choice ahead of you "+p2_name)
  subclass2=input("What class will you be? Mage, Healer, Rogue, or Knight?")
  subclass2=str(subclass2)
  if subclass2=="Mage" or subclass1=="mage" :
    attack_damagelight2=30
    attack_damageheavy2=60
    p2health=55
  if subclass2=="Healer" or subclass2=="healer":
    attack_damagelight2=5
    attack_damageheavy2=10
    p2health=150
  if subclass2=="Rogue" or subclass2=="rogue":
    attack_damagelight2=45
    attack_damageheavy2=90
    p2health=40
  if subclass2=="Knight" or subclass2=="knight":
    attack_damagelight2=20
    attack_damageheavy2=40
    p2health=80
    time.sleep(0.000000000001)
  print("Great You are a "+subclass2+" "+p2_name)
  time.sleep(0.000000000001)
  print("According to your class, it will determine your health and attack. Everything will be displayed below.")
  print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
  time.sleep(0.75)
  print("Health For Player 1")
  print(p1health)
  time.sleep(0.75)
  print("Health for Player 2")
  print(p2health)
  time.sleep(0.75)
  print("Player 1 Attack Damage")
  print(attack_damagelight1)
  time.sleep(0.75)
  print("Player 2 Attack Damage")
  print(attack_damagelight2)
  time.sleep(0.75)
  print("Now that you know all of your stats you will now begin your quest.")
  wakeup()
def wakeup():
  print("Gahhhhh, what was that dream...?")
  time.sleep(0.75)
  print("Ehh whatever.")
  time.sleep(0.75)
  print("Anyways, today's the big day!")
  time.sleep(0.75)
  print("I'm going to go to the Capital to get my first quest alongside my friend")
  time.sleep(0.75)
  print("I hear it's gonna be worth alot of gold. Woo whee!")
  time.sleep(0.75)
  print("Lets see what I should get...")
  time.sleep(0.75)
  print("Some money")
  time.sleep(0.75)
  print("And a map.")
  time.sleep(0.75)
  print("Here is a picture of the map :")
  time.sleep(0.000000000001)
  kingdom()
  print("Now it's time to meet")
  time.sleep(0.75)
  print("...")
  time.sleep(0.1)
  print("...")
  time.sleep(0.1)
  print("...") 
  time.sleep(0.1)
  print("Player 1 Meets Up With Player 2.")
  time.sleep(0.75)
  print("*They share info.*")
  time.sleep(0.75)
  print(money1)
  time.sleep(0.75)
  print(money2)
  time.sleep(0.75)
  print("You guys prepare to leave.")
  time.sleep(0.75)
  info=input("Would you like to learn more about the places you are going to?")
  if info=="Yes":
    learning()
  if info=="No":
    decision1()
def learning():
  print("Watching Mountains.")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("One of the mysterious places in the world of Oropos.")
  time.sleep(0.75)
  print("Known for it's weird, moving eye at the top of the highest peak.")
  time.sleep(0.75)
  print("Travelers who went exploring in these mountain always ends up battered up after leaving.")
  time.sleep(0.75)
  print("Noone knows why... as they won't tell.")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("Village of the Bloodmist.")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("One of the most dangerous places in the world.")
  time.sleep(0.000000000001)
  print("Rumors say this village trains their kids so hard, that they are forced into a killing competition between each other just to graduate.")
  time.sleep(0.000000000001)
  print("That's how they got the name Bloodmist...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("Village of the Edge.")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("The place known for the bravery of it's soldiers.")
  time.sleep(0.000000000001)
  print("They are willing to die for anything just to protect their honor.")
  time.sleep(0.000000000001)
  print("Rumors say they never lose stamina if it's for the protection of others.")
  decision1()
def decision1():
  decision=input("*Do you want to A.) go to the Watching Mountains (Easy difficulty) , B.) go to the Village of the Bloodmist (Normal Difficulty) or C.) go to the Village of the Edge (Hard Difficulty)?*")
  if decision=="A" or decision=="a":
    print("Alright, let's go to the Watching Mountain first!")
    dungeon_mountains()
  if decision=="B" or decision=="b":
    print("Alright, let's go to the Village of the Bloodmist first!")
    bloodmist()
  if decision=="C" or decision=="c":
    print("Alright, let's go to the Village of the Edge first!")
    
def kingdom():  
  print("|___________________________________________________________________________________________________________________________________________________________________________________________________________________________________|")
  time.sleep(0.2)
  print("|               /                                                                                                                         |           |                                                                       |     |")
  time.sleep(0.2)
  print("|              /                                                                                                                          |           |                                  ___                                  |     |")
  time.sleep(0.2)
  print("|             /                                                                                                                           |           |                                 /   \                                 |     |")
  time.sleep(0.2)
  print("|            /                                                                                                                            |           |                                /     \                                |     |")
  time.sleep(0.2)
  print("|           /                                                                                                                             |           |                /\             /       \             /\                |     |")
  time.sleep(0.2)
  print("|          /                                                                                                                              |           |               /  \           /         \           /  \               |     |")
  time.sleep(0.2)
  print("|         /                                                                                                                               |           |              /    \         /           \         /    \              |     |")
  time.sleep(0.2)
  print("|        /                                                                                                                                |           |             /      \       /             \       /      \             |     |")
  time.sleep(0.2)
  print("|       /                                                                                                                                 |           |            /        \_____/               \_____/        \            |     |")
  time.sleep(0.2)
  print("|      /                                                                                    ________________                              |           |            |                                             |            |     |")
  time.sleep(0.2)
  print("|     /     /|\                                                                            (       /        )                             |           |            |                                             |            |     |")
  time.sleep(0.2)
  print("|    /       |                                                                            (        /         )                            |           |            |                                             |            |     |")
  time.sleep(0.2)
  print("|   /        |                                                                             (        \       )                             |           |            |       Corrupt Kingdom of Knowltrolls        |            |     |")
  time.sleep(0.2)
  print("|  /         |                                                                              (_______\______)                              |           |            |                                             |            |     |")
  time.sleep(0.2)
  print("|_/    Dungeon of the Lavapool                                                                                                            |           |            |                                             |            |     |")
  time.sleep(0.2)
  print("|                                                                                                  /|\                                    |           |            |                                             |            |     |")
  time.sleep(0.2)
  print("|                                                                                                   |                                     |           |            |_____________________________________________|            |     |")
  time.sleep(0.2)
  print("|                                                                                                   |                                     |           |                                                                       |     |")
  time.sleep(0.2)
  print("|                                                                                     Dungeon of the Lightning Cloud                      |           |                                                                       |     |")
  time.sleep(0.2)
  print("|                                                                                                                                         |           |_______________________________________________________________________|     |")
  time.sleep(0.2)
  print("|                                                                                                                                         |                                                                                         |")
  time.sleep(0.2)
  print("|                                                                                                                                         |                                                                                         |")
  time.sleep(0.2)
  print("|                                                                                                                                         |                                         Wall Of Maria                                   |")
  time.sleep(0.2)
  print("|                                                                                                                                         |                                                                                         |")
  time.sleep(0.2)
  print("|                                                                                                                                         |                                                                                         |")
  time.sleep(0.2)
  print("|                                                                                                                                         |_________________________________________________________________________________________|")
  time.sleep(0.2)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.2)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.2)
  print("|                                                                                                                                                                                 Wall Of St. Lewis                                 |")
  time.sleep(0.2)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.2)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.2)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.2)
  print("|    Dungeon of the  Watching Mountains                                                                                                                                                                                             |")
  time.sleep(0.2)
  print("|               |                                                                                                                                                                                                                   |")
  time.sleep(0.2)
  print("|               |                                                                                                                                                                                                                   |")
  time.sleep(0.2)
  print("|               |                             /\                                                                                                                                                         Dungeon of Bloodshed Lake  |")
  time.sleep(0.2)
  print("|               |                            /  \                                                                                                                                                                  |                |")
  time.sleep(0.2)
  print("|              \|/                          /    \                                                                                                                                                                 |                |")
  time.sleep(0.2)
  print("|                    /\                    /      \                                                                                                                                                                |                |")
  time.sleep(0.2)
  print("|                   /  \                  /        \                                                                                                                                                               |                |")
  time.sleep(0.2)
  print("|                  /    \                /   ( | )  \                                                                                                                                                              |                |")
  time.sleep(0.2)
  print("|               /\/      \              /            \                                                                                                                                                            \|/               |")
  time.sleep(0.2)
  print("|              /  \       \     /\     /              \                      Village of the Bloodmist                                                                                                            ____________-___-_-|")
  time.sleep(0.2)
  print("|             /    \  /\   \   /  \   /                \                              |                                                          Sister Village of the Bloodmist                                |                   |")
  time.sleep(0.2)
  print("|           /\      \/  \   \ /    \ /                  \                             |                                                                      |                                                 /                    |")
  time.sleep(0.2)
  print("|          /  \     /    \   /      /                    \                            |                                                                      |                                                |                     |")
  time.sleep(0.2)
  print("|         /    \   /      \ /      /                      \                           |                                                                      |                                             -_|                      |")
  time.sleep(0.2)
  print("|        /      \ /        \      /                        \                         \|/                                                                    \|/                                           /          (------)       |")
  time.sleep(0.2)
  print("|       /        \          \    /                          \                  ______    ______    ______                                                 ______                                         |          (----|----)     |")
  time.sleep(0.2)
  print("|      /          \          \  /                            \                /      \  /      \  /      \                                               /      \                                       /            (------)       |")
  time.sleep(0.2)
  print("|                             \/                                              |      |  |      |  |      |                                               |      |                                      |                            |")
  time.sleep(0.2)
  print("|                                                                             |      |  |      |  |      |                                               |      |                     -__----_____---__|                            |")
  time.sleep(0.2)
  print("|   -_--________-_---____-__--________------___--__-__-_                                                                                         _--------_----__-_-___----------___--                  \                           |")
  time.sleep(0.2)
  print("|                                                      __-_---__-----_-----__-_-_----                                    _--__-_--_---____---_--                                                         |                         |")
  time.sleep(0.2)
  print("|                                                                                     -___---__-----_-_-_--_---__-_-__---_                                                                                _                         |")
  time.sleep(0.2)
  print("|                                                                                                                                                                                            ____--__-_---  \                       |")
  time.sleep(0.2)
  print("|                                                   ____--___-_------                                                                                                                        _               \____                  |")
  time.sleep(0.2)
  print("|                                       __-_--_---__                 __-_-----___------____                                                                                             ____-                     \                 |")
  time.sleep(0.2)
  print("|   ___---_____-__--_--_--___--___----__                                                   _-__---_                              _---___                                         -__--_-                          \                 |")
  time.sleep(0.2)
  print("|                                                                                                  __-----_------__----_--__---_-       ___----                           __--_--                                  |________________|")
  time.sleep(0.2)
  print("|                                                                                                                                              ____---__-___--____--____-_                                                          |")
  time.sleep(0.2)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.2)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.2)
  print("| You are here, in the village of Dertan                                                                                                                                                                                            |")
  time.sleep(0.2)
  print("|            |                                                                                                                                                                                                                      |")
  time.sleep(0.2)
  print("|            |                                                                                                                                                                               Village of the Edge                    |")
  time.sleep(0.2)
  print("|            |                                                                                                                                                                                        |                             |")
  time.sleep(0.2)
  print("|           \|/                                                                                                                                                                                       |                             |")
  time.sleep(0.2)
  print("|                        ______    ______                                                                                                                                                            \|/                            |")
  time.sleep(0.2)
  print("|         ()  ()        /      \  /      \                                                                                                                                                         ______                           |")
  time.sleep(0.2)
  print("|         \/  \/        |      |  |      |                                                                                                                                                        /      \                          |")
  time.sleep(0.2)
  print("|         /\  /\        |      |  |      |                                                                                                                                                        |      |                          |")
  time.sleep(0.2)
  print(" _______________________|______|__|______|________________________________________________________________________________________________________________________________________________________|______|__________________________|")
def edge():
  print("*This dungeon is the hard dungeon*")
  time.sleep(0.000000000001)
  print("*On the way to the village, you meet a merchant*")
  time.sleep(0.000000000001)
  #enter shop function
  print("*Let's rock.*")
  time.sleep(0.000000000001)
  print("*As you walk across the plains to go to the Village of the Edge...*")
  time.sleep(0.000000000001)
  print("*You meet some wild hyena's.*")
  time.sleep(0.000000000001)
  print("*Perfect! You guys were looking for some extra food.*")
  time.sleep(0.000000000001)
  print("*Prepare to fight.*")
  time.sleep(0.000000000001)
  #enter fight function
  print("*Gained 5 health and 500 gold.*")
  p1health=p1health+5
  p2health=p2health+5
  money1=money1+500
  money2=money2+500
  print(p1_name)
  time.sleep(0.000000000001)
  print("Hp")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p1health)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print("Money")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(money1)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p2_name)
  time.sleep(0.000000000001)
  print("Hp")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p2health)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print("Money")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(money2)
def bloodmist():
  global money1
  global money2
  print("*This dungeon is the normal dungeon.* ")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("*You head out*")
  time.sleep(0.000000000001)
  print("*On the way to the mountains you meet a merchant, where you can buy gear if you choose*")
  #enter shop function
  print("*Now that your geared up you now can begin your quest.*")
  time.sleep(0.000000000001)
  print("--------")
  print("*Nearly a week passes and you almost reach the gates of the Village of the Bloodmist.*")
  time.sleep(0.000000000001)
  guards=input("*Guards stand in your way. Do you want to A.) Fight them and get through, or B.) Sneak Past the guards to get in")
  if guards=="Fight" or guards=="A" or guards=="fight" or guards=="a":
    wboss=5
    fightmechanics1()
    enteringbm()
  if guards=="Sneak Past" or guards=="B" or guards=="b" or guards=="sneak past":
    print("You got past without being seen")

    enteringbm()
def enteringbm():
  print("You make it into the Bloodmist.")
  time.sleep(0.000000000001)
  print("People are giving you weird stares...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("2 men come up to you.")
  time.sleep(0.000000000001)
  print("Who are you people")
  time.sleep(0.000000000001)
  print("We are just travelers, no need to mind us")
  time.sleep(0.000000000001)
  print("Our village is private property, outsiders are not welcome.")
  time.sleep(0.000000000001)
  print("Don't worry, we'll leave.")
  time.sleep(0.000000000001)
  print("No you wont, you'll be staying with us...with your corpses.")
  time.sleep(0.000000000001)
  print("*Prepare to fight*")
  fightmechanics1()
  print("You may have beat us, but watch out. Mr.M is unbeatable.")
  time.sleep(0.000000000001)
  print("*You are intrigued.*")
  time.sleep(0.000000000001)
  print("*You make your way around town and find a shop.*")
  #enter shop functions
  print("Thanks for coming!")
  time.sleep(0.000000000001)
  print("You are walking around town and you hear a rumor.")
  print("The rumor is that there is a monster on top of the mountain and if you kill him you get 50000")
  print("This means you will each get 25000 gold.")
  print("LET'S GOOOOO!!! 50000 GOLD!!!")
  print("You decide to get some rest")
  print("ZZZZZZZZZ")
  time.sleep(2.5)
  print("You have an option ahead of you.")

def dungeon_mountains():
  global bossh
  global wb
  global money1
  global money2
  global p1health
  global p2health
  print("*This dungeon is the easiest dungeon, right choice?*")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  print("*On the way to the mountains you meet a merchant, where you can buy gear if you choose*")
  #enter shop function
  print("*Now that your geared up you now can begin your quest.*")
  time.sleep(0.000000000001)
  print("*You enter the dungeon and you are greeted by four archers.*")
  time.sleep(0.000000000001)
  print("ALRIGHT, OUR FIRST FIGHT!!! WOOOOOOOO!!!!")
  time.sleep(0.000000000001)
  print("LET'S GOOOOOOO")
  print(p2_name)
  print("*They start firing at you.*")
  wboss=1
  bossh=50
  if subclass1=="Healer" or subclass1=="healer":
      wboss=1
      fightmechanicsmage1()
  else:
    fightmechanics1()
def archerafter():
  global money1
  global money2
  global bossh
  global wboss
  time.sleep(0.000000000001)
  print("Nice job! Behind the archers you see a silver chest. Inside the chest you each get 10000 gold.")
  money1=money1+10000
  money2=money2+10000
  print(p1_name)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print("Money")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(money1)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p2_name)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print("Money")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(money2)
  print("Let's keep going.")
  time.sleep(0.000000000001)
  print("*Mysterious mountain men appear...*")
  bossh=100
  wboss=2
  if subclass1=="Healer" or subclass1=="healer":
      fightmechanicsmage1()
  else:
    fightmechanics1()
def afterfight2 ():
  global p1health
  global p2health
  global bossh
  global wboss
  time.sleep(0.000000000001)
  print("Who are you people and why are you here?")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("We are a group of people who have adapted to this region.")
  time.sleep(0.000000000001)
  print("We want to live, please don't hurt us.")
  time.sleep(0.000000000001)
  print("We'll give you some gear if you want, just spare our lives.")
  time.sleep(0.000000000001)
  print("Well, alright! Sure.")
  p1health=p1health+50
  p2health=p2health+50
  print("*You both just recieved 50 health.*")
  print(p1_name)
  time.sleep(0.000000000001)
  print("Hp")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p1health)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p2_name)
  time.sleep(0.000000000001)
  print("Hp")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p2health)
  time.sleep(0.000000000001)
  print("By the way, do you happen to know the fastest route through these mountains?")
  time.sleep(0.000000000001)
  print("I'm trying to get to the Capital right away.")
  time.sleep(0.000000000001)
  print("Sure, however the fastest way through the peak. Are you sure you are ready?")
  time.sleep(0.000000000001)
  print("Heck yeah I'm ready! Let's go!!!")
  time.sleep(0.000000000001)
  print("Alright, then.")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("...")
  time.sleep(0.000000000001)
  print("*You are climbing on the highest peak*")
  time.sleep(0.000000000001)
  print("*Wild, ferocious beasts appear before your eyes.*")
  time.sleep(0.000000000001)
  print("*They seem to be protecting something.*")
  time.sleep(0.000000000001)
  print("*Prepare to fight.*")
  wboss=3
  boss=250
  if subclass1=="Healer":
    wboss=3
    boss=250
    fightmechanicsmage1()
  else:
    boss=250
    fightmechanics1()
def almosts(): 
  global money1
  global money2
  global bossh
  global wboss
  print("*Gained 1000 gold.*")
  money1=money1+1000
  money2=money2+1000
  print(p1_name)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print("Money")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(money1)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(p2_name)
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print("Money")
  time.sleep(0.000000000001)
  print("--------")
  time.sleep(0.000000000001)
  print(money2)
  print("*You have reached the top*")
  wboss=4
  bossh=500
  adstart()
  
startgame()   
char=Char()
    
