import random
choice1 = random.randint(1, 2)

if choice1 == 1:
    who = 'You got caught by the police for running a red light.'
    
else:
    who = 'You caused someone to swerve to avoid crashing into you and crash into a street light.'
print("The goal of this game is to drive your car 10 yards with out runnning a red light. Good Luck!")

distance = 10

while distance > 0:

    print("You have " + str(distance) + " yards left to go.")
    move = input("Would you like to move (yes or no)? ")
    light = "Yellow"

    choice = random.randint(1, 100)
    
    if choice <= 25:
        light = 'Red'
        
    else:
        light = 'Green'

    print(light + " Light!")
    
    if move == "yes":
        
        if light == "Red":
            print(who + " You have to go back to the start.")
            distance = 10
            
        if light == "Green":
            distance -= 2

print("You made it!")
