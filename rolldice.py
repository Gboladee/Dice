import random
print("Infinity Dice!")
def rollDice (noOfsides):
    while True:
        roll = random.randint(1, noOfsides)
        print("you rolled", roll)
        stay= input("Do you want to continue?")
        if stay == "yes":
            print("Let's go !")
            continue
        else:
            print("Bye!")
            break    
        
rollDice(noOfsides)         