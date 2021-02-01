#===================

#define functions

#===================

''' Each function takes one input as float or int
    which is the amounts of units and the "unit"
    inputs would be strings.
'''

'''The first four functions individually convert
   "inches, "meters", "feet", and "miles" as floats/ints
   to a different "unit" taken as string inputs. The kilo, ounce,
   pound, celsius, and fahrenheit convert functions work the same.
'''

def meters_converter(meters, unit):

    inch = ["inches", "in"]
    feet = ["feet", "ft"]
    mile = ["miles", "mi"]

    if unit in inch and isinstance(meters, (int, float)):
        return str(round(meters * 39.37)) + " " + unit

    elif unit in feet and isinstance(meters, (int, float)):
        return str(round(meters * 3.28)) + " " + unit

    elif unit in mile and isinstance(meters, (int, float)):
        return str(round(meters * 0.000621)) + " " + unit
    else:
        return "invalid unit/number"


def inches_converter(inches, unit):

    feet = ["feet", "ft"]
    mile = ["miles", "mi"]
    meter = ["meters", "m"]

    if unit in feet and isinstance(inches, (int, float)):
        return str(round(inches / 12)) + " " + unit

    elif unit in mile and isinstance(inches, (int, float)):
        return str(round(inches * 0.000189 / 12)) + " " + unit

    elif unit in meter and isinstance(inches, (int, float)):
        return str(round(inches * 0.0254)) + " " + unit

    else:
        return "invalid unit/number"


def feet_converter(feet, unit):

    inch = ["inches", "in"]
    mile = ["miles", "mi"]
    meter = ["meters", "m"]

    if unit in inch and isinstance(feet, (int, float)):
        return str(round(feet * 12)) + " " + unit

    elif unit in mile and isinstance(feet, (int, float)):
        return str(round(feet * 0.000189)) + " " + unit

    elif unit in meter and isinstance(feet, (int, float)):
        return str(round(feet / 3.28)) + " " + unit

    else:
        return "invalid unit/number"


def miles_converter(miles, unit):
    inch = ["inches", "in"]
    feet = ["feet", "ft"]
    meter = ["meters", "m"]

    if unit in inch and isinstance(miles, (int, float)):
        return str(round((miles * 12) / 0.000189)) + " " + unit

    elif unit in feet and isinstance(miles, (int, float)):
        return str(round(miles / 0.000189)) + " " + unit

    elif unit in meter and isinstance(miles, (int, float)):
        return str(round(miles / 0.000621)) + " " + unit

    else:
        return "invalid unit/number"


''' distance_convert takes distance as a float/int and  
    converts from one unit "unit1" to a different unit "unit2".
    Weight_converter and temp_converter work the same way.
'''

def distance_convert(distance, unit1, unit2):
    
    inch = ["inches", "in"]
    feet = ["feet", "ft"]
    mile = ["miles", "mi"]
    meter = ["meters", "m"]

    if unit1 in meter and isinstance(distance, (float, int)):
        return meters_converter(distance, unit2)

    elif unit1 in feet and isinstance(distance, (float, int)):
        return feet_converter(distance, unit2)

    elif unit1 in mile and isinstance(distance, (float, int)):
        return miles_converter(distance, unit2)

    elif unit1 in inch and isinstance(distance, (float, int)):
        return inches_converter(distance, unit2)
    else:
        return "invalid unit/number"


def kilo_converter(kilo, unit):

    ounce = ["ounces", "ounce", "oz"]
    pound = ["pounds", "lb"]

    if unit in ounce and isinstance(kilo, (float, int)):
        return str(round(kilo * 35.274)) + " " + unit

    elif unit in pound and isinstance(kilo, (float, int)):
        return str(round(kilo * 2.20462)) + " " + unit

    else:
        return "invalid unit/number"


def ounce_converter(ounce, unit):

    kilo = ["kilograms", "kilo", "kilos", "k"]
    pound = ["pounds", "lb"]

    if unit in kilo and isinstance(ounce, (float, int)):
        return str(round(ounce / 35.274)) + " " + unit

    elif unit in pound and isinstance(ounce, (float, int)):
        return str(round(ounce * 0.0625)) + " " + unit

    else:
        return "invalid unit/number"


