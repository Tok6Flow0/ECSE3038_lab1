def potential_divider(voltage, resistor_values):
    if len(resistor_values) < 2:
        return "Error: At least 2 resistors are required."
    else:
        total_resistance = 0
        for i in resistor_values:
            total_resistance += i
        #creating an empty array
        