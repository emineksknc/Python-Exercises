# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

"""

1 kilopascal = 0.145037738 pounds per square inch
1 kilopascal = 7.50061683 mmhg
1 kilopascal = 0.0098692327 atm (https://www.unitconverters.net/pressure/kilopascal-to-standard-atmosphere.htm)

"""

a_kilopascal_to_per_square_inch = 0.145037738
a_kilopascal_to_millimeter_of_mercury = 7.50061683
a_kilopascal_to_atmosphere_pressure = 0.0098692327


def convert_a_kilopascal_to_per_square_inch(kilopascal):
    return kilopascal * a_kilopascal_to_per_square_inch


def convert_a_kilopascal_to_millimeter_of_mercury(kilopascal):
    return kilopascal * a_kilopascal_to_millimeter_of_mercury


def convert_a_kilopascal_to_atmosphere_pressure(kilopaskal):
    return kilopaskal * a_kilopascal_to_atmosphere_pressure


def main():
    pascal = 12
    per_square_inch = convert_a_kilopascal_to_per_square_inch(pascal)
    millimeter_of_mercury = convert_a_kilopascal_to_millimeter_of_mercury(pascal)
    atmosphere_pressure = convert_a_kilopascal_to_atmosphere_pressure(pascal)
    print(f'{pascal} Pascal = {round(per_square_inch, 2)}  per square inch \n'
          f'{pascal} Pascal = {round(millimeter_of_mercury, 2)} millimeter of mercury \n'
          f'{pascal} Pascal = {round(atmosphere_pressure, 2)} atmosphere pressure \n')


if __name__ == "__main__":
    main()
