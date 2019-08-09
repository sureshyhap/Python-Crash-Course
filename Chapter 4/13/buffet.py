foods = ('burgers', 'fries', 'lasagna', 'alfredo', 'macaroni')
for food in foods:
    print(food)
    
new_food1 = 'chicken'
new_food2 = 'vegan burger'
foods = (new_food1, new_food2, foods[2], foods[3], foods[-1])
for food in foods:
    print(food)
