from phase1 import *

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
