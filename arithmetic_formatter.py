def arithmetic_arranger(problems, show_answers=False):
    formatted = ''
    for problem in problems:
        if '+' in problem:
            splited_problem = problem.split('+')
            line1 = splited_problem[0].strip()
            line2 = splited_problem[1].strip()
            space_needed = abs(len(line1) - len(line2))
            space1 = ''
            space2 = ''
            if len(line1) < len(line2):
                space1 = ' ' * space_needed
            elif len(line2) < len(line1):
                space2 = ' ' * space_needed
            formatted += f"  {space1}{line1}\t"
            # print('+ ' + space2 + line2)
            # print('--' + '-' * max(len(line1), len(line2)))
        elif '-' in problem:
            splited_problem = problem.split('-')
            line1 = splited_problem[0].strip()
            line2 = splited_problem[1].strip()
            space_needed = abs(len(line1) - len(line2))
            space1 = ''
            space2 = ''
            if len(line1) < len(line2):
                space1 = ' ' * space_needed
            elif len(line2) < len(line1):
                space2 = ' ' * space_needed
            formatted += f"  {space1}{line1}\t"
            # print('- ' + space2 + line2)
            # print('--' + '-' * max(len(line1), len(line2)))
    formatted += '\n'
    for problem in problems:
        if '+' in problem:
            splited_problem = problem.split('+')
            line1 = splited_problem[0].strip()
            line2 = splited_problem[1].strip()
            space_needed = abs(len(line1) - len(line2))
            space1 = ''
            space2 = ''
            if len(line1) < len(line2):
                space1 = ' ' * space_needed
            elif len(line2) < len(line1):
                space2 = ' ' * space_needed
            formatted += f"+ {space2}{line2}\t"
        elif '-' in problem:
            splited_problem = problem.split('-')
            line1 = splited_problem[0].strip()
            line2 = splited_problem[1].strip()
            space_needed = abs(len(line1) - len(line2))
            space1 = ''
            space2 = ''
            if len(line1) < len(line2):
                space1 = ' ' * space_needed
            elif len(line2) < len(line1):
                space2 = ' ' * space_needed
            formatted += f"- {space2}{line2}\t"
        
    formatted += '\n'
    for problem in problems:
        if '+' in problem:
            splited_problem = problem.split('+')
            line1 = splited_problem[0].strip()
            line2 = splited_problem[1].strip()
            formatted += '--' + '-' * max(len(line1), len(line2)) + '\t'
        elif '-' in problem:
            splited_problem = problem.split('-')
            line1 = splited_problem[0].strip()
            line2 = splited_problem[1].strip()
            formatted += '--' + '-' * max(len(line1), len(line2)) + '\t'
    
    formatted += '\n'
    for problem in problems:
        if '+' in problem:
            splited_problem = problem.split('+')
            line1 = splited_problem[0].strip()
            line2 = splited_problem[1].strip()
            formatted += '--' + '-' * max(len(line1), len(line2)) + '\t'
        elif '-' in problem:
            splited_problem = problem.split('-')
            line1 = splited_problem[0].strip()
            line2 = splited_problem[1].strip()
            formatted += '--' + '-' * max(len(line1), len(line2)) + '\t'

    return formatted
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])}')
