### BLAHAJ VOYAGE ###
# MLH Local Hack Day: Learn 2022
# Day 1 - Text-Based Adventure Game
#
# Made by AnimatorOfSouls
# GitHub: https://github.com/AnimatorOfSouls/Blahaj-Voyage
#
# The journey of a brave Blahaj travelling across the country to reach their destiny at Ryan's house.
#



from random import randint
from math import floor
import json
import sys
import time



# Displays text from file
def display(file):
	with open(file) as f:
		lines = f.readlines()
	for line in lines:
		for c in line[:-1]:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.0002)
		print()


# Welcome and storyline info
def chapter_0():
	display("ch0.txt")


# Rolling a charisma check for companions
def chapter_1():
	display("ch1.txt")
	
	
	# Charisma Roll
	print("How much CHARISMA does Blahaj have?\nRoll a dice: 1-6 CHARISMA\nFlip a coin: Win = 6 CHARISMA, Lose = 1 CHARISMA\n")
	option = str(input("Which option do you choose? (dice/coin)\n")).lower()
	while option != "dice" and option != "coin":
		option = str(input("Invalid input.\nWhich option do you choose? (dice/coin)\n")).lower()
	print()
	
	if option == "dice":
		print("You roll the dice...")
		souls = randint(1,6)
		print("You rolled a "+str(souls)+"!")
	else:	#coin flip
		guess = str(input("You flip the coin. What will it land on? (heads/tails)\n"))
		while guess != "heads" and guess != "tails":
			guess = str(input("Invalid input. What will it land on? (heads/tails)\n"))
		
		flip = randint(1,2)
		if flip == 1:
			flip = "heads"
		else:
			flip = "tails"
		print("\nThe coin falls through the air and lands on... "+flip+"!")
		
		if guess == flip:
			print("You guessed correctly!")
			souls = 6
		else:
			print("You guessed wrong :(")
			souls = 1
		
	print("You now have "+str(souls)+" CHARISMA.\n\n")
	
	
	# Exit text
	print("--------")
	print("After activating their CHARISMA, Blahaj reaches out to the other sharks.\nWith their power, "+str(souls)+" of the sharks wake up and join Blahaj.")
	print("The ground under the crate suddenly jolts, sending Blahaj and his new friends sprawling. The lorry has begun to move...")
	return souls


# A single monster fight in chapter 2
def fight(chosen, souls):
	hp = 100
	str = 30
	
	# Reading JSON
	with open("products.json") as file:
		data = json.load(file)
	
	# Choosing monster
	rand_id = randint(0,len(data["products"])-1)
	while rand_id in chosen:
		rand_id = randint(0,len(data["products"])-1)
	chosen.append(rand_id)
	for p in data["products"]:
		if p["id"] == rand_id:
			enemy = p
			break
			
	# Display info about the fight
	ename = enemy["name"]
	ehp = enemy["hp"]
	estr = enemy["str"]
	
	ename_f = ""
	for c in ename:
		ename_f += c.upper()+" "
	print("--------------")
	print(f"[Fight {len(chosen)}/3]\nB L A H A J    VS    {ename_f}\n")
	print(f"{ename} <> {ehp} HP <> {estr} STR")
	print(f"Blahaj <> {hp} HP <> {str} STR <> {souls} Companions")
	
	# Fighting...
	while hp > 0 and ehp > 0:
		print()
		print("------------")
		atk = randint(int(str/2),str)
		eatk = randint(int(round(enemy["str"])/2),enemy["str"])
		hp -= eatk
		ehp -= atk
		
		#attack messages
		print(f"Blahaj dealt {atk} damage!")
		print(f"{ename} dealt {eatk} damage!")
		print()
		
		#stats
		print(f"Blahaj - {hp} HP")
		print(f"{ename} - {ehp} HP")
		
		#check if dead
		if hp <= 0 and ehp <= 0:
			print("Both fighters have died, the fight will start again.")
			chosen.pop()
			chosen, souls = fight(chosen,souls)
		elif hp <= 0:
			print("Blahaj is dead...")
			if souls > 0:
				print("Their soul escapes their body and enters the body of one of their companions.")
				souls -= 1
				chosen.pop()
				chosen, souls = fight(chosen,souls)
			else:
				input("Blahaj has no more companions :(\n\nG A M E    O V E R\n\nPress Enter to Quit ")
				quit()
		elif ehp <= 0:
			print(f"{ename} is dead!")
		
		print()
		input("Press enter to continue ")
		
	return chosen, souls
	

# Fighting flat-packed furniture on a truck
def chapter_2(souls):
	display("ch2.txt")
	
	# Fight 3 Monsters
	chosen = []
	for i in range(3):
		chosen,souls = fight(chosen,souls)
		
	print("------------")
	print("Blahaj ascends towards the prime location at the top of the box pile, clambering over the bodies of those\nthat they have defeated.")
	print("\nSEVERAL HOURS LATER...\n")
	print("The truck suddenly comes to a stop. Sunlight spills in through the doors as they open, a relief after spending\nseveral hours sitting in the dark.")
	print("\n\n\n")
	
	return souls
		

# Reaching Ryan's house
def chapter_3(souls):
	display("ch3.txt")
	print(f"Final Number of Companions: {souls}\n\n")
	
	

def main():
	chapter_0()
	souls = chapter_1()
	souls = chapter_2(souls)
	chapter_3(souls)

main()
