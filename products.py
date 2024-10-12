products = {
    'cheese' : 500,
    'bread' : 200,
    'tomato':  300
}
products.update({'juice' : 800})
print (products)

price = products.get('cheese', 'product not found')
print (price)