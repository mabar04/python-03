import math


def parsing_tuple(str):
    list_string = (str.split(",", 3))
    list_numbers = []
    try:
        for element in list_string:
            list_numbers += [int(element)]
    except ValueError:
        print(f"Error parsing coordinates: invalid literal for int()"
              f" with base 10: '{element}'")
        print(f"Error details - Type: ValueError, Args: "
              f"(\"invalid literal for int() with base 10: '{element}'\",)")
        return
    return list_numbers


print("=== Game Coordinate System ===\n")
tuple1 = (10, 20, 5)
print(f"Position created: {tuple1}")
distance1 = math.sqrt((tuple1[0] - 0)**2 + (tuple1[1] - 0)**2
                      + (tuple1[2] - 0)**2)
print(f"Distance between (0, 0, 0) and {tuple1}: {distance1:.2f}")
print()
str1 = "3,4,0"
print(f"Parsing coordinates: {str1}")
tuple2 = tuple(parsing_tuple(str1))
print(f"Parsed position: {tuple2}")
distance2 = math.sqrt((tuple2[0] - 0)**2 + (tuple2[1] - 0)**2
                      + (tuple2[2] - 0)**2)
print(f"Distance between (0, 0, 0) and {tuple1}: {distance2:.2f}")
print()
str2 = "abc,def,ghi"
print(f'Parsing coordinates: "{str2}"')
parsing_tuple(str2)
print("\n")
print("Unpacking demonstration:")
x, y, z = tuple2
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
