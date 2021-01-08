# FCC-Python-Certification-Projectrith
# Arithmetic Formatter

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

# For example
# Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  
# Function Call:
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

# Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
  
# Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

# Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.

If the user supplied the correct format of problems, the conversion you return will follow these rules:

There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)


# Assignment
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
 
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
 
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
 
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
 
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
 
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
