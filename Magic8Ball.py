from random import randint

message_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", 
"Outlook: good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", 
"Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no,", "Outlook not so good.", "Very doubtful."]
break1 = False

while True:
    input("Welcome to the programmed version of the Magic 8-Ball. What do you wish to ask?: ")
    print(message_list[randint(0, 19)])
    while True:
        yes_or_no = input("Would you like to try the Magic 8-Ball again?")
        if yes_or_no.strip().lower() == "yes":
            break
        elif yes_or_no.strip().lower() == "no":
            break1 = True
            break
        else:
            print("Try again. Type yes or no please.")
    if break1 is True:
        break
