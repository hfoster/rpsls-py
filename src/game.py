import random

user_wins = 0
cpu_wins = 0

options = ["rock", "paper", "scissors", "lizard", "spock"]

while True:
    user_pick = input("Choose (rock, paper, scissors, lizard, spock) or q to quit: ").lower()
    if user_pick == "q":
        break
    
    if user_pick not in options:
        continue

    random_number = random.randint(0, 4)
    cpu_pick = options[random_number]
    print("User picked", user_pick + "; CPU picked", cpu_pick)

    if user_pick == options[0] and cpu_pick == options[2]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == options[0] and cpu_pick == options[3]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == options[1] and cpu_pick == options[0]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == options[1] and cpu_pick == options[4]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == options[2] and cpu_pick == options[1]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == options[2] and cpu_pick == options[3]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == options[3] and cpu_pick == options[1]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == options[3] and cpu_pick == options[4]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == options[4] and cpu_pick == options[0]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == options[4] and cpu_pick == options[2]:
        print(user_pick, "defeats", cpu_pick + "! You win!")
        user_wins += 1
    elif user_pick == cpu_pick:
        print(user_pick, "ties", cpu_pick + "!")
        cpu_wins += 1
        user_wins += 1
    else:
        print(cpu_pick, "defeats", user_pick + "! You lose!")
        cpu_wins += 1

print("CPU won", cpu_wins, "times.")
print("User won", user_wins, "times.")
print("Goodbye!")
