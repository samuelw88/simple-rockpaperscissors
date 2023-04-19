import random

user_wins = 0
computer_wins = 0

choices = ["R", "P", "S"]

while True:
    user_answer = input("Choose Rock[R], Paper[P], Scissors[S] or Quit[Q]: ").upper()
    if user_answer == "Q":
        break

    if user_answer not in ["R", "P", "S"]:
        continue
        # if input isn't one of those, ends current iteration and moves onto next

    random_num_generator = random.randint(0, 2)
    # rock - 0, paper - 1, scissors - 2
    computer_answer = choices[random_num_generator]
    print("Computer picked", computer_answer)

    if user_answer == "R" and computer_answer == "S":
        print("You win!")
        user_wins += 1
        continue
    elif user_answer == "P" and computer_answer == "R":
        print("You win!")
        user_wins += 1
        continue
    elif user_answer == "S" and computer_answer == "P":
        print("You win!")
        user_wins += 1
        continue
    else:
        print("You Lost!")
        computer_wins += 1

file = open("wins.txt", "r")
currentwins = file.read()
newtotalwins = user_wins + int(currentwins)
file.close()

file = open("wins.txt", "w")
file.write(str(newtotalwins))
file.close

print(f"Your wins in the current game: {user_wins}\nComputer wins in the current game: {computer_wins}")
print(f"Total wins: {newtotalwins}")