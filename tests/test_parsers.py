from recipe import Recipe
import recipe_parsers
from bs4 import BeautifulSoup

def test_parser_div():
    with open("tests/resources/recipe_div.html", "r") as fh:
        soup = BeautifulSoup(fh.read(), 'html.parser')
        recipe = recipe_parsers.get_recipe(soup)

        name='Perfect Couscous'
        description='Couscous is made from tiny steamed balls of semolina flour. Though we think of it as a grain, it\'s actually a type of pasta.'
        ingredients={'low sodium chicken or vegetable broth (or water)': ('400', 'ml'), 'salt': ('1/2', 'teaspoon'), 'unsalted butter': ('1', 'tablespoon'), 'extra-virgin olive oil': ('1', 'tablespoon'), 'couscous': ('283', 'g')}
        instruction=['In a medium saucepan, bring the water (or broth), salt, butter, and oil to a boil', 'Stir in the couscous, cover tightly with a lid, and remove from heat', 'Let the couscous steam for 5 minutes', 'Use a fork to fluff the couscous and break up any clumps', 'Serve warm.']
        notes='Freezer-Friendly Instructions: The couscous can be frozen for up to 3 months.  When ready to serve, reheat it in the microwave until hot.'
        recipe_expected = Recipe(name, description, ingredients, instruction, notes)

    assert recipe == recipe_expected

def test_parser_tasty_recipe():
    with open("tests/resources/recipe_tasty_recipe.html", "r") as fh:
        soup = BeautifulSoup(fh.read(), 'html.parser')
        recipe = recipe_parsers.get_recipe(soup)
    assert recipe.name == 'Couscous from Tasty Recipe'
