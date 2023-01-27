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
            print("%.2f" % (j * voltage / total_resistance), "V")
        return divided_voltage

#-- An example on how to enter 2 resistor values below and a volatage. Using : 9V , 3kΩ, 1kΩ.
result = potential_divider(9, [3000,1000])
#--
print(result, "<-- Raw result in array format")

        