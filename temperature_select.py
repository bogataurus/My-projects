temperature = input("Please enter a temperature  between 15  to 60: ")

temperature_list = temperature.split()

heating_radiator = 0

for value in temperature_list:
    if int(value) > 60:
        heating_radiator = 60
    elif int(value) < 15:
        heating_radiator = 15        
    elif int(value) + 15 <= 60:
        heating_radiator = value
    elif int(value) + 15 >= 60:
        heating_radiator = int(value) +15 -15
    else:
        pass
    print(heating_radiator)