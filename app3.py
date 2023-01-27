def temperature_check(temperature, unit):
    if unit == 'C':
        if temperature < 35:
            print("3")
        elif temperature > 38:
            print("4")
        else:
            print("5")
