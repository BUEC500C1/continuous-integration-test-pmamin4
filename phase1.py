#===================

#define functions

#===================

def meters_converter(meters, unit):
    
    inch = ["inches", "in"]
    feet = ["feet", "ft"]
    mile = ["miles", "mi"]

    if unit in inch:
        return str(round(meters * 39.37)) + " " + unit

    elif unit in feet:
        return str(round(meters * 3.28)) + " " + unit

    elif unit in mile:
        return str(round(meters * 0.000621)) + " " + unit

    else:
        return "invalid unit"


def inches_converter(inches, unit):
    
    feet = ["feet", "ft"]
    mile = ["miles", "mi"]
    meter = ["meters", "m"]

    if unit in feet:
        return str(round(inches / 12)) + " " + unit

    elif unit in mile:
        return str(round(inches * 0.000189 / 12)) + " " + unit

    elif unit in meter:
        return str(round(inches * 0.0254)) + " " + unit

    else:
        return "invalid unit"


def feet_converter(feet, unit):
    
    inch = ["inches", "in"]
    mile = ["miles", "mi"]
    meter = ["meters", "m"]

    if unit in inch:
        return str(round(feet * 12)) + " " + unit

    elif unit in mile:
        return str(round(feet * 0.000189)) + " " + unit

    elif unit in meter:
        return str(round(feet / 3.28)) + " " + unit

    else:
        return "invalid unit"


def miles_converter(miles, unit):
    
    inch = ["inches", "in"]
    feet = ["feet", "ft"]
    meter = ["meters", "m"]

    if unit in inch:
        return str(round((miles * 12) / 0.000189)) + " " + unit

    elif unit in feet:
        return str(round(miles / 0.000189)) + " " + unit

    elif unit in meter:
        return str(round(miles / 0.000621)) + " " + unit

    else:
        return "invalid unit"


def distance_convert(distance, unit1, unit2):
    
    inch = ["inches", "in"]
    feet = ["feet", "ft"]
    mile = ["miles", "mi"]
    meter = ["meters", "m"]

    if unit1 in meter:
        return meters_converter(distance, unit2)

    elif unit1 in feet:
        return feet_converter(distance, unit2)

    elif unit1 in mile:
        return miles_converter(distance, unit2)

    elif unit1 in inch:
        return inches_converter(distance, unit2)
    else:
        return "invalid unit"


def weight_converter(weight, unit1, unit2):
    
    kilo = ["kilograms", "kilo", "k"]
    ounce = ["ounces", "oz"]
    pound = ["pounds", "lb"]

    if unit1 in kilo and unit2 in ounce:
        return str(round(weight * 35.274)) + " " + unit2

    elif unit1 in kilo and unit2 in pound:
        return str(round(weight * 2.20462)) + " " + unit2

    elif unit1 in ounce and unit2 in kilo:
        return str(round(weight / 35.274)) + " " + unit2

    elif unit1 in ounce and unit2 in pound:
        return str(round(weight * 0.0625)) + " " + unit2

    elif unit1 in pound and unit2 in kilo:
        return str(round(weight / 2.20462)) + " " + unit2

    elif unit1 in pound and unit2 in ounce:
        return str(round(weight / 0.0625)) + " " + unit2
    else:
        return "invalid unit"

def celsius_convert(degrees, unit):

    fahr = ["F", "f", "fahr", "fahrenheit"]
    if unit in fahr:
        return str(round((degrees * 1.8) + 32)) + " " + unit

    else:
        return "invalid unit"


def fahrenheit_convert(degrees, unit):

    cels = ["C", "c", "cels", "celsius"]
    if unit in cels:
        return str(round((degrees - 32) / 1.8)) + " " + unit

    else:
        return "invalid unit"


def temp_converter(temp, unit1, unit2):

    fahr = ["F", "f", "fahr", "fahrenheit"]
    cels = ["C", "c", "cels", "celsius"]
    if unit1 in cels:
        return celsius_convert(temp, unit2)

    elif unit1 in fahr:
        return fahrenheit_convert(temp, unit2)

    else:
        return "invalid unit"


    
    
# ============================================================

# Defining testing here

# ============================================================

def test_distance():

    
    assert inches_converter(24, "feet") == '2 feet'
    
    assert meters_converter(1, "inches") == '39 inches'

    assert feet_converter(3, "inches") == '36 inches'

    assert distance_convert(1609.34, "meters", "miles") == '1 miles'

    assert distance_convert(72, "inches", "feet") == '6 feet'   
    
    assert distance_convert(72, "ies", "et") == 'invalid unit'
    
def test_weight():
    
    assert weight_converter(1, "kilograms", "ounces") == '35 ounces'
    
    assert weight_converter(72, "ounces", "kilograms") == '2 kilograms'
    
    assert weight_converter(72, "ounces", "pounds") == '4 pounds'
                         
    assert weight_converter(5, "pounds", "ounces") == '80 ounces'
                           
    assert weight_converter(10, "kilograms", "pounds") == '22 pounds'
                            
    assert weight_converter(22, "pounds", "kilograms") == '10 kilograms'
                            
    assert weight_converter(10, "rr", "kilograms") == 'invalid unit' 
    
    
def test_temperature():
    
    assert temp_converter(32, "celsius", "fahrenheit") == '90 fahrenheit' 
    
    assert temp_converter(89.6, "fahrenheit", "celsius") == '32 celsius'
    
    assert temp_converter(32, "C", "celsius") == 'invalid unit'
    
    assert temp_converter(89.6, "f", "fahrenheit") == 'invalid unit'
    
    assert temp_converter(32, "celsius", "j") == 'invalid unit'
    
    assert temp_converter(89.6, "fahrenheit", "cas") == 'invalid unit'
    
    assert temp_converter(89.6, "fahrenheit", "case") == 'invalid unit'
