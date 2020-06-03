from recipe import Recipe
import re

class RecipeDivParser:
    def parse_html(self, soup):
        ingredients = dict()
        instruction = list()

        #find the name of the recipe
        name = soup.find_all('h2',class_='fn tabtitle')[0].text

        #find the name of the recipe
        description = soup.find_all('div',class_='recipedescription')[0].text

        #find all the ingredients for the recipe
        ingr = soup.find_all('li',class_='ingredient')
        for i in ingr:
            #for each ingredient find its NAME and AMOUNT
            ingr_name = i.find_all('span',class_='name')
            ingr_amt = i.find_all('span',class_='amount')
            try:
                #try to get the amount from nested tag with metric system amount
                tmp_lst = ingr_amt[0].contents[0].get('data-alt', None).split()
                if len(tmp_lst) == 1: tmp_lst.append('items')
                ingredients[ingr_name[0].text] = (tmp_lst[0],tmp_lst[1])
            except:
                #if there is no nested tag, then get the only amount provided
                tmp_lst = str(ingr_amt[0].contents[0]).split()
                if len(tmp_lst) == 1: tmp_lst.append('items')
                ingredients[ingr_name[0].text] = (tmp_lst[0],tmp_lst[1])

        #find all the instructions for the recipe
        instr = soup.find_all('li',class_='instruction')
        if len(instr) == 1:
            #if all the instructions are provided as one string, then split it by sentence
            instruction.extend(instr[0].text.split('. '))
        else:
            #otherwise store the instructions as a list of steps
            for i in instr:
                instruction.append(i.text)

        #find the notes for the recipe
        notes = soup.find_all('li',class_='free_text')[0].text

        recipe = Recipe(name, description.strip(), ingredients, instruction, notes.strip())
        return recipe

class TastyRecipeParser:
    def parse_html(self, soup):
        name = 'Couscous from Tasty Recipe'
        description = 'Hello'
        ingredients = {'butter':(2,'Tbsp'),'couscous':(10, 'oz')}
        full_instruction = 'In a medium saucepan, bring the water (or broth), salt, butter, and oil to a boil. Stir in the couscous, cover tightly with a lid, and remove from heat. Let the couscous steam for 5 minutes. Use a fork to fluff the couscous and break up any clumps. Serve warm'
        instruction = full_instruction.split('. ')
        notes = 'The couscous can be frozen for up to 3 months. When ready to serve, reheat it in the microwave until hot'
        recipe = Recipe(name, description, ingredients, instruction, notes)
        return recipe

# The Crunch is able to scrape the recipes from the following plug-ins
PARSERS_BY_FORMAT = {
    ("div","recipediv") : RecipeDivParser(),
    ("div","tasty-recipe-ingredients") : TastyRecipeParser()
}

'''get_recipe function tries to extract the MAIN recipe tag from html file
based on supported in the Crunch recipe plug-ins and if successful, will return the
 object with type recipe'''
def get_recipe(soup):
    for tag_param in PARSERS_BY_FORMAT:
        all_recipes = soup.find_all(tag_param[0],class_=tag_param[1])
        if len(all_recipes)>0:
            # current assumption is that there is ONLY ONE recipe on a webpage
            return PARSERS_BY_FORMAT[tag_param].parse_html(all_recipes[0])
    return None
