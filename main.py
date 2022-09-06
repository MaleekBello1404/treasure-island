print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

decision_1 = input(
    'You\'re at the crossroad, Where do you want to go? Type "left" or "right" '
).lower()
if decision_1 == "left":
    decision_2 = input(
        'You\'ve come to a Lake, There\'s an island in the middle of the lake, type "wait" to wait for a boat. type "swim" to swim across? '
    ).lower()
    if decision_2 == "wait":
        decision_3 = input(
            'You arrived at the Island, there\'s a house with 3 doors. One is red, one is yellow and the last one is blue, Which color will you like to open? '
        ).lower()
        if decision_3 == "yellow":
            print(
                "Took you long enough, You finally found the treasure, or .. have you??(dramatic stare)haaha, you actually won man! Congratulations"
            )
        elif decision_3 == "red":
            print(
                "Really? who tf picks red at the go?? It's a room full of fire loser, Game Over!!!"
            )
        elif decision_3 == "blue":
            print(
                "Lol, you really thought you was going win this, THINK AGAIN! It's a room full of Beast, Game Over!! hahahhahah "
            )
        else:
            print("You choose a door that doesn't exits, Game Over")
    else:
        print(
            "LMAO!! you really thought you was goin swim your way to the Island??, think again young blud. you got attacked by an angry trout and you kinda deserved it, Smart work not hard work. Game over!!"
        )
else:
    print(
        "I don't think Treasure hunting is for you bruv, you fell into a hole already?? GTF outta here, Damn Nigga, Game over!!!."
    )
