inventory = {
    'gold': 500,
    'pouch': ['flint','twine','gemstone'],
    'backpack': ['xylophone','dagger','bedroll','bread loaf']
}
inventory.update({'pocket': ['seashell','strange berry','lint']})
del inventory['backpack'][1]
inventory['gold']= 500+50
print(inventory)