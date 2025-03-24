import random
##Inventory items and health for text based adventure game
options = ["1","2"]
inventory = {"money" : 200,
             "healing": 1
             



               }

boss = {
  "health": 20,
  "damage": 5,
}

playerHealth = {
  "Health": 40
}

#this is how we make a function
def pickclass():
 print("you are in the kingdom of Cake")
 print("we are in a war against the dintest coalition")
 print("it's your job to fight the dintests")
 print("please pick a class")
 print("____________________")
 print("press 1 celery paladin")
 print("____________________")
 print("press 2 cilly mage")
 print("____________________")
 print("press 3 brusersprout bomber ")
 print("____________________")
 userinput = input("        ")
 if userinput == "1":
    print("you are a celery paladin")
    inventory.update({"weapon": "celery-sword"})
    inventory.update({"class": "celery-paladin"})
    choclate1()


 elif userinput == "2":
    print("you are a cilly mage")
    inventory.update({"weapon": "cilly-staf"})
    inventory.update({"class": "cilly-mage"})
    choclate1()

 elif userinput == "3":
    print("you are a brusersprout bomber")
    inventory.update({"weapon": "brusersprout-bombs"})
    inventory.update({"class": "brusersprout-bomber" })
    choclate1() 
#lets you shop and use money
def shop():
  ##Default values
 money = inventory["money"]
 food = 0 
 armorA = 0
 armorB = 0
 armorC = 0 
 potions = 0
 userinput = ""
 shoping = False
 print("you have $200")
 ##Continues going until shopping is equal to true
 while shoping == False:
  print("press 1 for a healing potion its $50")
  print("press 2 for grade A armor its $100")
  print("press 3 for grade B armor its $50")
  print("press 4 for grade C armor its $25")
  print("press 5 for food its $25 for 250 pound")
  print("press 6 to leave the shop")
  userinput = input("")
  
   ##adds healing potions if user has enough money
  if userinput == "1" and inventory["money"] >= 50:
    potions += 1
    money -= 50
    inventory.update({"give healing potion":potions})
    inventory.update({"money": money})
    print(f"you have {inventory['money']}")
   



   ##Adds armor if user has enough money
  elif userinput == "2" and inventory["money"] >= 100 :
    armorA += 1
    money -= 100
    inventory.update({"give grade 1 armor":armorA})
    inventory.update({"money": money})  
    print(f"you have {inventory['money']}")
    

 ##Adds grade 2 armor if user has enough money
  elif userinput == "3" and inventory["money"] >= 50:
    armorB += 1 
    money -= 50
    inventory.update({"give grade 2 armor":armorB})
    inventory.update({"money": money})
    print(f"you have {inventory['money']}")
 


##Adds grade 3 armor if user has enough money
  elif userinput == "4" and inventory["money"] >= 25:
    armorC += 1 
    money -= 25
    inventory.update({"give grade 3 armor":armorC})
    inventory.update({"money": money})   
    print(f"you have {inventory['money']}")


   ##Adds food if user has enough money
  elif userinput == "5" and inventory["money"] >= 25:
    food += 250
    money -= 25
    inventory.update({"give food":food})   
    inventory.update({"money": money})
    print(f"you have {inventory['money']}")
  
 ##If the user has no money, it will display this
  elif inventory["money"] ==  0:
     print("you have no money to spend")
  
  

  elif userinput == "5":
     choclate1()



##If the user types something else, it will send the user to mission 1
  else: 
    print("are you srue")
    print("yes or no")
    userinput = ""
    userinput = input("")
  if userinput == ("yes"):
    shoping = True
  else:
    shoping = False
    mission1()

def secondMission():
  print('this works')

def afterFightScene():
  print("You beat the man to a pulp, you walk out with a scene of glory, first mission is over")
  print("Would you like to go to the shop or continue on your adventure?")
  userinput = input("Press 1 to continue, press 2 to go to shop")

  if userinput == "1":
    secondMission()
  elif userinput == "2":
    shop()