def pound_converter(pound, unit):

    kilo = ["kilograms", "kilo", "kilos", "k"]
    ounce = ["ounces", "ounce", "oz"]

    if unit in kilo and isinstance(pound, (float, int)):
        return str(round(pound / 2.20462)) + " " + unit

    elif unit in ounce and isinstance(pound, (float, int)):
        return str(round(pound / 0.0625)) + " " + unit

    else:
        return "invalid unit/number"


def weight_converter(weight, unit1, unit2):

    kilo = ["kilograms", "kilo", "kilos", "k"]
    ounce = ["ounces", "ounce", "oz"]
    pound = ["pounds", "lb"]

    if unit1 in kilo and isinstance(weight, (float, int)):
        return kilo_converter(weight, unit2)

    elif unit1 in ounce and isinstance(weight, (float, int)):
        return ounce_converter(weight, unit2)

    elif unit1 in pound and isinstance(weight, (float, int)):
        return pound_converter(weight, unit2)

    else:
        return "invalid unit/number"


def celsius_convert(degrees, unit):

    fahr = ["F", "f", "fahr", "fahrenheit"]

    if unit in fahr and isinstance(degrees, (float, int)):
        return str(round((degrees * 1.8) + 32)) + " " + unit

    else:
        return "invalid unit/number"


def fahrenheit_convert(degrees, unit):

    cels = ["C", "c", "cels", "celsius"]

    if unit in cels and isinstance(degrees, (float, int)):
        return str(round((degrees - 32) / 1.8)) + " " + unit

    else:
        return "invalid unit/number"


def temp_converter(temp, unit1, unit2):

    fahr = ["F", "f", "fahr", "fahrenheit"]
    cels = ["C", "c", "cels", "celsius"]
    
    if unit1 in cels and isinstance(temp, (float, int)):
        return celsius_convert(temp, unit2)

    elif unit1 in fahr and isinstance(temp, (float, int)):
        return fahrenheit_convert(temp, unit2)

    else:
        return "invalid unit/number"
    
# ============================================================

# Defining testing here

# ============================================================

def test_distance():

    
    assert inches_converter(24, "feet") == '2 feet'
    
    assert meters_converter(1, "inches") == '39 inches'

    assert feet_converter(3, "inches") == '36 inches'

    assert distance_convert(1609.34, "meters", "miles") == '1 miles'

    assert distance_convert(72, "inches", "feet") == '6 feet'   
    
    assert distance_convert(72, "ies", "et") == 'invalid unit/number'
    
def test_weight():
    
    assert weight_converter(1, "kilograms", "ounces") == '35 ounces'
    
    assert weight_converter(72, "ounces", "kilograms") == '2 kilograms'
    
    assert weight_converter(72, "ounces", "pounds") == '4 pounds'
                         
    assert weight_converter(5, "pounds", "ounces") == '80 ounces'
                           
    assert weight_converter(10, "kilograms", "pounds") == '22 pounds'
                            
    assert weight_converter(22, "pounds", "kilograms") == '10 kilograms'
                            
    assert weight_converter(10, "rr", "kilograms") == 'invalid unit/number' 
    
    
def test_temperature():
    
    assert temp_converter(32, "celsius", "fahrenheit") == '90 fahrenheit' 
    
    assert temp_converter(89.6, "fahrenheit", "celsius") == '32 celsius'
    
    assert temp_converter(32, "C", "celsius") == 'invalid unit/number'
    
    assert temp_converter(89.6, "f", "fahrenheit") == 'invalid unit/number'
    
    assert temp_converter(32, "celsius", "j") == 'invalid unit/number'
    
    assert temp_converter(89.6, "fahrenheit", "cas") == 'invalid unit/number'
    
    assert temp_converter(89.6, "fahrenheit", "case") == 'invalid unit/number'
