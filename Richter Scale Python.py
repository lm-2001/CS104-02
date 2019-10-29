#Python Richter Scale Calculation
#Your first and last name: Lyah Morales
#Your ID: s1292359

#Algorithm:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
# display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)
#ask the user if they want to enter another value

# test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6


over =False 
while over != True:
    richter= float(input('Enter the richter scale value: '))
    if richter >=8:
        print("Most structures fall")
        over=True
    elif richter >=7:
        print("Many buildings destroyed")
        over=True
    elif richter >=6:
        print("Many buildings considerably damaged, some collapse")
        over=True
    elif richter >=4.5:
        print("Damage to poorly constructed buildings")
        over=True
    elif richter <=0 and richter!=-99:
        print("Value must be greater than 0")
    elif richter==-99:
        print("You've ended the program")
        break
   


       
                 
                 

         
          
