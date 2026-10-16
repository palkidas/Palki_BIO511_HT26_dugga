#Question 1:

# AI not used :)

my_name = "Palki Das"

#length of my_name
print(len(my_name))

#number of times letter 's' occurs
print(my_name.count("s"))

###########################################################


#Question 2:  (with AI)

my_list = [1, 5, "4", "six", 3.14]


#a)

#converting each item to an int and adding to new_list
new_list = []

#if an error occurs here, the program won't crash :)
for item in my_list:
    try:
        new_list.append(int(item))
    except ValueError:
        print(f"Could not convert '{item}' to an integer.")

print(new_list)



#b)
#extracts the valid integers, skips the text, removes the decimal part, and prints message

def clean_list(my_list):
    new_list = []

    for item in my_list:
        try:
            new_list.append(int(item))
        except ValueError:
            print(f"'{item}' cannot be converted to an integer")

    return new_list

my_list = [1, 5, "4", "six", 3.14]
new_list = clean_list(my_list)

print(new_list)



#c)
#calculates the sum of every neighboring pair of numbers

neighbor_sums = []

for i in range(len(new_list) - 1):
    neighbor_sums.append(new_list[i] + new_list[i + 1])

print(neighbor_sums)

##########################################################


#Question 3: (with AI)

#a)
#genetate a scatter plot

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("cnv_data.csv")

# Create scatter plot
plt.scatter(df["position_mb"], df["log2_ratio"])

plt.xlabel("position_mb")
plt.ylabel("log2_ratio")
plt.title("CNV Data")

plt.show()



#b)
# Save the plot as .png file

plt.savefig("cnv_plot.png")



#c)
#user can define the names of input and output files

import pandas as pd
import matplotlib.pyplot as plt

input_file = input("Enter input CSV file: ")
output_file = input("Enter output plot name: ")

df = pd.read_csv(input_file)

plt.scatter(df["position_mb"], df["log2_ratio"])

plt.xlabel("position_mb")
plt.ylabel("log2_ratio")
plt.title("CNV Data")

plt.savefig("cnv_plot.png")

####################################################

#Question 4:(with AI)

#a)

import random

results = {}

for game in range(1, 21): #Loops exactly 21 times and Generates a random whole number between 1 and 6 for both Alice and Bob.
    alice = random.randint(1, 6)
    bob = random.randint(1, 6)

    if alice > bob:
        results[game] = "Alice won"
    elif bob > alice:
        results[game] = "Bob won"
    else:
        results[game] = "Draw"

print(results)

#Because the code uses random numbers, the output will change every single time you run it.


#b)

import random

def play_games(player1, player2, n_games):
    results = {}

    for game in range(1, n_games + 1):
        score1 = random.randint(1, 6)
        score2 = random.randint(1, 6)

        if score1 > score2:
            results[game] = f"{player1} won"
        elif score2 > score1:
            results[game] = f"{player2} won"
        else:
            results[game] = "Draw"

    return results


results = play_games("Alice", "Bob", 20)
print(results)
