print("🏝️ Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure.")

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input("You come to a lake. There is an island in the middle.\nType 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    
    if choice2 == "wait":
        choice3 = input("You reach the island safely. You see a house with 3 doors: red, yellow, and blue.\nWhich door do you choose? ").lower()
        
        if choice3 == "red":
            print("🔥 It's a room full of fire. Game Over.")
        
        elif choice3 == "yellow":
            print("🏆 You found the treasure. You Win!")
        
        elif choice3 == "blue":
            print("👻 The room is full of ghosts! You run away, but you're lost forever. Game Over.")
        
        else:
            print("🚪 That door doesn't exist. You're confused and get lost. Game Over.")
    
    else:
        print("🐟 You try to swim, but a fish attacks you. Game Over.")

else:
    print("🕳️ You fall into a hole. Game Over.")
