""" The Number Guessing Game
if the player's guess is higher than the actual number,the program displays "Lower number please"
similarly the player's number is lower than the acutal number. then program displays "Higher number please"
When the player guess the correct number,then program displaysthe number of guesses the user used to arrive 
at the number
by using the random module"""

"""This is a number guessing game, built by Ananth Shetty in python. where user has to guess the number and
 program will give random number. If both user and program number is same the user wins or else program will wins.
  """


import random 
c = random.randint(1,10)

guesses = 0
user_guess = None
max_lim = 4
limit = 1
while user_guess!=c:
    if limit<=max_lim:
        user_guess = int(input(f"Guess number between 1 to 10\nYou are left with {max_lim-guesses} Guesses\n"))
        guesses+=1
        if user_guess==c:
            print(f"Great! you guessed the correct number {c}, in {guesses} guesses")
        else:
            if user_guess>c:
                print(("Guessed greater number!"))
            elif user_guess<c:
                print(("Guessed lower number!"))
    
        limit+=1
    else:
        print(f"Better luck next time,\nCorrect number is {c}")    
        break
with open("C:\\Users\\91967\\Desktop\\codeisfun\\Learnings\\1_python\\My_completed_Projects\\2_Number_guessing_game\\High_score.txt",'r') as r:
    R = r.read()
    if guesses<int(R):
        with open("C:\\Users\\91967\\Desktop\\codeisfun\\Learnings\\1_python\\My_completed_Projects\\2_Number_guessing_game\\High_score.txt",'w') as w:
            w.write(str(guesses))