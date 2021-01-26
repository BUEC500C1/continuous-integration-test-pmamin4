#===================

#define functions

#===================


def meters_converter(meters, unit):
    
    if unit in "inches":
        return str(meters * 39.37) + " " + unit
    
    elif unit in "feet":
        return str(meters * 3.28) + " " + unit
    
    elif unit in "miles":
        return str(meters * 0.000621) + " " + unit
    
    else:
        return "invalid unit"
    
    
def inches_converter(inches, unit):
    
    if unit in "feet":
        return str(inches / 12) + " " + unit
    
    elif unit in "miles":
        return str(inches * 0.000189 / 12) + " " + unit
    
    elif unit in "meters":
        return str(inches * 0.0254) + " " + unit    
    
    else:
        return "invalid unit"
    
def feet_converter(feet,unit):
    
    if unit in "inches":
        return str(feet * 12) + " " + unit
    
    elif unit in "miles":
        return str(feet * 0.000189) + " " + unit
    
    elif unit in "meters":
        return str(feet / 3.28) + " " + unit    
    
    else:
        return "invalid unit"
    
def miles_converter(miles, unit):
    
    if unit in "inches":
        return str((miles * 12) / 0.000189) + " " + unit
    
    elif unit in "feet":
        return str(miles / 0.000189) + " " + unit
    
    elif unit in "meters":
        return str(miles / 0.000621) + " " + unit   
    
    else:
        return "invalid unit"   
    
def distance_convert(distance, unit1, unit2):
    
    if unit1 in "meters":
        return meters_converter(distance, unit2)
    
    elif unit1 in "feet":
        return feet_converter(distance, unit2)
    
    elif unit1 in "miles":
        return miles_converter(distance, unit2)
    elif unit1 in "meters":
        return meters_converter(distance,unit2)
    else:
        return "invalid unit"
    
    
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

    elif unit1 in "pounds" and unit2 in "ounces":
        return str(weight / 0.0625) + " " + unit2
    else:
        return "invalid unit"


def temp_converter(temp, unit1, unit2):

    if unit1 in "celsius":
        return str(temp) + " " + unit1 + " = " + str((temp * 1.8) + 32) + " " + unit2

    else:
        return str(temp) + " " + unit1 + " = " + str((temp - 32)/1.8) + " " + unit2
