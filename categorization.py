# DESCRIPTIONS ARE ACCORDING TO CHATGPT (take with a grain of salt)


ales = set() # ALE
ipas = set() # A subset of ales
dark_ales = set() # A subset of ales

lagers = set() # LAGERs are different somehow? idek man

sakes = set() # RICE BEER
misc = set() #Beers I was unable to classify into a category

# I don't know if this is a 'real' category but these are all fruit infused or based beers
fruitbeers = set()

# Not sure how to categorize the 'lambics'
# MEAD IS ITS OWN CATEGORY OF ALCOHOL BUT I PUT IT INTO p_fruit cuz its sweet

for d in dataset:
    # presets based on ChatGPT categorizations
    p_ales = ['Belgian White &#40;Witbier&#41;', 'Berliner Weisse', 'Bire de Garde', 'Saison', 'Schwarzbier', 'Abbey Dubbel', 'Abbey Tripel', 'Abt/Quadrupel', 'Altbier', 'Barley Wine', 'German Hefeweizen', 'German Kristallweizen', 'Weizen Bock']
    p_paleales = ['Premium Bitter/ESB', 'Bitter',]
    p_lagers = ['Dunkelweizen', 'Kölsch', 'Klsch', 'Eisbock', 'Malt Liquor', 'California Common', 'Doppelbock', 'Dunkel', 'Dunkler Bock', 'Dortmunder/Helles', 'Heller Bock', 'Oktoberfest/Mrzen', 'Vienna', 'Zwickel/Keller/Landbier']
    p_fruit = ['Cider', 'Fruit Beer', 'Ice Cider/Perry', 'Perry', 'Mead']

    if not d:
        continue
    s = d['beer/style']
    if 'Pale Ale' in s or 'IPA' in s or s in p_paleales:
        ipas.add(s)
    elif 'Ale' in s or s in p_ales:
        ales.add(s)
    elif 'Stout' in s or 'Porter' in s:
        dark_ales.add(s)
    elif 'Lager' in s or 'Pilsener' in s or s in p_lagers:
        lagers.add(s)
    elif 'Sak' in s:
        sakes.add(s)
    elif s in p_fruit:
        fruitbeers.add(s)
    else:
        misc.add(s)

# print the size of each set
print('Ales:', len(ales))
print('Lagers:', len(lagers))
print('Stouts:', len(stouts))
print('IPAs:', len(ipas))
print('Sakes:', len(sakes))
print('Fruit Beers:', len(fruitbeers))

print(misc)

# TODO
'''
It is definitely worth looking into splitting up the 'ale' dataset into more specific categories.
I haven't looked into the dataset enough but I assume the vast majority of beers fall under this category, 
unless we break it up or perform some model balancing I would expect it to be heavily biased towards this category.

The same could possibly be said fo for the lagers category, but I'm not sure.
'''
