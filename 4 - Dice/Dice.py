
import random
import matplotlib.pyplot as pl


n = int(input("Please Enter Your Desired Number of Rolling The Dice: "))

counts = [0, 0, 0, 0, 0, 0]

for i in range(n + 1):
    dice = random.randint(1, 6)

    counts[dice - 1] += 1
print(counts)

numbers = [1, 2, 3, 4, 5, 6]

pl.xlabel("Dice Number")
pl.ylabel("Frequency")
pl.title("Dice Simulation with Input Rolls")
pl.xticks(numbers)

pl.bar(numbers, counts)
pl.show()