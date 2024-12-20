import random
bot = random.randint(1 , 20)

attemp = 0

while True:
    attemp += 1
    userinput = int(input("Enter Number(1 to 20): "))
    if(bot == userinput):
        print(f"YOU SELECT RIGHT NUMBER IN {attemp} attemp")
        break
    else:
        print("LOOSE")

print("bot Choose: ", bot )
print("you Choose: ", userinput)


