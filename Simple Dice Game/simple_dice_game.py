#Create a Python program that simulates a simple dice game:
# 1. The program should draw two random numbers from 1 to 6.
#   It should follow these rules: 
#   a. If any number other than 1 or 6 is drawn, return the result immediately.
#   b. If 6 occurs twice, draw again and return all results up to 3 times. 
#   c. If 1 occurs twice, draw again and return only the next valid draw (not including double 1's), up to 3 attempts total. 
#   d. If after 3 draws no valid result is obtained, return an empty list.
# 2. Write unit tests for your code.    
# 3. Create a command-line interface that allows the user to specify the number of times to run the simulation.
# 4. Log each run's results to a file.
# 5. Use proper documentation, including docstrings and comments.

import random
import argparse


def roll():
    results = []

    with open("log_file.txt", "a") as log_file: # "with" ensures the file is properly closed

        for attempt in range(3):
            first = random.randint(1, 6)
            second = random.randint(1, 6)
            results.append((first, second))
            
            log_file.write(f"Attempt {attempt + 1}: Roll = [{first}, {second}]\n")

            if first == 1 and second == 1:
                continue

            elif first == 6 and second == 6:
                continue

            log_file.write(f"Result: [{first}, {second}]\n\n")
            return [first, second]

        log_file.write(f"Results: [] \n\n") # return an empty list if no valid result

    return results


def main(number_of_rolls):
    for i in range(number_of_rolls):
        result = roll()
        print(f"Game {i + 1} result: {result}")

# Creating a command-line interface that allows the user to specify the number of times to run the simulation.
#   navigate to the directory
#   run the script
#   python simple-dice-game.py 10 (for Win)
#   python3 simple-dice-game.py 10 (for Mac)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dice roll")
    parser.add_argument("number_of_rolls", type=int, help="How many times should the dice roll? ")

    args = parser.parse_args()

    main(args.number_of_rolls)