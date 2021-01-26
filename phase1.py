
## define functions

def meters_converter(meters, unit1):
    
    if unit1 in "inches":
        return str(meters * 39.37) + " " + unit1
    
    elif unit1 in "feet":
        return str(meters * 3.28) + " " + unit1
    
    else:
        return str(meters * 0.000621) + " " + unit1
    
def inches_converter(inches, unit1):
    
    if unit1 in "feet":
        return str(inches / 12) + " " + unit1
    
    elif unit1 in "miles":
        return str(inches * 0.000189 / 12) + " " + unit1
    
    else:
        return str(inches * 0.0254) + " " + unit1    
    
def feet_converter(feet,unit1):
    
    if unit1 in "inches":
        return str(feet * 12) + " " + unit1
    
    elif unit1 in "miles":
        return str(feet * 0.000189) + " " + unit1
    
    else:
        return str(feet / 3.28) + " " + unit1    
    
    
def miles_converter(miles, unit1):
    
    if unit1 in "inches":
        return str((miles * 12) / 0.000189) + " " + unit1
    
    elif unit1 in "feet":
        return str(miles / 0.000189) + " " + unit1
    
    else:
        return str(miles / 0.000621) + " " + unit1    
    
    
def weight_converter(weight, unit1, unit2):

    if unit1 in "kilograms" and unit2 in "ounces":
        return str(weight * 35.274) + " " + unit2

    elif unit1 in "kilograms" and unit2 in "pounds":
        return str(weight * 2.20462) + " " + unit2

    elif unit1 in "ounces" and unit2 in "kilograms":
        return str(weight / 35.274) + " " + unit2

    elif unit1 in "ounces" and unit2 in "pounds":
        return str(weight * 0.0625) + " " + unit2

    elif unit1 in "pounds" and unit2 in "kilograms":
        return str(weight / 2.20462) + " " + unit2

    else:
        return str(weight / 0.0625) + " " + unit2


def temp_converter(temp, unit1, unit2):

    if unit1 in "celsius":
        return str(temp) + " " + unit1 + " = " + str((temp * 1.8) + 32) + " " + unit2

    else:
        return str(temp) + " " + unit1 + " = " + str((temp - 32)/1.8) + " " + unit2
