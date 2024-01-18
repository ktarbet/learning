import csv
import pandas

data = pandas.read_csv('Squirrel_Data.csv')

colorColumnName = 'Primary Fur Color'
allColors = data[colorColumnName]
print(f"number of items in '{colorColumnName}' column: {len(allColors)}")
colors = data[colorColumnName].unique()

count =[]
for c in colors:
    rows = data[data[colorColumnName] == c]
    count.append(len(rows))

color_summary = {
    "Colors": colors,
    "Count": count
}
x = pandas.DataFrame(color_summary)
x.to_csv("summary.csv")

# import statistics
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))  # <class 'pandas.core.frame.DataFrame'>
# # print(data["temp"])
# # print(type(data["temp"])) # <class 'pandas.core.series.Series'>
#
# # data_dict = data.to_dict()
# # print(data_dict)
# # temp_list = data["temp"].tolist()
# # print(temp_list)
# # print(f"average= {statistics.mean(temp_list)}")
# # print(f"pandas  mean = {data['temp'].mean()}")
# # print(f"pandas max  = {data['temp'].max()}")
# #
# # print(data.temp)
# # print(data.condition)
# #
# # # get row..
# #
# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)
# degC = monday.temp
# #
# # °F = (°C * 9/5) + 32`
# degF = degC * 9 / 5 + 32
# print(f" degF = {degF}")
# #
# # row = data[data.temp == data.temp.max()]
# # print(row)
# # print(row)
# # row = data[data.condition == 'Sunny']
# # print(row)
# #
# # x = input("i")
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(data)
# #     temperatures = []
# #     for i, row in enumerate(data):
# #         if i > 0:
# #             temperatures.append(int(row[1]))
# #         print(row)
# #
# #     print(temperatures)
#
#
# # data frame in memory
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "Scores": [76, 56, 65],
# }
# x = pandas.DataFrame(data_dict)
# print(x)
# x.to_csv("/tmp/x.csv")
