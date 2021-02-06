# continuous-integration-test-pmamin4
# Project 1


There are three main python functions. One will be for converting between distances in meters, inches, feet, and miles. The second one will be for converting between weight in kilograms, ounces, and pounds. The third will be for converting between temperatures in degrees Celsius and degrees Fahrenheit.
 
 For converting distances, there are five functions. Four will be for converting from a distance in one individual unit to the equavalent in any of the other units. These will take a number input for the quantity of the unit converted from and a string input for the unit being converted to. The fifth function will take a number input for the quantity of the distance in the first unit, a string input will be the first unit in which the distance will be converted from, and another string input will be the second unit that the distance will be converted to. Based on the inputs for the units, one the other four functions will be called to convert the distance in the first unit to the second unit.
 

For converting weight, there three functions converting weight in one indiviual unit(kilogram, pounds, or ounces) to the other units. There is a main function that will work similar to the distance conversion function by calling the one of the other three functions for converting weight based on the inputs for quantity and units.


Converting between degrees Celsius and degrees Fahrenheit will work similar to the distance and weight conversion functions. There are two functions for individually converting degrees Celsius to degrees Fahrenheit and degrees Fahrenheit to degrees Celsius. The third main function will call one of these two based on the input for quantity (temperature) and first and second units.

There will also tests for all of these functions as well and they will all be tested in continuous build processes. The purpose is to find as many errors as possible and improve the functions as much as possible.
