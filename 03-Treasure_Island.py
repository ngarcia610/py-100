# Day 3 - Create a choice based adventure game.
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

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You walk along a forest path and stop upon reaching a fork in the road.")

# First Choice Path
choice = input("Which direction do you go? left or right? ").lower()
if choice == "left":
    print("The path leads to a calm body of water. In the distance you see a cabin on the beach.")
    # Second Choice Water
    choice = input("Do you swim across or wait at the waters edge? swim or wait? ").lower()
    if choice == "wait":
        print("You wait and hear the creaking of a nearby canoe tied a tree. You climb inside and paddle safely to the shore.")
        print("You step inside the cabin and find yourself in front of three colored doors: Red, Yellow, and Blue.")
        # Third Choice Doors
        choice = input("Which door do you open? Red, Yellow, or Blue? ").lower()
        if choice == "yellow":
            print("You open the door and find the room brimming with jewelry, coins, and ancient artifacts. Congratulations.")
        elif choice == "red":
            print("The handle on the door is incredibly hot. When opened flames engulf the cabin. Game Over.")
        elif choice == "blue":
            print("The handle on the door chills to the touch. When opened a cold wind encases your body in ice. Game Over.")
        else:
            print("You decide not to choose any of the doors and head back to a life of mediocrity. Game Over.")
    else:
        print("Upon reaching the midway point, you are pulled under by the iron grip of the Kraken. Game Over.")
else:
    print("The path leads to a rocky cliff. While trying to turn back you slip and fall to the crashing waves below. Game Over.")

