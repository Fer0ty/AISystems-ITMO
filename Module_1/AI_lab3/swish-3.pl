%Факты
player(андрей).
player(рома).
player(вадим).
player(ваня).
player(родион).
player(артемий).
player(владислав).
player(никита).
player(костя).
player(саша).
player(илья).
player(кирилл).

online(артемий).
online(илья).
online(никита).
online(костя).
online(рома).

game(dst).
game(cs).
game(astroneer).
game(hoi4).
game(smc5).
game(phasmophobia).
game(fortheking).
game(seaofthieves).
game(lostcastle).
game(humanfallflat).

friends(вадим, рома).
friends(вадим, артемий).
friends(рома, вадим).
friends(рома, артемий).
friends(андрей, рома).
friends(андрей, артемий).
friends(родион, илья).
friends(родион, артемий).
friends(ваня, артемий).
friends(владислав, никита).
friends(илья, родион).
friends(илья, артемий).
friends(илья, никита).
friends(илья, кирилл).
friends(илья, саша).
friends(кирилл, никита).
friends(кирилл, костя).
friends(кирилл, артемий).
friends(кирилл, саша).
friends(кирилл, илья).
friends(саша, артемий).
friends(саша, костя).
friends(саша, никита).
friends(саша, илья).
friends(саша, кирилл).
friends(костя, никита).
friends(костя, артемий).
friends(костя, саша).
friends(костя, кирилл).
friends(никита, владислав).
friends(никита, костя).
friends(никита, саша).
friends(никита, артемий).
friends(никита, кирилл).
friends(никита, илья).
friends(артемий, ваня).
friends(артемий, вадим).
friends(артемий, рома).
friends(артемий, андрей).
friends(артемий, родион).
friends(артемий, никита).
friends(артемий, илья).
friends(артемий, костя).
friends(артемий, саша).
friends(артемий, кирилл).

%друзья и их игры
have_game(артемий, cs).
have_game(артемий, dst).
have_game(артемий, astroneer).
have_game(артемий, hoi4).
have_game(артемий, smc5).
have_game(артемий, phasmophobia).
have_game(артемий, fortheking).
have_game(артемий, seaofthieves).
have_game(артемий, lostcastle).
have_game(артемий, humanfallflat).
have_game(вадим, dst).
have_game(вадим, astroneer).
have_game(родион, cs).
have_game(родион, dst).
have_game(андрей, cs).
have_game(андрей, hoi4).
have_game(кирилл, hoi4).
have_game(кирилл, cs).
have_game(кирилл, smc5).
have_game(кирилл, phasmophobia).
have_game(рома, cs).
have_game(рома, astroneer).
have_game(рома, phasmophobia).
have_game(рома, humanfallflat).
have_game(никита, cs).
have_game(никита, fortheking).
have_game(никита, seaofthieves).
have_game(никита, humanfallflat).
have_game(никита, dst).
have_game(саша, cs).
have_game(саша, hoi4).
have_game(саша, smc5).
have_game(саша, phasmophobia).
have_game(саша, fortheking).
have_game(саша, seaofthieves).
have_game(владислав, cs).
have_game(илья, cs).
have_game(илья, dst).
have_game(илья, fortheking).
have_game(илья, lostcastle).
have_game(ваня, cs).
have_game(ваня, seaofthieves).
have_game(ваня, astroneer).
have_game(костя, cs).
have_game(костя, fortheking).

%Правила

common_friends(Persone1,Persone2, R):-  
    friends(Persone1,R), 
    friends(R,Persone2),
    \+ (Persone1 = Persone2).


common_games(Persone1,Persone2, R):- 
    have_game(Persone1,R),
    have_game(Persone2,R).


friends_online(Person, R):- 
    friends(Person, R),
    online(R).


may_be_familiar_with(Persone, R):-  
    friends(Persone,Friend), friends(Friend,R),
    not(friends(Persone,R)),
    not(Persone=R).


possible_interesting_games(Persone, R):- 
    friends(Persone,Friend),
    have_game(Friend,R), 
    not(have_game(Persone,R)).




