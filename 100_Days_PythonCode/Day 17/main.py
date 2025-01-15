class User:
    def __init__(self, user_id, username):
        # print("new user being created...") # will be printed everytime the constructor is called
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#
# my_car = Car(5) # creating an object by calling the name of the class and then adding the parenthesis to set the atributes for that object.
# # It's exactly the same as: my_car.seats = 5

user_1 = User("001", "nicu") #with the constructor we can add values
user_2 = User("002", "petru")
print(user_1.followers)
print(user_1.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)