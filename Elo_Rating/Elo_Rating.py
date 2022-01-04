players = input("Please input player names: ").split()
elo_dict = {}
for player in players:
    elo_dict.update({player: 1000})
print(elo_dict)

scores = input("Please input result here. (Template: User1 beats/ties/lost to User2): ")

while scores != "exit":
    score = scores.split()

person1 = score[0]
result = score[1]
person2 = score[len(score)]

    # Elo calculation based on 
    # https://zh.wikipedia.org/wiki/%E7%AD%89%E7%BA%A7%E5%88%86
    # and https://en.wikipedia.org/wiki/Elo_rating_system

if result == "beats":
    new_1 = elo_dict[person1]+32*(1-(1/(1+10**((elo_dict[person2]-elo_dict[person1])/400))))
    new_2 = elo_dict[person2]+32*(0-(1/(1+10**((elo_dict[person1]-elo_dict[person2])/400))))

elif result == "loses":
    new_1 = elo_dict[person1]+32*(0-(1/(1+10**((elo_dict[person2]-elo_dict[person1])/400))))
    new_2 = elo_dict[person2]+32*(1-(1/(1+10**((elo_dict[person1]-elo_dict[person2])/400))))

elif result == "ties":
    new_1 = elo_dict[person1]+32*(0.5-(1/(1+10**((elo_dict[person2]-elo_dict[person1])/400))))
    new_2 = elo_dict[person2]+32*(0.5-(1/(1+10**((elo_dict[person1]-elo_dict[person2])/400))))
    
else:
    print("Invalid Result; Please Try Again")
    new_1 = elo_dict[person1]
    new_2 = elo_dict[person2]

elo_dict.update({person1: int(round(new_1,0))})
elo_dict.update({person2: int(round(new_2,0))})
print(elo_dict)

scores = input("Please input result here. (Template: User1 beats/ties/lost to User2): ")