"""
Aling Nena stores her soft drink stock on two refrigerators.
She stores Coke, Sprite and Royal on her Sari-sari store's refrigerator while
RC and 7UP can be found on her house's refrigerator.

Help Aling Nena to properly respond to her customer
when buying softdrinks.

The reply will depend if the soft drink brand is on the store's ref,
on the house's ref or none. If the customer buys a soft drink brand that is:
    1. stored on the store, she will respond 'Got it!'
    2. stored on the house, she will respond 'Please wait for a while!'
    3. not sold by her, she will respond 'Sorry we do not sell that. We only
    have <input here the soft drink brands>'
"""

customer_order = input('Hi! What soft drink brand do you want?').lower()

softdrinks_brands = ['Coke', 'Sprite', 'Royal', 'RC', '7UP']

on_store = softdrinks_brands[:4]
# print(on_store)

on_house = softdrinks_brands[3:]
# print(on_house)

#on_store = ['Coke', 'Sprite', 'Royal']
#on_house = ['RC', '7UP']
#softdrinks_brands 

if customer_order in on_store:
	print('Got it!')
elif customer_order in on_house:
	print('Please wait for a while!')
else:
	print('Sorry we do not sell that. We only have ' + ', '.join(softdrinks_brands) + '.')