def fight():
  ##Default health and damage values
 base_armor = 4
 base_health = 40
 base_damage = 1 
 boss_health = 20
 updatedHealth = 0
 
 userinput = ""

##Updates the player health
 playerHealth.update({"Health": base_health})

##Continues to loop until either the player health is 0 or the boss health is 0
 while boss["health"] > 0 and playerHealth["Health"] > 0:

  userinput = input("Would you like to attack, dodge")

##If the sword is inside the values
  if "celery-sword" in inventory.values() and userinput == "1":
   base_damage = 4

   ##Minus the boss health with the base damange of the hero
   ##reduce the health of character based on random number
   boss_health = boss_health - base_damage
   hitNumber = random.randint(0,10)
   boss.update({"health": boss_health})


   print(f'The boss swings at you and you take {hitNumber}')
   playerHealth["Health"] -= hitNumber
   print(playerHealth)
   print(boss)
   ##Dodge mechanic based on random number
  elif  userinput == "2":
    randomNumber = random.randint(1, 10)  # Random damage from the boss
    reducedDamage = max(0, randomNumber - base_armor)  # Armor reduces damage
    playerHealth["Health"] -= reducedDamage
    print(f"You dodge, but still take {reducedDamage} damage due to your armor.")
    print(f"Player Health: {playerHealth['Health']}")
  elif userinput == "3":
    ##If the user has healing potions
            if inventory['healing'] >= 1 and playerHealth["Health"] != 40:
                print("You drink a potion.")
                health = 10
                ##Increase the users health by 10
                playerHealth["Health"] += health
                inventory['healing'] -= 1  # Decrease the potion count
                ##If the user has over 40 health already
                ##Set the player health to 40
                print("You now have",playerHealth["Health"])
            elif playerHealth["Health"] >= 40:
                playerHealth["Health"] = 40
                print("Your health is now:", playerHealth["Health"])
            ##If the user does not have any potions, run the else statement
            else:
                print("You have no healing potions left.")

  ##If the player health is less than 0, display game over
  elif playerHealth["Health"] <= 0 :
    print("You have died game over")
    intro()
  ##If the bosses health is less than 0, player defeated boss and after fight scene plays
  if boss["health"] <= 0:
    print("You defeated the boss")
    afterFightScene()

  elif playerHealth["Health"] <= 0:
    print("You have died game over")
    intro() 

 




def talk():
 print("you go to talk to the man")

#plays the mission
def mission1():
  print("you approach the falls to confront the man and stop him from turning choclate to watar")
  print("you see sumebody you go to see if he is the person your looking for you approach")
  print("going tords the man you get ready to fight the man")
  print("press 1 to fight")
  print("press 2 to talk")
  userinput = input("")

  if userinput == "1":
     fight()
  elif userinput == "2":
     talk()




    
#let you go to the shop and the frit part of the mission
def choclate1():
 print("now you go to the shop")
 shop()
 print("your frist mission is to the choclate falls to investigate a suspicious man")
 print("that seems to be cleaned up the choclate??")
 print("he is wearing a mask is he a dintest??")
 ##starts the game if the input = yes if not it loops
 print("press 1 to go to investigate")
 print("press 2 to go home")
 userinput = input("")
 if userinput == "1":
  mission1()


 elif userinput == "2":
  cake()
  
 
 def cake():
    print("you go back to the kingdom of cake")



##play the intro to the game 
def intro():
    print(" Hello brave adveturer")
    name = userinput 
    name = input("please put in your name")
    if name == "":
        print("please pick your heain")
    else:
        print('welcome')
        print(f'{name}')
        print("========================================================")
        pickclass()
  




if __name__ in "__main__":
    #Introduction to game 
    print("welcome to the hunt for the pizza rolls")

    userinput = ""

 ##checks to see if the user inputs a valid option
while userinput not in options:
    userinput = input("press 1 to start press 2 to exit")

    if userinput == "1":
        intro()

    elif userinput == "2":
        print("goodbye")
    else:
        print("please enter a valid number")

