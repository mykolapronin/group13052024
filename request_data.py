import requests
from pprint import pprint

url = 'https://dummyjson.com/todos'


# response = requests.get(url=url, params=params)
#
# # print(response)
# # print(response.content)
# # print(response.text)
# response_json = response.json()
# todos = response_json['todos']


def get_todos(limit: int = 50, start: int = 0) -> list[dict]:
    params = {
        'limit': limit,
        'skip': start,
    }
    response = requests.get(url=url, params=params)
    response_json = response.json()
    todos = response_json['todos']
    return todos


def get_completed_todos_number(todos_candidates: list[dict], is_completed: bool = True) -> int:
    counter = 0
    for todo in todos_candidates:
        if todo['completed'] is is_completed:
            counter += 1
    return counter


def get_todos_by_content(todos_candidates: list[dict], content: str) -> list[str]:
    content_list = []
    for todo in todos_candidates:
        if content.lower() in todo["todo"].lower():
            content_list.append(todo["todo"])

    return content_list


def main():
    start = 0
    limit = 50

    completed_successfully = 0
    completed_unsuccessfully = 0
    content_lst = []
    content_word = 'solve'
    for iterator in range(1, 301):
        chunk = get_todos(start=start, limit=limit)
        if not chunk:
            break
        completed_successfully += get_completed_todos_number(chunk)
        completed_unsuccessfully += get_completed_todos_number(chunk, is_completed=False)
        content_lst += get_todos_by_content(chunk, content_word)
        start += limit

    print(f'{completed_successfully=}, {completed_unsuccessfully=} {2+2=}')
    pprint(content_lst)


if __name__ == "__main__":
    main()



    # ********************************************
    # n = {
    #     "trip": [
    #         {
    #             "date": "2024-06-24T16:10:49.941Z",
    #             "gender": "Ч",
    #             "dishes": "Борщ, Ковбаса",
    #             "money": 6660,
    #             "name": "ропрпрпр",
    #             "was_contacted": True
    #         },
    #         {
    #             "date": "2024-06-24T16:11:05.747Z",
    #             "gender": "Ж",
    #             "dishes": "Мандарини",
    #             "money": -1,
    #             "name": "null",
    #             "was_contacted": False
    #         },
    #         {
    #             "date": "2024-06-24T16:11:12.078Z",
    #             "gender": "Ч",
    #             "dishes": "Борщ, Макарони",
    #             "money": 3456789,
    #             "name": "Макс",
    #             "was_contacted": True
    #         },
    #         {
    #             "date": "2024-06-24T16:11:42.515Z",
    #             "gender": "Ж",
    #             "dishes": "Борщ, Макарони",
    #             "money": 13,
    #             "name": "чапр",
    #             "was_contacted": False
    #         },
    #         {
    #             "date": "2024-06-24T16:12:14.523Z",
    #             "gender": "Ж",
    #             "dishes": "Макарони, Мандарини",
    #             "money": 1000000,
    #             "name": "Sonya",
    #             "was_contacted": False
    #         },
    #         {
    #             "date": "2024-06-24T16:14:05.239Z",
    #             "gender": "Ч",
    #             "dishes": "Борщ, Ковбаса, Мандарини",
    #             "money": 5000,
    #             "name": "А тут ничего нет",
    #             "was_contacted": False
    #         },
    #         {
    #             "date": "2024-06-24T16:29:07.210Z",
    #             "gender": "Ч",
    #             "dishes": "Макарони, Мандарини",
    #             "money": 888,
    #             "name": "anonym",
    #             "was_contacted": False
    #         }
    #     ],
    #     "count": 7,
    #     "with_gender": True
    # }
