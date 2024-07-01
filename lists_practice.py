from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider
from pywebio.output import put_success, put_error, put_warning, put_image, put_html
from pywebio.session import run_js
from pywebio import start_server

admin_one_login = 'aaa'
admin_one_password = '123'

bad_weather = ['Хмарно', 'Шторм']
good_weather = ['Сонячно', 'Сніжно']
weathwer_options = bad_weather + good_weather

emotions = ["Круто", "Набридло"]

monitoring_info = []


def main():
    put_html('<h1>Програма моніторингу погоди</h1>')
    # login = input_pw('Введіть ваш логін', required=True)
    # password = input_pw('Введіть ваш пароль', type=PASSWORD, required=True)

    # if login != admin_one_login or password != admin_one_password:
    #     put_error('Невірний логін чи пароль')
    #     run_js('setTimeout(function(){location.reload();}, 7000)')
    #     return

    monitoring_date = input_pw('Введіть дату спостереження', type=DATE)
    weather = select('Яка сьогодні погода', options=weathwer_options)

    if weather in good_weather:
        put_success('Супер що класно погуляв')

    short_desription = textarea('Опишіть природу сьогодні')
    temperature = slider('Температура', min_value=-35, max_value=50)
    your_emotions = checkbox('Які у вас емоції', options=emotions)
    alone = radio("Ви були самі", options=[True, False])
    if alone:
        put_image('https://neurosciencenews.com/files/2023/11/loneliness-alone-neurosicnecee-1155x770.jpg.webp')
    else:
        put_image(
            'https://i0.wp.com/weezproject.com/wp-content/uploads/2018/11/youarenotalone-e1580544593298.jpg?resize=640%2C182&ssl=1')

    monitoring_info.append([monitoring_date, weather])
    run_js('setTimeout(function(){location.reload();}, 4000)')


if __name__ == '__main__':
    start_server(main, port=11000)
