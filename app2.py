def potential_divider(voltage, resistor_values):
    if len(resistor_values) < 2:
        return "Error: At least 2 resistors are required."
    else:
        total_resistance = 0
        for i in resistor_values:
            total_resistance += i

        #creating an empty array
        divided_voltage = []
        for j in resistor_values:
            #assigning values to empty array using append operation in python
            divided_voltage.append(j * voltage / total_resistance)
            divided_voltage.append("V")
        return divided_voltage

result = potential_divider(5, [100,330])

print(result)

        