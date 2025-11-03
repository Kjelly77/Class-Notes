# Immutable - cant change - a string cant change, but you can make a new string

#store recipes in a list

recipes=[]

def show_recipe(recipe):
    print("="*40)
    print(recipe["name"])
    print("="*40)
    for quant,unit,ingredient in recipe["ingredients"]:
        print(f" - {quant} {unit} {ingredient}")
    print("="*40)
    for direction in recipe["directions"]:
        print(f" - {direction}")
    print("="*40)

recipe={"name":"cookies", "ingredients":[(2,"cups""sugar"),(1, "tsp","salt")],
"directions":["add wet ingredients", "add dry ingredients"]} #dict

recipes.append(recipe)

for r in recipes:
    show_recipe(r)

import pickle

with open("recipes.pkl","wb") as file:
    pickle.dump(recipes, file)

with open("recipes.pkl","rb") as file:
    #missed in, but example shared in project readme



#RANDOM

import random

random.seed(0) #no longer random, it looks like it though

def roll():
    value.random.randomint(1,6)
    print(value)

for i in range(15):
roll()