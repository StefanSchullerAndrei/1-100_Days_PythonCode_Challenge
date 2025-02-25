# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas      #is the go-to library when we have to work with csv data

# data = pandas.read_csv("weather_data.csv")
# print(data)     #The outcome of the print command using panda library is going to be a tabel with indented rows and columns aligned
# print(data["temp"]) #It will be printed only the temp column
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in Columns
# # print(data["condition"])
# # print(data.condition)      #Either method has the same result
#
# #Get Data in Row
# # print(data[data.day == "Monday"])  #to check for the row where the value is equal to the one specified
# # print(data[data.temp == data.temp.max()]) #to access the data with the row that has the criteria specified
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_tempF = monday_temp * 9/5 + 32
# print(monday_tempF)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250225.csv")
# grey_squirrels = data[data["Primary Fur Color"] == "Gray"]   #retrieving data from the column where the color grey is written
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count, red_squirrels_count, black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")