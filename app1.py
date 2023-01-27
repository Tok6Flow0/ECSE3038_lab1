from unittest import result


def parallel(resistor_values):
    if len(resistor_values) < 2:
        return "Client Side Error: At least 2 resistors are required."
    else:
        total_resistance = 0
        for i in resistor_values:
            total_resistance += 1/i
        return 1/total_resistance

#-- An example on how to enter 3 resistor values below. Using : 100Ω , 330Ω, 1kΩ.
result = parallel([100,330,1000])
#-- 

print(result, "Ω")