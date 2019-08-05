prices = {
    'banana': 4,
    'apple': 2,
    'orange':1.5,
    'pear': 3
}
stock = {
    'banana':6,
    'apple': 0,
    'orange': 32,
    'pear':15
}
for k,v in prices.items():
    print (k)
    print('prices: ',v )
    if k in stock:
        print('stock: ',end = '')
        print(stock[k])

t = 0
for n in prices:
    t += prices[n]*stock[n]
print('Tổng', t)
