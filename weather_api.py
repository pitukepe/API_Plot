import requests
from datetime import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt

###GETTING DATA FROM API
api = requests.get("https://api.open-meteo.com/v1/forecast?latitude=48.1482&longitude=17.1067&hourly=temperature_2m,rain,wind_speed_10m&timezone=Europe%2FBerlin")
time_data = [datetime.strptime(x,"%Y-%m-%dT%H:%M").strftime('%d.%B. - %H:%M') for x in api.json()['hourly']['time']]
master_data = list(zip(time_data, api.json()['hourly']['temperature_2m'], api.json()['hourly']['rain'], api.json()['hourly']['wind_speed_10m']))

###PRINTING DATA FOR SPECIFIC DAY
#print("Temperature for today:")
#for x in master_data[0:24]:
#    print(f"Day: {x[0]} - Temperature: {x[1]}°C - Rain: {x[2]}mm - Wind: {x[3]}m/h")

###WRITING DATA TO CSV FILE
with open('weather_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Time', 'Temperature', 'Rain', 'Wind'])
    writer.writerows(master_data)

###PLOTTING DATA
plot_data = pd.read_csv('weather_data.csv')
plot_data['Temperature'].plot(kind='line', title='Temperature', color='red', figsize=(15,6))
plot_data['Rain'].plot(kind='line', title='Rain', color='blue')
plot_data['Wind'].plot(kind='line', title='Wind', color='green')

###SETTING TICK MARKS
plt.xticks(range(1, len(plot_data['Temperature']), 24), rotation=45)
current_ticks = plt.xticks()[0]
new_ticks = list(current_ticks)+[35,112]
plt.xticks(new_ticks, rotation=45)

###SETTING TITLE, MAXIMUM VALUE LINES, LEGEND AND LABELS
plt.title('Weather Data')
plt.axvline(x=plot_data.loc[plot_data['Temperature']==plot_data['Temperature'].max()].index, color='red', linestyle='--', label='Max Temperature')
plt.axvline(x=plot_data.loc[plot_data['Wind']==plot_data['Wind'].max()].index, color='green', linestyle=':', label='Max Wind')
plt.legend(loc='upper right')
plt.xlabel('Time')

###SHOWING PLOT
plt.show()