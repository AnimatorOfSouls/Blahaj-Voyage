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



# Displays text from file
def display(file):
	with open(file) as f:
		lines = f.readlines()
	for line in lines:
		print(line[:-1])


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


def chapter_2():
	display("ch2.txt")
	
	
	# Reading JSON
	with open("products.json") as file:
		data = json.load(file)

	
	# Fight 3 Monsters
	chosen = []
	str = 40
	for i in range(1):
		hp = 100
		
		# Choosing monster
		rand_id = randint(0,len(data["products"])-1)
		while rand_id in chosen:
			rand_id = randint(0,len(data["products"])-1)
		chosen.append(rand_id)
		for p in data["products"]:
			if p["id"] == rand_id:
				enemy = p
				break

		#TODO: message saying "You are now fighting enemy-name"
		# Fighting monster
		ehp = enemy["hp"]
		ename = enemy["name"]
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
			if hp <= 0:
				print("Blahaj is dead!")
				#TODO: take a soul and restart the fight, or die and restart/quit
			if ehp <= 0:
				print(f"{ename} is dead!")
			if hp <= 0 and ehp <= 0:
				print("Both fighters have died, the fight will start again.")
				hp = 100
				ehp = enemy["hp"]
			print()
			
			input("Press enter to continue ")
	

def main():
	#chapter_0()
	#chapter_1()
	chapter_2()

main()
