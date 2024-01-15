import commands
import parse
import re

messages = {
    "start_message": "Программа работает на базе знаний prolog. \n\"help\" для помощи",
    "help_msg": "1) Запрос вводится в виде: \"Меня зовут *имя*. *действие* (с *имя)\"\n Пример1: \"Меня зовут артемий. "
                "Выведи список друзей.\" \n Пример2: Меня зовут артемий. Кто общий друг с вадим?\" \n имена "
                "ВАЖНО: имена вводятся с МАЛЕНЬКОЙ буквы.\n"
                "2) exit - выход из программы \n"
                "3) actions - список доступных действий.\n"
                "4) players - список доступных имен.\n"
                "5) games - список доступных игр"
}

if __name__ == '__main__':
    print(messages["start_message"])
    input_string = input(">>>")
    name_pattern = r'Меня зовут (\w+)\.'
    name = re.match(name_pattern, input_string).group(1)
    is_first = True
    while (True):
        if is_first:
            parse.parse("Меня зовут "+name+input_string.rsplit(name,1)[1])
            is_first = False
        else:
            input_string = input(">>>")
            if input_string == "exit":
                break
            if input_string == "help":
                print(messages["help_msg"])
            elif input_string == "actions":
                for s in parse.available_actions:
                    print(s)
            elif input_string == "players":
                names = commands.players()
                for s in names:
                    print(s)
            elif input_string == "games":
                games = commands.games()
                for s in games:
                    print(s)
            else:
                parse.parse("Меня зовут "+name+". "+input_string)
