import decimal

cheese_kg = decimal.Decimal('1')
cheese_price = decimal.Decimal('1000')

final_cost = cheese_kg * cheese_price
final_cost = final_cost.quantize(decimal.Decimal('0.01'))

# representation
divider_symbol = '-'
divider = divider_symbol * 31
cheese_smile = '\U0001F9C0'
shop_name = 'Ромашка весняна'
header = f'{divider}{shop_name}{divider}'
length_header = len(header)
footer = divider_symbol * length_header

# result output
print(header)
print('Товар\tвага\tціна\tвартість')
print(f'сир{cheese_smile}\t\t\t{cheese_kg}\t\t\t\t{cheese_price}\t\t\t\t{final_cost}')
