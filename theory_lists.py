# cities = 'Lviv Odesa     Kherson'.split()
# # result = ['Lviv', 'Kyiv', 'Kherson']
#
# print(cities)
# print(cities[0])
# print(cities[2])
# # print(cities[20])
#
# odesa_name = cities[1]
# odesa_name = odesa_name.upper()
#
# cities[1] = 'Kyiv'
#
# cities.append(odesa_name)
# cities.append(11111)
# cities.append(True)
# cities.append(None)
#
# print(len(cities))
# print(len('fghfghfjfgjjfgjyt'))
#
# pass

new_purchase = []

mom_purchase = [
    'bread',
    'milk',
    'ice-cream',
    'water',
]

print(mom_purchase)

sister_wish = 'doll'
mom_purchase.append(sister_wish)

father_wish = [
    'beer',
    'chips',
]

# # mom_purchase.append(father_wish)
# mom_purchase.extend(father_wish)
#
# mom_purchase.remove('beer')
# mom_purchase.remove('car')
# mom_purchase.pop()
# deleted = mom_purchase.pop(0)
# mom_purchase.pop(0)
# mom_purchase.insert(0, 'matches')

final_purchase_list = mom_purchase * 2

# new_list[0] = new_list[0] * 2
final_purchase_list[0] *= 2


number = 10
number += 5
number -= 3
number *= 3
number /= 3

final_purchase_list += father_wish
final_purchase_list += father_wish

for product_ in final_purchase_list:
    print(product_)
















