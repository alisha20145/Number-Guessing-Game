#number guessing game
secret=10
guess=int(input("Guess the number: "))
difference=guess-secret

while guess!=secret:
    print("Guess Again! Wrong answer")
    guess2=int(input("Guess the number: "))
    if guess2!=secret:
        print("Guess Again! Wrong answer")
        guess3=int(input("Guess the number: "))
    if guess3!=secret:
        print("Guess Again! Wrong answer")
        guess4=int(input("Guess the number: "))
    if guess4!=secret:
        print("Guess Again! Wrong answer")
        guess5=int(input("Guess the number: "))
    if guess5!=secret:
        print("Sorry ! 5 wrong attempts. Attempts Finished.Try again! Better luck next time!!!")
    elif guess or guess2 or guess3 or guess4 or guess5==secret:
        print("Congratulations!! You have correctly guessed the secret or missing number...")
    elif guess or guess2 or guess3 or guess4 or guess5!=secret:
        print("The secret number waas 10.")
    break


if difference>guess:
    print("Ice cold")
else:
    print("Hot")