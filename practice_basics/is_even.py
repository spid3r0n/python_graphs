

#defining the function to check if a number is even or not
def is_even(n):
    return n % 2 == 0

#taking input from the user
n = int(input("Enter a number: "))
print(is_even(n))