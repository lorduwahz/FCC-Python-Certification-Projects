def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    num1 = ""
    oprtr = ""
    num2 = ""
    spaces = "    "
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        values = problem.split(" ")

        if len(values[0]) > 4 or len(values[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(values[0]), len(values[2]))

        if not values[0].isnumeric():
            return "Error: Numbers must only contain digits."
        
        if not values[2].isnumeric():
            return "Error: Numbers must only contain digits."

        num1 = int(values[0].rstrip())
        oprtr = values[1].rstrip()
        num2 = int(values[2].rstrip())

        if oprtr == '+':
            result = num1 + num2
        elif oprtr == '-':
            result = num1 - num2
        else:
            return "Error: Operator must be '+' or '-'."

        line1 += (str(num1)).rjust(width + 2) + spaces
        line2 += str(oprtr) + " " + (str(num2)).rjust(width) + spaces
        line3 += ("-" * (width + 2)).rjust(width) + spaces
        line4 += (str(result).rjust(width + 2)) + spaces

    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

    if solve:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()

    return arranged_problems      
