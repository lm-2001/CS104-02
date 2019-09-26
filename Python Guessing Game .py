import random
theComputerNumber =(random.randint(1,1000000))
#Comments start with#
print (theComputerNumber)

numberOfGuesses=0
lowGuessRange=1
highGuessRange=1000000
gameOver=False 

while not gameOver:
    print ("Enter a guess between",lowGuessRange, "to", highGuessRange)
    guess = int(input("Enter a guess: "))
    if (guess<lowGuessRange or guess>highGuessRange):
        print ("Out of range")
    if guess>theComputerNumber:
        print("Guess is too high")
        highGuessRange=guess
        numberOfGuesses=numberOfGuesses+1
    if guess<theComputerNumber:
        print("Guess is too low")
        lowGuessRange=guess
        numberOfGuesses=numberOfGuesses+1
    if guess == theComputerNumber:
        print ("You won")
        gameOver = True
    if numberOfGuesses is 20:
        print("You ran out of guesses")
        gameOver=True
            
    
   
        
        
