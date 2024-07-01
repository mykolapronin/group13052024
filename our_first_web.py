from pywebio.input import input as input_pw
from pywebio.input import NUMBER
from pywebio.output import put_text, put_html, put_image

import constants_web

# header
put_html('<h1>Вас вітає Марінара</h1>')
put_html('<h2>зробіть замовлення🍕</h2>')

# input section
name = str(input_pw('Як вас звати')).title()

formatted_order_pizza = f'Доброго дня, {name}. Скільки акційних піц замовите?'
put_text(formatted_order_pizza)

pizza_count_order = input_pw('Введіть бажану кількість піци', type=NUMBER)

pizza_order_cost = pizza_count_order * constants_web.pizza_cost

formatted_order_cola = f'{name},Ще дуже рекомендую колу по {constants_web.cola_cost} грн за пляшку'
put_text(formatted_order_cola)
cola_count_order = input_pw('Введіть бажану кількість коли', type=NUMBER)
cola_order_cost = cola_count_order* constants_web.cola_cost

total_cost = cola_order_cost + pizza_order_cost
put_text(f'Загальна вартість замовлення буде {total_cost} грн' )

img = open('pizza.jfif', 'rb').read()
put_image(img, width='2500px')
