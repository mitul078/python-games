import random
numbers = [-1, 0, 1]
botNumber = random.choice(numbers)
botDic = {-1: "Rock" , 0: "Paper" , 1: "Scissors" }
bot = botDic[botNumber]

userinput = input("Enter (r for rock , p for paper , s for scissors ) :----> ")
userDic = {"r": "Rock", "p": "Paper", "s": "Scissors"}
you = userDic[userinput]

print("Bot Choose :" ,bot)
print("YOU Choose :" , you)

if(bot ==  you):
    print("DRAW")
else:
    if(bot == "Rock" and you == "Paper"):
        print("YOU WIN") 
    elif(bot == "Rock" and you == "Scissors"):
        print("BOT WIN")
    elif(bot == "Paper" and you == "Rock"):
        print("BOT WIN")
    elif(bot == "Paper" and you == "Scissors"):
        print("YOU WIN")
    elif(bot == "Scissors" and you == "Paper"):
        print("BOT WIN")
    elif(bot == "Scissors" and you == "Rock"):
        print("YOU WIN")



