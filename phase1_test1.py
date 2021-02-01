from phase1 import *

# ============================================================

# Defining testing here

# ============================================================

def test_distance():

    
    assert inches_converter(24, "feet") == '2 feet'
    assert inches_converter(126984, "miles") == '2 miles'
    assert inches_converter(4800, "meters") == '122 meters'    
    assert meters_converter(1, "inches") == '39 inches'
    assert feet_converter(3, "inches") == '36 inches'
    assert distance_convert(1609.34, "meters", "miles") == '1 miles'
    assert distance_convert(72, "inches", "feet") == '6 feet'      
    assert inches_converter(24, "ft") == '2 ft'
    assert meters_converter(1, "ft") == '3 ft'
    assert miles_converter(2, "m") == '3221 m'
    assert distance_convert(72, "in", "ft") == '6 ft'    
    assert distance_convert(72, "ies", "et") == 'invalid unit/number'
    assert distance_convert("asdf", "in", "ft") == 'invalid unit/number'
    assert distance_convert(2, "miles", "inches") == '126984 inches'
    assert distance_convert(400, "feet", "meters") == '122 meters' 
    
def test_weight():
    
    assert weight_converter(1, "kilograms", "ounces") == '35 ounces'
    assert weight_converter(72, "ounces", "kilograms") == '2 kilograms'
    assert weight_converter(72, "ounces", "pounds") == '4 pounds'
    assert weight_converter(5, "pounds", "ounces") == '80 ounces'
    assert weight_converter(10, "kilos", "pounds") == '22 pounds'
    assert weight_converter(22, "lb", "kilo") == '10 kilo'
    assert weight_converter(10, "rr", "kilograms") == 'invalid unit/number'
    assert weight_converter(72, "oz", "k") == '2 k'
    assert weight_converter(72, "ounces", "pounds") == '4 pounds'
    assert weight_converter(5, "lb", "oz") == '80 oz'
    assert weight_converter(10, "k", "lb") == '22 lb'
    assert weight_converter(22, "pounds", "kilos") == '10 kilos'
    assert weight_converter(10, "rr", "ki") == 'invalid unit/number'    
    
def test_temperature():
    
    assert temp_converter(32, "celsius", "fahrenheit") == '90 fahrenheit' 
    assert temp_converter(89.6, "fahrenheit", "celsius") == '32 celsius'   
    assert temp_converter(32, "H", "celsius") == 'invalid unit/number'   
    assert temp_converter(89.6, "k", "fahrenheit") == 'invalid unit/number'    
    assert temp_converter(32, "celsius", "j") == 'invalid unit/number'    
    assert temp_converter(89.6, "fahrenheit", "cas") == 'invalid unit/number'    
    assert temp_converter(89.6, "fahrenheit", "case") == 'invalid unit/number'
    assert temp_converter(33, "c", "f") == '91 f'
    assert temp_converter(32, "f", "C") == '0 C'
    assert temp_converter(89.6, "fahr", "cels") == '32 cels'
    assert temp_converter(32, "celsius", "fahr") == '90 fahr'
    assert temp_converter(32, "c", "F") == '90 F'
    assert temp_converter(89.6, "f", "c") == '32 c'
    assert temp_converter(32, "F", "celsius") == '0 celsius'
    assert temp_converter(89.6, "C", "fahrenheit") == '193 fahrenheit'
    assert temp_converter('r', "f", "c") == 'invalid unit/number'      
