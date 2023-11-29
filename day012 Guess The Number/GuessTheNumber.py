#Step 0 - Number Generator
#Randomly draw a number between 1 and 100

#Step 1 - Greeting
#Call ASCII Logo
#"Welcome to the Number Guessing Game!"
#"I'm thinking of a number between 1 and 100."
#Let's player choose "easy" or "hard"
#"Choose a difficulty. Type 'easy' or 'hard': easy"

#Step 2 - Hard & easy
#easy: 10 attempts
#hard: 5 attempts

#Step 3 - Attempts counter
#If answer is wrong attempts -1
#"You have x attempts remaining to guess the number."
#"You've run out of guesses, you lose" GAME OVER

#Step 4 - Number checker
#Respond "Too high" or "Too low"

#Step 5 - run again

import os
from subprocess import call
import random
import logoGTN

def number_checker():
	if answer < number:
		print("Too low")
	elif answer > number:
		print("Too high")
	elif answer == number:
		print(f"You got it! The answer was {number}")


def attempts_counter():
	return token


def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

#Game start
number = random.randint(1, 100)
token = 0

print(logoGTN.logo)
print(f"The answer is {number}")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
	token = 10
elif difficulty == "hard":
	token = 5
else:
	print("Bye")


while token != 0:
	answer = int(input("Make a guess: "))

	number_checker()

	if answer != number:
		token -= 1
		print(f"You have {token} attempts remaining to guess the number.")
		if answer == number:
			play_again = input("Do you want to play again? Type 'yes' or 'no': ")
			if play_again == "yes":
				clear()
				print("I'm thinking of a number between 1 and 100.")
				difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
				if difficulty == "easy":
					token = 10
				elif difficulty == "hard":
					token = 5
				else:
					print("Bye")

			else:
				print("Thank you for your playing")
		elif token == 0:
			print("You've run out of guesses, you lose")
			print("Game Over")
			play_again = input("Do you want to play again?")
			if play_again == "yes":
				clear()
				print("I'm thinking of a number between 1 and 100.")
				difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
				if difficulty == "easy":
					token = 10
				elif difficulty == "hard":
					token = 5
				else:
					print("Bye")


			else:
				print("Thank you for your playing")
				

















#How to clean terminal screen
#https://www.geeksforgeeks.org/clear-screen-python/
#要做返notes落EN
# import os

# # import call method from subprocess module
# from subprocess import call
  
# # import sleep to show output for some time period
# from time import sleep
  
# # define clear function
# def clear():
#     # check and make call for specific operating system
#     _ = call('clear' if os.name =='posix' else 'cls')
  
# print('hello geeks\n'*10)
  
# # sleep for 2 seconds after printing output
# sleep(2)
  
# # now call function we defined above
# clear()