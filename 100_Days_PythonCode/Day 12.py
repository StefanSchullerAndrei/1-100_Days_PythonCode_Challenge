game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)

""" 
Prime numbers are numbers that can only be cleanly divided by themselves and 1. 

You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.

e.g.

7 is a primer number because it is only divisible by 1 and itself.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1."""
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False

    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True

is_prime(101)

#--------------------------------------------------------------------

# Modifying Global Scope

enemies = 1

def increase_enemies(enemy):
    """in order to modify a variable outside of function, we call "global <variable>"""
    # global enemies
    # enemies += 1

    print(f"Enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"Enemies outside function: {enemies}")