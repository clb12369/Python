convert_from = input("Enter starting unit of measurement (inches, feet, or yards): ")

convert_to = input("Enter desired ending unit of measurement (inches, feet, or yards): ")


if convert_from.lower() in ['inches', 'in', 'inch']:
    number_of_inches = int(input("Enter starting measure in inches: "))
    if convert_to.lower() in ['feet', 'foot', 'ft']:
        print(f"Result: {number_of_inches} Inches = {round(number_of_inches / 12, 2)} Feet")
    elif convert_to.lower() in ['yards', 'yard', 'yds', 'yd']:
        print(f"Result: {number_of_inches} Inches = {round(number_of_inches / 36, 2)} Yards")
    else:
        print("Please enter Inches, Feet, or Yards.")
elif convert_from.lower() in ['feet', 'foot', 'ft']:
    number_of_feet = int(input("Enter starting measure in feet: "))
    if convert_to.lower() in ['inches', 'in', 'inch']:
        print(f"Result: {number_of_feet} Feet = {round(number_of_feet * 12)} Inches")
    elif convert_to.lower() in ['yards', 'yard', 'yds', 'yd']:
        print(f"Result: {number_of_feet} Feet = {round(number_of_feet / 3, 2)} Yards")
    else:
        print("Please enter Inches, Feet, or Yards.")
elif convert_from.lower() in ['yards', 'yard', 'yds', 'yd']:
    number_of_yards = int(input("Enter starting measure in yards: "))
    if convert_to.lower() in ['inches', 'in', 'inch']:
        print(f"Result: {number_of_yards} Yards = {round(number_of_yards * 36)} Inches")
    elif convert_to.lower() in ['feet', 'foot', 'ft']:
        print(f"Result: {number_of_yards} Yards = {round(number_of_yards * 3)} Feet")
    else:
        print("Please enter Inches, Feet, or Yards.")
else:
        print("Please enter Inches, Feet, or Yards.")
