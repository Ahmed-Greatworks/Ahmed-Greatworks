def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    operand1 = []
    operand2 = []
    signs = []

    for problem in problems:
        problem_split = problem.split(' ')

        operand1.append(problem_split[0])
        signs.append(problem_split[1])
        operand2.append(problem_split[2])
    
    # Check for * or /
    if "*" in signs or "/" in signs:
        return "Error: Operator must be '+' or '-'."

    # Check the digits
    for i in range(len(operand1)):
        if not (operand1[i].isdigit() and operand2[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check the length
    for i in range(len(operand1)):
        if len(operand1[i]) > 4 or len(operand2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."
    
    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for i in range(len(operand1)):
        if len(operand1[i]) > len(operand2[i]):
            line1.append(f"{' '* 2}{operand1[i]}")
        else:
            line1.append(f"{' ' * (len(operand2[i]) - len(operand1[i]) + 2)}{operand1[i]}")

    for i in range(len(operand2)):
        if len(operand2[i]) > len(operand1[i]):
            line2.append(signs[i] + " " + operand2[i])
        else:
            line2.append(f'{signs[i]}{" "*(len(operand1[i]) - len(operand2[i]) + 1)}{operand2[i]}')
    
    for i in range(len(operand1)):
        line3.append(f'{"-"*(max(len(operand1[i]), len(operand2[i])) + 2)}')
    
    if show_answers:
        for i in range(len(signs)):
            if signs[i] == "+":
                ans = str(int(operand1[i]) + int(operand2[i]))
            else:
                ans = str(int(operand1[i]) - int(operand2[i]))

            if len(ans) > max(len(operand1[i]), len(operand2[i])):
                line4.append(" " + ans)
            else:
                line4.append(" "*(max(len(operand1[i]), len(operand2[i])) - len(ans) + 2) + ans)
        result = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3) + "\n" + "    ".join(line4)
    else:
        result = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
    
    return result

print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
