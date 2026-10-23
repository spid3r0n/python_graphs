# ==========================================
# Lab session N° 1
# ==========================================

import math
import random
import numpy as np


# ------------------------------------------
# 1. Variables and Output
# ------------------------------------------

# 1.1. Variable Types
x = 4
y = 5.5
a = "Hello"
b = "Hiii"

# 1.2. Operations on Variables
print("--- 1.2 Operations on Variables ---")
print(x + y)
print(y - x)
print((x * 10) / y)
print(2**3)
print(5 % 4)
print(8 % 4)

# 1.3. Operations on Strings
print("\n--- 1.3 Operations on Strings ---")
chaine = "salut"
print(chaine + " python")
print(chaine * 3)
print("2" + "3")

# 1.4. The type() Function
print("\n--- 1.4 The type() Function ---")
x = 3
print(type(x))
y = 6.1
print(type(y))
z = "12"
print(type(z))
del x

# 1.5. Output
print("\n--- 1.5 Output ---")
x = 19
name = "Ahmed"
print(name, "is", x)
print(x == 20)
# N = int(input('Enter the value you want: ')) # Décommentez pour exécuter l'interaction utilisateur


# ------------------------------------------
# 2. Lists
# ------------------------------------------
print("\n--- 2. Lists ---")
animaux = ["girafe", "tigre", "singe", "souris"]
Tailles = [5, 2.5, 1.75, 0.15]
miste = ["girafe", 5, "souris", 0.15]
print(animaux[0])

# 2.1. Operations on lists
ani1 = ["girafe", "tigre"]
ani2 = ["singe", "souris"]
print(ani1 + ani2)
print(ani1 * 3)

a = []  # créer une liste vide
a = a + [15]
a.append(6)
a = a + [-5]
print("a:", a)

b = [1, 2, 3, 4, 5]
b.remove(5)
print("b:", b)

# 2.2. Slicing
print("\n--- 2.2 Slicing ---")
animaux = ["girafe", "tigre", "singe", "souris"]
print(animaux[0:2])
print(animaux[2:])


# ------------------------------------------
# 3. Functions
# ------------------------------------------

# 3.1. len() function
print("\n--- 3.1 len() function ---")
animaux = ["girafe", "tigre", "singe", "souris"]
print(len(animaux))

# 3.2. range() and list() function
print("\n--- 3.2 range() and list() function ---")
print(list(range(10)))
print(list(range(3, 16)))
print(list(range(0, 100, 10)))


# ------------------------------------------
# 4. Loops and Comparisons
# ------------------------------------------

# 4.1. Loops
print("\n--- 4.1 Loops ---")
for i in range(4):
    print(i)

animaux = ["girafe", "tigre", "singe", "souris"]
for animal in animaux:
    print(animal)

for i in range(len(animaux)):
    print(animaux[i])

# 4.2. Comparisons
print("\n--- 4.2 Comparisons ---")
x = 4
print(x == 4)
print(x > 10)
print(x < 6)
print(x != 6)

# 4.3. While Loop
print("\n--- 4.3 While Loop ---")
i = 1
while i <= 4:
    print(i)
    i = i + 1


# ------------------------------------------
# 5. Tests
# ------------------------------------------

# 5.1. Single-Case Test
print("\n--- 5.1 Single-Case Test ---")
x = 9
if x == 2:
    print("Le test est vrai !")

y = "souris"
if y == "tigre":
    print("Le test est vrai !")

# 5.2. Multiple-Case Test
print("\n--- 5.2 Multiple-Case Test ---")
x = 2
if x == 2:
    print("Le test est vrai !")
else:
    print("Le test est faux !")

base = random.choice(["a", "t", "c"])
if base == "a":
    print("choix 1")
elif base == "t":
    print("choix 2")
elif base == "c":
    print("choix 3")

# 5.3. Multiple Test
print("\n--- 5.3 Multiple Test ---")
x = 2
y = 2
if x == 2 and y == 2:
    print("le test est vrai")

if x == 2:
    if y == 2:
        print("Le test est vrai")

# 5.4. The break and continue Statements
print("\n--- 5.4 break and continue ---")
for i in range(5):
    if i > 2:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)


# ------------------------------------------
# 6. Reading from a File
# ------------------------------------------
print("\n--- 6. Reading from a File ---")

# Création préalable du fichier zoo.txt pour tester la lecture sans erreur
with open("zoo.txt", "w") as f:
    f.write("Girafe\nTigre\nSinge\nSouris\n")

filin = open("zoo.txt", "r")
print(filin)
print(filin.readlines())
filin.close()

# tentative de relecture sur fichier fermé (illustrée dans le TP)
try:
    print(filin.readlines())
except ValueError as e:
    print("Fichier fermé, réouverture nécessaire :", e)

filin = open("zoo.txt", "r")
lignes = filin.readlines()
print(lignes)
filin.close()

filin = open("zoo.txt", "r")
# print(filin.read())
for ligne in lignes:
    print(ligne)
filin.close()


# ------------------------------------------
# 7. Writing to a File
# ------------------------------------------
print("\n--- 7. Writing to a File ---")
animaux2 = ["poisson", "abeille", "chat"]
filout = open("zoo2.txt", "w")
for animal in animaux2:
    filout.write(animal + "\n")
filout.close()


# ------------------------------------------
# 8. Functions
# ------------------------------------------
print("\n--- 8. Functions ---")

x = math.cos(2 * math.pi)
print(x)


def carre(x):
    return x**2


print(carre(2))


def produit(x, y):
    return x * y


print(produit(2, 3))
print(produit("to", 2))


def abs_val(x):
    if x >= 0:
        return x
    else:
        return -x


print("Valeur absolue de -5:", abs_val(-5))


# ------------------------------------------
# 9. NumPy Arrays
# ------------------------------------------
print("\n--- 9. NumPy Arrays ---")

# 9.1. Vectors
print(np.zeros(10))
print(np.ones(10))
print(np.arange(10))
print(np.array([1, 2, 3, 4, 5]))

# 9.2. Functions
x = np.array([10, 2, 2, 3, 4, 123, 3])
x.sort()
print("Trie :", x)
print("Somme :", x.sum())
print("Variance :", x.var())
print("Écart-type :", x.std())
print("Max :", x.max())
print("Min :", x.min())