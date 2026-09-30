room = 'starting'
keys = 0
game_running = True

while game_running:
    if room == 'starting':
        print("You fall into a big hole it led you into a big labatory. To your left is a Teleporter that has two keys holes, that Teleporter can take you home! To you left is a big door that leads into a massive room.")
        print("If you want to fix the Teleporter, enter '1'. To go into that big room, enter '2'")

        answer = input("1-2: ")

        if answer == "1":
            room = "Teleporter"
        elif answer == '2':
            room = "big"
        else:
            print("Invalid input entered")
            
    elif room == "Teleporter":
        if keys >= 2:
            print("The Teleporter turns on! You step in and a loud ringing noise fills your ears, you are blinded by a light. When you open your eyes, you are home! YOU WIN!!!")
            game_running = False
        else:
            print("You two keys to fix this Teleporter, you only have " + str(keys) + "!")
            room = 'starting'
            
    elif room == 'big':
        print("You enter the massive room. To your left, you see a advanced safe with a math puzzle. To your right, you see a weird machine that has a word puzzle on it.")
        print("Enter '1' to do the math puzzle, enter '2' to do the word puzzle, enter '3' to go back to the starting room")

        answer = input("1-3: ")

        if answer == "1":
            room = "math"
        elif answer == "2":
            room = "word"
        elif answer == "3":
            room = "starting"
        else:
            print("Invalid Input Entered!")
            
    elif room == "math":
        print("You see in front of you the following puzzle:")
        print("3 + 4 * 2")
        print("Choose your answer below:")
        print("a: 8")
        print("b: 11")
        print("c: 14")
        print("d: 18")

        answer = input("a-d: ").lower()

        if answer == "a" or answer == "c" or answer == "d":
            print("Sorry, that is incorrect")
            room = "big"
        elif answer == "b":
            print("That is correct! You have been awarded 1 key")
            keys += 1  
            room = "big"
            
    elif room == "word":
        print("You see in front of you the following puzzle:")
        print("Descramble the name of an element: norcb")

        answer = input("Type out your answer: ").lower()

        if answer == "carbon":
            print("That's correct! One key has been shot out of the machine!")
            keys += 1  
            room = "big"
        else:
            print("Sorry, that is incorrect")
            room = "big"

    else:
        print("Sorry, that is incorrect.")
# finished it yay!!!
# if your reading this hello! lolololololololololololololol
# this isnt my first time coding, its like my fifth time maybe but def the first time i followed a tut alll the way ngl! its kinda sad
# but im very proud of what i made here!
# cant wait to get those stickers!!!
# 60 mins of coding wow
