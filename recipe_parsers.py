from recipe import Recipe

class RecipeDivParser:
    def parse_html(self, soup):
        name = 'Couscous from Div'
        ingredients = {'butter':(1,'Tbsp'),'couscous':(10, 'oz')}
        full_instruction = 'In a medium saucepan, bring the water (or broth), salt, butter, and oil to a boil. Stir in the couscous, cover tightly with a lid, and remove from heat. Let the couscous steam for 5 minutes. Use a fork to fluff the couscous and break up any clumps. Serve warm'
        instruction = full_instruction.split('. ')
        notes = 'The couscous can be frozen for up to 3 months. When ready to serve, reheat it in the microwave until hot'
        recipe = Recipe(name, ingredients, instruction, notes)
        return recipe

class TastyRecipeParser:
    def parse_html(self, soup):
        name = 'Couscous from Tasty Recipe'
        ingredients = {'butter':(1,'Tbsp'),'couscous':(10, 'oz')}
        full_instruction = 'In a medium saucepan, bring the water (or broth), salt, butter, and oil to a boil. Stir in the couscous, cover tightly with a lid, and remove from heat. Let the couscous steam for 5 minutes. Use a fork to fluff the couscous and break up any clumps. Serve warm'
        instruction = full_instruction.split('. ')
        notes = 'The couscous can be frozen for up to 3 months. When ready to serve, reheat it in the microwave until hot'
        recipe = Recipe(name, ingredients, instruction, notes)
        return recipe

# The Crunch is able to scrape the recipes from the following plug-ins
PARSERS_BY_FORMAT = {
    ("div","recipediv") : RecipeDivParser(),
    ("span","tasty-recipe-ingredients") : TastyRecipeParser()
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
