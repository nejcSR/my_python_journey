while True:
    Question1 = input("Which person is also known as liquid snake? (david/eli/george)").lower().strip()
    if Question1 == "eli":
        print("You are correct")
    else:
        print("Wrong, try again")
        retry =input("Try again (yes/no)").lower().strip()
        if retry != "yes":
            break
        else:
            continue
        
    Question2 = input("How did Liquid die? (foxdie/killed in action)" ).lower().strip()
    if Question2 == "foxdie":
        print("right again!")
    else:
        print("close, but no")
        retry = input("do you want to have another go? (yes/no)").lower().strip()
        if retry != "yes":
            break
        else:
            continue
    while True:    
        Question3 = input("lastly, which game did he die in? (metal Gear solid 1/metal gear solid 3/death stranding/metal gear solid rising revengeance)").lower().strip()
        if Question3 =="metal gear solid 1":
            print("You make me proud, correct!")
            break
        elif Question3 =="death stranding":
            print("Wrong Kojima game")
            break
        else:
            Question4 =input("Is that your final answer? (yes/no)")
            if Question4 == "yes":
                print("well you're wrong, sorry")
                break
            else:
                print("Don't mess it up")
            
    again =input("Do you want one more go at it? (yes/no)").lower().strip()
    if again !="yes":
        break
    
