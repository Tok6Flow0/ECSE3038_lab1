def temperature_check(temperature, unit):
    if unit == 'C':
        if temperature < 35 and temperature != 0:
            print("the patient is hypothermic")
        elif temperature > 38:
            print("the patient is hyperthermic")
        elif temperature == 0:
            print("You are not measuring a patient, but in fact an ice block. You are measuring an ice block")
        else:
            print("The patient's temperature is normal")
    elif unit == 'F':
        if temperature < 95 and temperature != 32:
            print("the patient is hypothermic")
        elif temperature > 104:
            print("the patient is hyperthermic")
        elif temperature == 32:
            print("changing the temperature to Fahrenheit does not change the fact that you are measuring an ice block")
        else:
            print("the patient's temperature is normal")
    else:
        print("please enter 'C' for Celcius OR 'F' for Fahrenheit")

temperature_check(0, 'C')