import pandas

data = pandas.read_csv('day-25/weather_data.csv')

print(data["temp"].median())
print(data["temp"].max())