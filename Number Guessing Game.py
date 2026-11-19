#number guessing game
secret=10
guess=int(input("Guess the number: "))
max_lives=5

while guess!=secret:
    print("Guess Again! Wrong answer")
    if guess > 20:
        print("Ice cold!!")
    elif guess > 15:
        print("Cold...")
    elif guess >= 8:
        print("Hot!!!")
    else:
        print("Warm...")
    max_lives -= 1
    print("❤️ " * max_lives)
    print() 

    if guess!=secret:
        guess=int(input("Guess the number: "))
        if guess != secret:
            print("Guess Again! Wrong answer")
            
            if guess > 20:
                print("Ice cold!!")
            elif guess > 15:
                print("Cold...")
            elif guess >= 8:
                print("Hot!!!")
            else:
                print("Warm...")
            max_lives -= 1
            print("❤️ " * max_lives)
            print()  
            
    if guess!=secret:
        guess=int(input("Guess the number: "))
        if guess != secret:
            print("Guess Again! Wrong answer")
            
            if guess > 20:
                print("Ice cold!!")
            elif guess > 15:
                print("Cold...")
            elif guess >= 8:
                print("Hot!!!")
            else:
                print("Warm...")
            max_lives -= 1
            print("❤️ " * max_lives)
            print()  
                
    if guess!=secret:
        guess=int(input("Guess the number: "))
        if guess != secret:
            print("Guess Again! Wrong answer")
            
            if guess > 20:
                print("Ice cold!!")
            elif guess > 15:
                print("Cold...")
            elif guess >= 8:
                print("Hot!!!")
            else:
                print("Warm...")
            max_lives -= 1
            print("❤️ " * max_lives)
            print()  
                
    if guess!=secret:
        guess=int(input("Guess the number: "))
        print("Guess Again! Wrong answer")
        if guess > 20:
            print("Ice cold!!")
        elif guess > 15:
            print("Cold...")
        elif guess >= 8:
            print("Hot!!!")
        else:
            print("Warm...")
        max_lives -= 1
        print("❤️ " * max_lives)
        print()  
  
    if max_lives==0:
        break
if guess!=secret:
    print("Sorry ! 5 wrong attempts. Attempts Finished.Try again! Better luck next time!!!")
    print("The secret number was 10.")
elif guess==secret:
    print("Congratulations!! You have correctly guessed the secret or missing number...")