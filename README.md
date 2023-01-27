# ECSE3038 LAB 1
Aaron Samuel 
620141792

# Question 1
Purpose:
This function outputs the effective resistance of a network of 2 or more resistors connected in parallel.

Explanation:
A parallel circuit requires at least two resistors. The fucntion checks first to see if the list has fewer than two items and returns an error notice if it does. 
If there are two or more resistors, the function uses a for loop to compute and total the reciprocal of each resistance value. 
for i in resistor_values:
            total_resistance += 1/i
//in this example, 'i' represents the actual value in the array.
Finally, it computes and returns the reciprocal of the sum of the reciprocals to determine the parallel circuit's overall resistance.
The final output is then displayed.

# Question 2
Purpose:
Ttakes two values as argument, a number that represents a voltage supply value and a list of numbers that represent resistance values of resistors connected in series.


Explanation:
The function determines whether the list has fewer than two items and provides an error message if it does.

If there are two or more resistors, the function employs a for loop to compute the overall resistance of the circuit by adding the resistance values. 
total_resistance = 0
        for i in resistor_values:
            total_resistance += i

The voltage drop across each resistor is then calculated using the formula Voltage drop across each resistor = Resistor value * voltage supply value / total resistance. 
print((j * voltage / total_resistance), "V")

It then gives a list of voltage drops across each resistor.
The function displays both the raw result and the result as requested.

# Question 3
Purpose:
This function accepts a single number, a patient's body temperature, and a single character, the unit of temperature.

Explanation:
It first determines whether the temperature unit is 'C,' and if the temperature is less than 35 degrees Celsius, it is hypothermic; 
if temperature < 35 and temperature != 0:
            print("the patient is hypothermic")

if the temperature is greater than 38 degrees Celsius, it is hyperthermic; and if the temperature is between 35 and 38 degrees Celsius, it is normal. 

If the temperature unit is 'F,' and the temperature is less than 95 degrees Fahrenheit, it is hypothermic; if the temperature is greater than 104 degrees Fahrenheit, it is hyperthermic; and if the temperature is between 95 and 104 degrees Fahrenheit, it is normal. 

If the temperature unit is not 'C' or 'F,' an error notice will be printed. 
It displays the proper message on the screen.