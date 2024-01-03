name = input("Type your name: ")
print("Welcome",name,"to this adventure! Here's how your journey will begin.")

answer = input("You're on a dirt road and it's come to an end. You can either go left or right, which way would you like to go?: ").lower()

if answer=="left":
    answer=input("You've come to a river. You can either walk over a bridge or swim across this vast river. Which fate will you choose? Type walk to walk over the bridge or swim to swim across: ").lower()
    
    if answer =="swim":
        print("You swam across and were eaten by a shark")

    elif answer == "walk":
        print("You walked for many miles and miles, ran out of water, and passed away in the lonley dessert. You lose, try again!")

    else:
        print("That was not one of the options. You lose!")

elif answer=="right":
    answer = input("You've stumbled upon a jungle. Would you like to treck through it or test your luck with going around?(Go Through or Go Around): ").lower()

    if answer == "go through":
        answer = input("It's taking a long time to get through and now daylight is becoming thin. Do you set up camp or continue forward?(Camp or Forward): ").lower()

        if answer =="camp":
            answer = input("You set up camp and hear a scary noise in the distance. Do you ignore it and go to sleep or investigate?(Ignor or Investigate): ").lower()
            if answer == "ignore":
                print("You ignor it and fall asleep and get eaten in your sleep by a tiger. You died :( , try a different path.")
            elif answer == "investigate":
                print("You went to investigate and got bitten by a snake. The venom made you go crazy and you were found years later dead in a cave.")
                print("You lose :( , try a different path.")
            else:
                print("Sorry this answer is invalid")

        
        elif answer == "forward":
            print("You fell into quicksand. You lose, try again!")
        
        else:
            print("Not a valid answer. Try again")

    elif answer == "go around":
        answer = input ("You walk along the shore and start to become hungry. Do you eat a coconut or try and catch a fish?(Coconut or Fish): ").lower()

        if answer == "coconut":
            print("You crack open the coconut and eat it's contents. Hours later you start to feel sick and die from eating a rotten coconut.""You died! :( , try again.")
        
        elif answer == "fish":
            print("You're successful! Your health was replenished an you now have the strenth to continue on another day.")
            answer = input("You have a restful slumber and you see a ship passing by. Do you shout out for help or continue on your adventure?(Shout or Continue): ").lower()

            if answer == "shout":
                print("You shout to the ship and they rescue you and take you back home! Hooray!")

            elif answer == "continue":
                print("You decide to let your ego do the talking and continue on. You survive for some time but that was the only ship you've seen and now you die from starvation. :( . ")

            else:
                print("Don't enter an invalid answer")
        else:
            print("Sorry that's invalid")
    
    else:
        print("That was not a valid answer")
        

else:
    print("Type in either left or right next time")

print("Thank you for trying", name)