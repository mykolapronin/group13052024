# group13052024

- python -m venv venv
- win -- .\venv\Scripts\activate 
pip 
pip list 



python.exe -m install --upgrade pip




pip freeze > requirements.txt
#
# True
# False
# def can_you_swim(answer):
#    positive_part = 'yes'
#    result = positive_part in answer.lower()
#    return result
#
#
# print(can_you_swim('ye s'))
#
#
# result = add_two_numbers(2, 6)
# 
# print(result)








    if string_like_number.isdigit():
        result = int(string_like_number)
        
        is_only_one_dot_string = string_like_number.count('.') == 1
        is_only_digits_except_dots = string_like_number.replace('.', '').isdigit()
        if is_only_one_dot_string and is_only_digits_except_dots:
            result = float(string_like_number)
            return result