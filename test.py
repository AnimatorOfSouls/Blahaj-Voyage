
import json

with open("products.json") as file:
	data = json.load(file)
	for p in data["products"]:
		print(p["name"])
