recipe = {"name":"cookies","ingredients":["2 cups sugar","1 stick butter"],
    "intructions":["mix dry ingredients", "fold in wet"]}

new_ins

recipe["instructions"].append(new_ins)

while True:
    ing=input("ingredient: ")
    if ing!="done":
        recipe["ingredients"].append(ing)

class Recipe:
    def _init_9(self,name)
        self.name=name
        self.instrcutions=[]
        self.ingreditents=[]
    def add_ingredient(item):
        self.ingredient.append(item)
    def add_instruction(item):
        self.instructions.append(item)