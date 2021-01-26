
## define functions

def distance_converter(distance, unit1, unit2):

    # The user input/arguments would be the quantity(distance,weight, temperature)
    # unit1 and unit2 are the current unit and the united converted to respectively
    # unit1 and unit2 are strings
    # distance, weight, and temp are all int/float types.
   
    if unit1 in "meters" and unit2 in "feet":
        return str(distance * 3.28) + " " + unit2

    elif unit1 in "meters" and unit2 in "inches":
        return str(distance * 39.37) + " " + unit2

    elif unit1 in "meters" and unit2 in "miles":
        return str(distance * 0.000621) + " " + unit2

    elif unit1 in "feet" and unit2 in "meters":
        return str(distance / 3.28) + " " + unit2

    elif unit1 in "feet" and unit2 in "inches":
        return str(distance * 12) + " " + unit2

    elif unit1 in "feet" and unit2 in "miles":
        return str(distance * 0.000189) + " " + unit2

    elif unit1 in "inches" and unit2 in "feet":
        return str(distance / 12) + " " + unit2

    elif unit1 in "inches" and unit2 in "miles":
        return str(distance * 0.000189 / 12) + " " + unit2

    elif unit1 in "inches" and unit2 in "meters":
        return str(distance * 0.0254) + " " + unit2

    elif unit1 in "miles" and unit2 in "feet":
        return str(distance / 0.000189) + " " + unit2

    elif unit1 in "miles" and unit2 in "inches":
        return str((distance * 12) / 0.000189) + " " + unit2

    else:
        return str(distance / 0.000621) + " " + unit2


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


