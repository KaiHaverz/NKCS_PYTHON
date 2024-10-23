players=[]

def add_player():
    name=input("Enter player name: ")
    number=input("Enter player number: ")
    age=input("Enter player age: ")
    position=input("Enter player position: ")
    dominant_foot=input("Enter player dominant foot: ")
    nationality=input("Enter player nationality: ")
    value=input("Enter player value: ")
    apperance=input("Enter player apperance: ")
    goals=input("Enter player goals: ")
    assists=input("Enter player assists: ")

    player_info={
        'name':name,
        'number':number,
        'age':age,
        'position':position,
        'dominant_foot':dominant_foot,
        'nationality':nationality,
        'apperance':apperance,
        'goals':goals,
        'assists':assists
    }

    players.append(player_info)
    print(f"added successfully {player_info['name']}")
    return player_info


def delete_player():
    serial_number=int(input("Enter serial number you want to delete: "))
    if(serial_number<0 or serial_number>len(players)-1):
        print("Invalid serial number")
    else:
