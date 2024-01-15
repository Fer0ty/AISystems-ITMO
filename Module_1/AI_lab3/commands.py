import pyswip

prolog = pyswip.Prolog()
prolog.consult('swish-3.pl')


def players():
    results = list(prolog.query(f'player(X).'))
    return [result['X'] for result in results]


def games():
    results = list(prolog.query(f'game(X).'))
    return [result['X'] for result in results]


def find_friends(person):
    results = list(prolog.query(f'friends({person}, X).'))
    return [result['X'] for result in results]


def find_friends_to_play(game):
    results = list(prolog.query(f'have_game(X, {game})'))
    return [result['X'] for result in results]


def find_games(person):
    results = list(prolog.query(f'have_game({person}, X).'))
    return [result['X'] for result in results]


def find_common_friends(person1, person2):
    results = list(prolog.query(f'common_friends({person1}, {person2}, R).'))
    return [result['R'] for result in results]


def find_common_games(person1, person2):
    results = list(prolog.query(f'common_games({person1}, {person2}, R).'))
    return [result['R'] for result in results]


def find_friends_online(person):
    results = list(prolog.query(f'friends_online({person}, R).'))
    return [result['R'] for result in results]


def find_may_be_familiar_with(person):
    results = list(prolog.query(f'may_be_familiar_with({person}, R).'))
    return [result['R'] for result in results]


def find_possible_interesting_games(person):
    results = list(prolog.query(f'possible_interesting_games({person}, R).'))
    return [result['R'] for result in results]
