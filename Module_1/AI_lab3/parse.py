import commands
import re

available_actions = {"кто общий друг",
                     "какие общие игры",
                     "выведи список \"в сети\"",
                     "выведи список друзей",
                     "выведи список игр",
                     "выведи рекомендованные игры",
                     "с кем поиграть",
                     "выведи рекомендованные друзья"
                     }


def do_action(action, person):
    actions = {
        "выведи список \"в сети\"": commands.find_friends_online(person),
        "выведи список друзей": commands.find_friends(person),
        "выведи список игр": commands.find_games(person),
        "выведи рекомендованные игры": commands.find_possible_interesting_games(person),
        "выведи рекомендованные друзья": commands.find_may_be_familiar_with(person)
    }
    return actions[action]


def do_action_v2(action, person1, person2):
    actions = {
        "кто общий друг": commands.find_common_friends(person1, person2),
        "какие общие игры": commands.find_common_games(person1, person2),
        "с кем поиграть": commands.find_friends_to_play(person2)
    }
    return actions[action]


def is_available_action(action):
    if action in available_actions:
        return True
    return False


def parse(string):
    name_pattern = r'Меня зовут (\w+)\. (.*?) [вс] (\w+)\?'
    action_pattern = r"Меня зовут (\w+)\. (.*?)\."
    match_two_names = re.match(name_pattern, string)
    match_name_action = re.match(action_pattern, string)
    if match_two_names:
        name1 = match_two_names.group(1).lower()
        action = match_two_names.group(2).lower()
        name2 = match_two_names.group(3).lower()
        if not (name1 in commands.players()):
            print("Такого имени нет в списке")
            print("Список рекомендованных игр:")
            for i in commands.games():
                print(i)
        if is_available_action(action):
            results = do_action_v2(action, name1, name2)
            if results:
                print(set(results))
                return True
            else:
                print("False")
                return True
        else:
            print("Ошибка в построении запроса.")
            return False
    elif match_name_action:
        name = match_name_action.group(1).lower()
        action = match_name_action.group(2).lower()
        if not (name in commands.players()):
            print("Такого имени нет в списке")
            print("Список рекомендованных игр:")
            games = commands.games()
            for i in games:
                print(i)
        if is_available_action(action):
            results = do_action(action, name)
            if results:
                print(set(results))
                return True
            else:
                print("False")
                return True
        else:
            print("Ошибка в построении запроса.")
            return False
    else:
        print("Не удалось разобрать входную строку.")
        return False
