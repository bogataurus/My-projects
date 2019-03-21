radiators_list = ["kitchen","livingRoom","diningRoom","bathroom","bedroom1","bedroom2", "bedroom3"]
temperatur_list = [15, 18, 22,  26, 30, 35, 40, 45]

heating_radiator = ""
temperature = "" 

while True:
    radiator_select = input ( "Select radiator at list: kitchen, livingRoom , diningRoom , bathroom , bedroom1 , bedroom2, bedroom3: or quit: " )
    if radiator_select in radiators_list:
        heating_radiator = radiator_select        
        
        while True:            
            temperature_select = int(input("Please enter a temperature at list: 15, 18, 22,  26, 30, 35, 40, 45: "))
            if temperature_select in temperatur_list:
                temperature = temperature_select
                print("Radiator Type: ",heating_radiator , ";", "Temperature: ", temperature)
                break            
            else:
                print("Invalid input! Please enter a temperature at list")   
            
    elif radiator_select.startswith ( "q" ):
        print("exit!")
        break    
    else:
        print("Invalid input! Please select radiator at list")
    
          
