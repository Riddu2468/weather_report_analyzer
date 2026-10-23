days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temperature_data = []
rainfall_data = []
for  day in days:
    temperature = float(input(f"Enter the temperature for {day}:"))
    rainfall= float(input(f"enter the rainfall for{day}: "))
    temperature_data.append(temperature)
    rainfall_data.append(rainfall) 


average_temperature= sum(temperature_data)/len(temperature_data)
print(f"Average temperature for the week is: {average_temperature:.2f}°C")
highest_temperature= max(temperature_data)
index= temperature_data.index(highest_temperature)
print(f"The highest temperature for the week is: {highest_temperature:.2f}°C")
print(f"Day with the highest temperature: {days[index]}")

lowest_temperature= min(temperature_data)
index= temperature_data.index(lowest_temperature)
print(f"The lowest temperature for the week is: {lowest_temperature:.2f}°C")
print(f"Day with the lowest temperature: {days[index]}")
total_rainfall=sum(rainfall_data)
print("total rainfall this week:", total_rainfall)
index=rainfall_data.index(max(rainfall_data))
print(f"Day with the highest rainfall: {days[index]} with {max(rainfall_data)}mm")
index=rainfall_data.index(min(rainfall_data))
print(f"Day with the lowest rainfall: {days[index]} with {min(rainfall_data)}mm")
temperature_range = max(temperature_data) - min(temperature_data)
print("Temperature range:", temperature_range, "°C")
rainfall_day_count=0
for rainfall in rainfall_data:
    if rainfall>0:
        rainfall_day_count+=1
print("Number of days with rainfall:", rainfall_day_count)