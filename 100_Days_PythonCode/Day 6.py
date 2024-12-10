## Loops
## for item in list_of_items:
##     do something to each item

## for number in range(a, b):
##     print(number)

## while something_is_true:
#     do something repeatedly

## making a function

# # defining a function -> def name ()
# def test_function():
#     print("Test")
#     print("Learn")

# # call the function or accessing the function
# test_function()

# -----------------------------------------

# Reebord practice - used https://reeborg.ca/ for all the practice exercises below

# def turn_around():
#     turn_left()
#     turn_left()
# move()
# move()
# turn_around()
# move()
# move()
# turn_around()

# # #  EXERCISE NO. 1 - turning draw a square
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# turn_left()
# move()
# move()
# turn_right()
# move()
# move()
# turn_right()
# move()
# move()
# turn_right()
# move()
# move()

# # # EXERCISE NO. 2
# def jumping_fence():
#     move()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#
# number_of_hurdles = 0
# while not at_goal():
#     jumping_fence()
#     number_of_hurdles += 1
#     print(number_of_hurdles)

# # # EXERCISE NO.3
# def jumping_fence():
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#
#
# def smart_robot():
#     def wall_in_front():
#         jumping_fence()
#
#     while front_is_clear() == True:
#         move()
#     while not front_is_clear():
#         wall_in_front()
#
#
# while not at_goal():
#     smart_robot()


#Exercise NO.4

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# def smart_robot():
#     while not at_goal():
#         if wall_in_front():
#             jump()
#         else:
#             move()
#
#
# smart_robot()

#REVISIT DAY 6 PART 50, MIDDLE OF THE VIDEO AFTER I COMPLETED DAY 15 !!!
