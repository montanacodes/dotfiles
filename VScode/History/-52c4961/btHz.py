# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return convert_distance

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(55)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
def round_trip():
	full = my_trip_km * 2
	return round_trip()
print("The round-trip in kilometers is " + str(round_trip))

##Not quite. Remember to use the str() function to convert
##numbers into strings when printing them with text, and to
call the function with just one parameter, then accept the
##return value into a new variable.
#-----------------------

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#-------------------------------

def lucky_number(name):
  number = len(name) * 9
  print = "Hello " + name + ". Your lucky number is " + str(number)
  return lucky_number
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

##Not quite. You may want to review the videos in this lesson
##to see how functions return variables.