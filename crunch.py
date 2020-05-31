import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import recipe_parsers

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.onceuponachef.com/recipes/couscous.html'
#url = 'https://cookieandkate.com/raw-beet-salad-with-carrot-quinoa-spinach/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

recipe = recipe_parsers.get_recipe(soup)
if recipe is None:
    print ('No recipes were extracted from the page.')
    exit()

recipe.print()
